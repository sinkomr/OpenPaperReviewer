"""Tests for validate_review.py. Run with: python3 -m unittest discover -s tests"""
import importlib.util
import json
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
FIXTURE = ROOT / "tests" / "fixtures" / "good-review"
SCRIPT = ROOT / "plugin" / "skills" / "open-paper-reviewer" / "scripts" / "validate_review.py"

_spec = importlib.util.spec_from_file_location("validate_review", SCRIPT)
validator = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(validator)


class ReviewCase(unittest.TestCase):
    def setUp(self):
        self.tmp = Path(tempfile.mkdtemp())
        self.folder = self.tmp / "https-example.org-fictional-mulch-study" / "v1" / "example-reviewer-2026-01-15"
        shutil.copytree(FIXTURE, self.folder)

    def tearDown(self):
        shutil.rmtree(self.tmp)

    def edit_json(self, name, change):
        path = self.folder / name
        data = json.loads(path.read_text(encoding="utf-8"))
        change(data)
        path.write_text(json.dumps(data, indent=2), encoding="utf-8")

    def edit_text(self, name, old, new):
        path = self.folder / name
        text = path.read_text(encoding="utf-8")
        self.assertIn(old, text)
        path.write_text(text.replace(old, new), encoding="utf-8")

    def claim(self, data, claim_id):
        return next(item for item in data["claims"] if item["id"] == claim_id)

    def citation(self, data, citation_id):
        return next(item for item in data["citations"] if item["id"] == citation_id)

    def make_postable(self):
        (self.folder / "00_extraction.md").unlink()

    def errors(self, **options):
        return validator.validate(self.folder, **options).errors

    def assert_fails(self, fragment, **options):
        errors = self.errors(**options)
        self.assertTrue(any(fragment in line for line in errors), f"no error containing {fragment!r} in {errors}")


class ValidFixture(ReviewCase):
    def test_valid_as_a_local_run(self):
        self.assertEqual(self.errors(), [])

    def test_valid_for_posting(self):
        self.make_postable()
        self.assertEqual(self.errors(posting=True, check_path=True), [])

    def test_command_line_exit_codes(self):
        ok = subprocess.run([sys.executable, str(SCRIPT), str(self.folder)], capture_output=True, text=True)
        self.assertEqual(ok.returncode, 0, ok.stdout)
        self.edit_json("claims.json", lambda d: self.claim(d, "A-01").update(verdict="Fine"))
        bad = subprocess.run([sys.executable, str(SCRIPT), str(self.folder), "--json"], capture_output=True, text=True)
        self.assertEqual(bad.returncode, 1)
        self.assertFalse(json.loads(bad.stdout)["ok"])


class RubricDrift(ReviewCase):
    """Values outside the rubric must all be rejected, including near misses a model might write."""

    def test_verdict_outside_the_rubric(self):
        for value in ("Not Supported", "Partly Supported", "Likely Wrong", "supported"):
            with self.subTest(value=value):
                self.edit_json("claims.json", lambda d, v=value: self.claim(d, "B-02").update(verdict=v))
                self.assert_fails("B-02 verdict")

    def test_severity_outside_the_rubric(self):
        for value in ("Severe", "Moderate", "Minor to Major"):
            with self.subTest(value=value):
                self.edit_json("claims.json", lambda d, v=value: self.claim(d, "B-02").update(severity=v))
                self.assert_fails("B-02 severity")

    def test_confidence_outside_the_rubric(self):
        self.edit_json("claims.json", lambda d: self.claim(d, "B-02").update(confidence="Medium-High"))
        self.assert_fails("B-02 confidence")

    def test_supported_claim_cannot_carry_a_severity(self):
        self.edit_json("claims.json", lambda d: self.claim(d, "A-01").update(severity="Minor"))
        self.assert_fails("severity must be null")

    def test_other_verdicts_need_a_severity(self):
        self.edit_json("claims.json", lambda d: self.claim(d, "B-02").update(severity=None))
        self.assert_fails("severity is required")

    def test_tier_must_be_a_number_from_the_rubric(self):
        for value in ("2", 4, True):
            with self.subTest(value=value):
                self.edit_json("claims.json", lambda d, v=value: self.claim(d, "B-01").update(tier=v))
                self.assert_fails("B-01 tier")

    def test_claim_type_outside_the_rubric(self):
        self.edit_json("claims.json", lambda d: self.claim(d, "B-01").update(type="measurement/data"))
        self.assert_fails("B-01 type")


