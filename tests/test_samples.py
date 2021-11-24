import os
import subprocess
import time
import unittest
import malbench.samples as samples

class TestSamples(unittest.TestCase):
    def setUp(self):
        self.sample = samples.Sample(os.path.abspath("tests/data/samples/notepad.exe"), autorun=False)

    def test_get_name(self):
        self.assertEqual(self.sample.__get_name__(self.sample.filepath), "notepad.exe")

    def test_update_detected(self):
        # Test updating True
        self.assertTrue(self.sample.__update_detected__(True))
        self.assertEqual(self.sample.detected, True)

        # Test updating False
        self.assertFalse(self.sample.__update_detected__(False))
        self.assertEqual(self.sample.detected, False)

    def test_start(self):
        result = self.sample.start()
        self.assertIsInstance(result, subprocess.Popen)
        self.assertGreater(self.sample.process.pid, 0)
        self.assertNotEqual(self.sample.process.returncode, 0)

    def test_monitor(self):
        if self.sample.process:
            time.sleep(self.sample.timeout + 1)

            self.assertFalse(self.sample.monitor())
            self.assertFalse(self.sample.detected)