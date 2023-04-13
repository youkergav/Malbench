import argparse
import stat
from unittest import TestCase
from unittest.mock import patch
from malbench.parsed_args import ParsedArgs


class TestParsedArgs(TestCase):
    @patch("os.path.exists", return_value=True)
    @patch("os.path.isfile", return_value=True)
    @patch("os.stat")
    @patch("os.listdir", return_value=["executable_file"])
    def test_parse(self, mock_listdir, mock_stat, mock_isfile, mock_exists):
        expected_malware_samples = ["/path/to/malware.exe"]
        expected_timeout = 5
        expected_banner = True
        expected_verbose = True

        mock_stat.return_value.st_mode = stat.S_IFREG | stat.S_IXUSR
        with patch("argparse.ArgumentParser.parse_args", return_value=argparse.Namespace(
            path="/path/to/malware.exe",
            timeout=5,
            no_banner=False,
            verbose=True,
        )):
            result = ParsedArgs.parse()

        self.assertEqual(result["malware_samples"], expected_malware_samples)
        self.assertEqual(result["timeout"], expected_timeout)
        self.assertEqual(result["banner"], expected_banner)
        self.assertEqual(result["verbose"], expected_verbose)