class RunRecord(ReviewCase):
    def test_model_identifier_is_required(self):
        for value in ("", "unknown", None):
            with self.subTest(value=value):
                self.edit_json("run.json", lambda d, v=value: d["models"][0].update(id=v))
                self.assert_fails("id is missing")

    def test_effort_is_required(self):
        for value in ("", "unknown", "none", None):
            with self.subTest(value=value):
                self.edit_json("run.json", lambda d, v=value: d["models"][0].update(effort=v))
                self.assert_fails("effort is missing")

    def test_a_tool_without_an_effort_setting_can_say_so(self):
        self.edit_json("run.json", lambda d: d["models"][0].update(effort="none exposed"))
        self.edit_text("06_synthesis.md", "effort: high", "effort: none exposed")
        self.assertEqual(self.errors(), [])

    def test_tool_version_is_required(self):
        for value in ("", None):
            with self.subTest(value=value):
                self.edit_json("run.json", lambda d, v=value: d["tool"].update(version=v))
                self.assert_fails("tool.version is missing")

    def test_a_tool_that_does_not_show_its_version_can_say_unknown(self):
        self.edit_json("run.json", lambda d: d["tool"].update(version="unknown"))
        report = validator.validate(self.folder)
        self.assertEqual(report.errors, [])
        self.assertTrue(any("tool.version is not known" in line for line in report.warnings), report.warnings)
        self.make_postable()
        self.assertEqual(self.errors(posting=True), [])

    def test_source_of_model_values_is_required(self):
        self.edit_json("run.json", lambda d: d["models"][0].update(id_source="guessed"))
        self.assert_fails("id_source")

    def test_every_phase_needs_a_recorded_model(self):
        self.edit_json("run.json", lambda d: d["models"][0].update(phases=["0", "1", "2", "3"]))
        self.assert_fails("no model is recorded for phase(s) 4, 5, 6, 7")

    def test_prompt_file_is_required(self):
        (self.folder / "prompt.md").unlink()
        self.assert_fails("prompt.md: file is missing")

    def test_prompt_request_cannot_be_empty(self):
        self.edit_text("prompt.md", "Please review the attached paper on mulch depth and tomato yield.", "")
        self.assert_fails('section "## Request" is empty')

    def test_focused_review_must_list_concerns(self):
        self.edit_json("run.json", lambda d: d["review"].update(concerns=[]))
        self.assert_fails("must list the concerns")

    def test_standard_review_has_no_concerns(self):
        self.edit_json("run.json", lambda d: d["review"].update(mode="standard"))
        self.assert_fails("a standard review has no concerns")

    def test_non_interactive_run_is_standard(self):
        self.edit_json("run.json", lambda d: d["review"].update(intake="not_interactive"))
        self.assert_fails("could not ask the intake question")

    def test_dates(self):
        self.edit_json("run.json", lambda d: d["review"].update(finished="15 Jan 2026"))
        self.assert_fails("review.finished must be a date")

    def test_synthesis_must_name_the_model_and_effort(self):
        self.edit_text("06_synthesis.md", "example-model-1", "a model")
        self.assert_fails("must name the model used")


