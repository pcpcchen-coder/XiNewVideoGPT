import importlib.util
import json
import tempfile
import unittest
from pathlib import Path

spec = importlib.util.spec_from_file_location("academy", Path(__file__).resolve().parents[1] / "pipeline/academy.py")
a = importlib.util.module_from_spec(spec)
spec.loader.exec_module(a)
ORIGINAL = a.ROOT


class IntegrationTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        a.ROOT = Path(self.tmp.name)

    def tearDown(self):
        a.ROOT = ORIGINAL
        self.tmp.cleanup()

    def test_init_preserves_curriculum_and_refuses_overwrite(self):
        catalog = ORIGINAL / "curriculum/catalog.json"
        before = a.sha(catalog)
        a.init_lesson(catalog, "L001")
        lesson = a.read(a.ROOT / "lessons/L001/lesson.json")
        self.assertEqual(len(lesson["resources"]), 3)
        self.assertIn("MacBook", lesson["sourceRow"]["課程主題"])
        with self.assertRaises(FileExistsError): a.init_lesson(catalog, "L001")
        self.assertEqual(before, a.sha(catalog))

    def test_srt_import_retains_timestamps_and_refuses_overwrite(self):
        a.init_lesson(ORIGINAL / "curriculum/catalog.json", "L001")
        srt = a.ROOT / "sample.srt"
        srt.write_text("1\n00:00:01,250 --> 00:00:02,500\n孩子問：檔案在哪？\n", encoding="utf-8")
        a.ingest("L001", srt)
        raw = a.read(a.ROOT / "lessons/L001/private/transcript/raw.json")
        self.assertEqual(raw["segments"][0]["start"], 1.25)
        self.assertEqual(raw["segments"][0]["id"], "seg-00001")
        with self.assertRaises(FileExistsError): a.ingest("L001", srt)

    def test_bad_timing_rejected(self):
        for start, end in [(2, 1), (-1, 1), (0, float("nan"))]:
            with self.assertRaises(ValueError):
                a.validate_segments({"segments": [{"start": start, "end": end, "text": "例"}]})

    def test_new_episode_does_not_pass_as_finished(self):
        a.init_lesson(ORIGINAL / "curriculum/catalog.json", "L001")
        a.new_episode("L001", "l001-mac-workstation")
        ep = a.ROOT / "episodes/academy/l001-mac-workstation"
        with self.assertRaisesRegex(ValueError, "placeholders"): a.validate_episode(ep)
        self.assertFalse((ep / "audio/slide_01.mp3").exists())

    def test_fingerprint_detects_modified_delivery(self):
        ep = a.ROOT / "episode"
        (ep / "output").mkdir(parents=True)
        p = ep / "output/master.mp4"
        p.write_bytes(b"first")
        previous = a.fingerprint(ep)
        p.write_bytes(b"second")
        self.assertNotEqual(previous, a.fingerprint(ep))

    def test_l003_audio_hashes_match_real_files(self):
        a.media_check(ORIGINAL / "episodes/academy/l003-keyboard-ninja")

    def test_scaffold_endpoints_without_ep10_and_no_old_lesson_content(self):
        for lesson_id in ("L004", "L192"):
            a.init_lesson(ORIGINAL / "curriculum/catalog.json", lesson_id)
            slug = lesson_id.lower() + "-test"
            a.new_episode(lesson_id, slug)
            ep = a.ROOT / "episodes/academy" / slug
            manifest = a.read(ep / "production/manifest.json")
            self.assertEqual(manifest["lessonIds"], [lesson_id])
            self.assertEqual(manifest["publicationMode"], "manual-user-upload")
            self.assertFalse(manifest["autoPublish"])
            self.assertEqual(len(a.read(ep / "production/narration.json")), 12)
            self.assertFalse((ep / "production/timing.json").exists())
            with self.assertRaises(FileExistsError): a.new_episode(lesson_id, slug)
            with self.assertRaisesRegex(ValueError, "placeholders"): a.validate_episode(ep)

    def test_wrong_lesson_slug_and_out_of_range_rejected_before_writes(self):
        for lesson_id, slug in [("L004", "l003-test"), ("L193", "l193-test"), ("L004", "../outside")]:
            with self.assertRaises(ValueError): a.new_episode(lesson_id, slug)
        self.assertFalse((a.ROOT / "episodes").exists())

    def test_catalog_has_exactly_192_lessons_and_576_search_entries(self):
        lessons = a.read(ORIGINAL / "curriculum/catalog.json")["lessons"]
        self.assertEqual([x["lessonId"] for x in lessons], [f"L{i:03d}" for i in range(1, 193)])
        self.assertTrue(all(len(x["resources"]) == 3 for x in lessons))

    def test_l003_is_valid_but_missing_template_edit_is_not_ready(self):
        import shutil
        source = ORIGINAL / "episodes/academy/l003-keyboard-ninja"
        ep = a.ROOT / "test-episode"
        shutil.copytree(source / "production", ep / "production")
        a.validate_episode(ep)
        edits = a.read(ep / "production/template-text.json")
        edits[0]["new"] = "待編寫"
        a.write(ep / "production/template-text.json", edits)
        with self.assertRaisesRegex(ValueError, "placeholders"): a.validate_episode(ep)


if __name__ == "__main__":
    unittest.main()
