import unittest
import malbench.samples as samples
import malbench.metrics as metrics

class TestMetrics(unittest.TestCase):
    def setUp(self):
        malware = [
            samples.Sample("tests/data/samples/notepad.exe", autorun=False),
            samples.Sample("tests/data/samples/calc.exe", autorun=False),
        ]
        malware[0].detected = False
        malware[1].detected = True

        self.metrics = metrics.Metric(malware)
    
    def test_detection_rate(self):
        self.assertEqual(self.metrics.detection_rate(), 50)

    def test_failed_samples(self):
        self.assertListEqual(self.metrics.failed_samples(), ["notepad.exe"])