class Claims(ReviewCase):
    def test_quote_limit(self):
        long_text = " ".join(["word"] * 61)
        self.edit_json("claims.json", lambda d: self.claim(d, "A-02").update(text=long_text))
        self.assert_fails("text is 61 words")

    def test_duplicate_ids(self):
        self.edit_json("claims.json", lambda d: self.claim(d, "A-02").update(id="A-01"))
        self.assert_fails("duplicate id")

    def test_malformed_id(self):
        self.edit_json("claims.json", lambda d: self.claim(d, "A-02").update(id="A2"))
        self.assert_fails("id must look like A-01")

    def test_blocked_by_must_name_a_real_claim(self):
        self.edit_json("claims.json", lambda d: self.claim(d, "B-02").update(blocked_by=["Z-09"]))
        self.assert_fails("blocked_by names Z-09")

    def test_blocked_claim_cannot_be_supported(self):
        self.edit_json("claims.json", lambda d: self.claim(d, "B-01").update(blocked_by=["A-02"]))
        self.assert_fails("cannot be Supported")

    def test_failed_headline_claim_is_critical(self):
        for verdict in ("Unsupported", "Contradicted"):
            with self.subTest(verdict=verdict):
                self.edit_json("claims.json", lambda d, v=verdict: self.claim(d, "B-02").update(verdict=v, severity="Major"))
                self.assert_fails("severity must be Critical")

    def test_narrower_headline_claim_is_major(self):
        self.edit_json("claims.json", lambda d: self.claim(d, "B-02").update(verdict="Partially Supported", severity="Minor"))
        self.assert_fails("severity must be Major")

    def test_headline_rule_leaves_other_claims_alone(self):
        self.edit_json("claims.json", lambda d: self.claim(d, "B-02").update(headline=False, severity="Major"))
        self.assertFalse(any("for a headline claim" in line for line in self.errors()))

    def test_critical_needs_a_checkable_basis(self):
        self.edit_json("claims.json", lambda d: self.claim(d, "B-02").update(severity="Critical", basis=[]))
        self.assert_fails("needs a basis anyone can check")

    def test_contradicted_cannot_rest_on_an_unverified_source(self):
        def unverify(data):
            self.citation(data, "C-002").update(status="unverified", access="metadata", quote=None)

        self.edit_json("citations.json", unverify)
        self.assert_fails("needs a basis anyone can check")

    def test_basis_must_be_a_location_or_citation_id(self):
        self.edit_json("claims.json", lambda d: self.claim(d, "B-02").update(basis=["everyone knows this"]))
        self.assert_fails("basis entry")

    def test_every_claim_needs_a_scrutiny_block(self):
        path = self.folder / "03_scrutiny" / "group_B.md"
        path.write_text(path.read_text(encoding="utf-8").replace("B-04", "B-99"), encoding="utf-8")
        self.assert_fails("B-04: has no block in the scrutiny files")

    def test_every_claim_must_be_in_the_synthesis_table(self):
        self.edit_text("06_synthesis.md", "B-04", "one claim")
        self.assert_fails("must list every claim; missing: B-04")


class Citations(ReviewCase):
    def test_confirmed_source_must_have_been_opened(self):
        self.edit_json("citations.json", lambda d: self.citation(d, "C-001").update(access="metadata"))
        self.assert_fails("must have been opened")

    def test_confirmed_source_needs_a_quote(self):
        self.edit_json("citations.json", lambda d: self.citation(d, "C-001").update(quote=""))
        self.assert_fails("quote is required")

    def test_quote_limit(self):
        long_quote = " ".join(["word"] * 41)
        self.edit_json("citations.json", lambda d: self.citation(d, "C-001").update(quote=long_quote))
        self.assert_fails("quote is 41 words")

    def test_corrected_source_must_name_the_error(self):
        self.edit_json("citations.json", lambda d: self.citation(d, "C-004").update(error=None))
        self.assert_fails("must say what kind of error")

    def test_confirmed_source_has_no_error(self):
        self.edit_json("citations.json", lambda d: self.citation(d, "C-001").update(error="unsupported"))
        self.assert_fails("a confirmed source has no error")

    def test_status_outside_the_rubric(self):
        self.edit_json("citations.json", lambda d: self.citation(d, "C-003").update(status="probably fine"))
        self.assert_fails("C-003 status")

    def test_used_for_must_point_at_something_real(self):
        self.edit_json("citations.json", lambda d: self.citation(d, "C-001").update(used_for=["Q-77"]))
        self.assert_fails("used_for entry 'Q-77'")

    def test_verification_line_must_match_the_table(self):
        self.edit_text("06_synthesis.md", "| Citation verification | partial |", "| Citation verification | all |")
        self.assert_fails("says citation verification is 'all'")

    def test_run_record_verification_must_match_the_table(self):
        self.edit_json("run.json", lambda d: d["review"].update(citation_verification="all"))
        self.assert_fails("review.citation_verification is 'all'")

    def test_no_web_access_means_none(self):
        def unverify_all(data):
            for item in data["citations"]:
                if item["status"] != "removed":
                    item.update(status="unverified", access="none", quote=None, error=None)

        self.edit_json("citations.json", unverify_all)
        self.assert_fails("citations.json makes it 'none'")


class NoOutsideSources(ReviewCase):
    def drop_sources(self, web_access, line):
        self.edit_json("citations.json", lambda d: d.update(citations=[]))
        for claim_id in ("B-02", "B-03"):
            self.edit_json("claims.json", lambda d, c=claim_id: self.claim(d, c).update(basis=["paper: Table 1"]))
        self.edit_json("run.json", lambda d: (d.update(web_access=web_access), d["review"].update(citation_verification=line)))
        self.edit_text("06_synthesis.md", "| Citation verification | partial |", f"| Citation verification | {line} |")

    def test_offline_review_with_no_sources_says_none(self):
        self.drop_sources(web_access=False, line="none")
        self.assertEqual(self.errors(), [])

    def test_online_review_with_no_sources_says_all(self):
        self.drop_sources(web_access=True, line="all")
        self.assertEqual(self.errors(), [])

    def test_offline_review_with_no_sources_cannot_say_all(self):
        self.drop_sources(web_access=False, line="all")
        self.assert_fails("citations.json makes it 'none'")


class Structure(ReviewCase):
    def test_missing_phase_output(self):
        (self.folder / "05_methods.md").unlink()
        self.assert_fails("05_methods: phase output is missing")

    def test_phase_may_be_one_file_instead_of_a_folder(self):
        parts = sorted((self.folder / "03_scrutiny").glob("*.md"))
        (self.folder / "03_scrutiny.md").write_text("\n".join(p.read_text(encoding="utf-8") for p in parts), encoding="utf-8")
        shutil.rmtree(self.folder / "03_scrutiny")
        self.assertEqual(self.errors(), [])

    def test_what_the_paper_establishes_is_required(self):
        self.edit_text("06_synthesis.md", "## 2. What the paper establishes", "## 2. Strengths")
        self.assert_fails('"What the paper establishes" is required')

    def test_focused_review_must_answer_the_concerns(self):
        self.edit_text("06_synthesis.md", "## 5. Concerns raised at intake", "## 5. Other notes")
        self.assert_fails("needs a section answering the concerns")


class Posting(ReviewCase):
    def setUp(self):
        super().setUp()
        self.make_postable()

    def test_extraction_is_not_posted(self):
        (self.folder / "00_extraction.md").write_text("abstract and reference list", encoding="utf-8")
        self.assert_fails("must not be posted", posting=True)

    def test_the_paper_itself_is_never_posted(self):
        (self.folder / "paper.pdf").write_bytes(b"%PDF-1.7")
        self.assert_fails("only .md, .json and .txt files can be posted", posting=True)

    def test_human_check_is_required(self):
        self.edit_json("run.json", lambda d: d.update(human_check=""))
        self.assert_fails("human_check is missing", posting=True)

    def test_human_check_may_honestly_be_none(self):
        self.edit_json("run.json", lambda d: d.update(human_check="none"))
        self.edit_text("06_synthesis.md", "Read the synthesis and compared claims A-02 and B-01 with Table 1 of the paper.", "none")
        self.assertEqual(self.errors(posting=True), [])

    def test_conflicts_of_interest_are_required(self):
        self.edit_json("run.json", lambda d: d.pop("conflicts_of_interest"))
        self.assert_fails("conflicts_of_interest is missing", posting=True)

    def test_reviewer_handle_is_required(self):
        self.edit_json("run.json", lambda d: d.update(reviewer="not a handle"))
        self.assert_fails("GitHub handle", posting=True)

    def test_only_public_papers(self):
        self.edit_json("run.json", lambda d: d["paper"].update(public=False))
        self.assert_fails("publicly available", posting=True)

    def test_identifier_must_be_public(self):
        self.edit_json("run.json", lambda d: d["paper"].update(identifier="internal draft"))
        self.assert_fails("paper.identifier must start with", posting=True)

    def test_folder_must_sit_at_the_expected_path(self):
        moved = self.tmp / "somewhere" / "else" / "review"
        moved.parent.mkdir(parents=True)
        shutil.move(str(self.folder), str(moved))
        self.folder = moved
        self.assert_fails("must be at https-example.org-fictional-mulch-study/v1/example-reviewer-2026-01-15/", posting=True, check_path=True)

    def test_local_run_without_posting_fields_is_still_valid(self):
        (self.folder / "00_extraction.md").write_text("# Extraction\n", encoding="utf-8")
        self.edit_json("run.json", lambda d: [d.pop(key) for key in ("reviewer", "human_check", "conflicts_of_interest")])
        self.assertEqual(self.errors(), [])


if __name__ == "__main__":
    unittest.main()
