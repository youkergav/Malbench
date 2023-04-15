import argparse
import stat
from unittest import TestCase
from unittest.mock import patch
from malbench.parsed_args import ParsedArgs


class TestParsedArgs(TestCase):
    @patch("os.path.exists", return_value=True)
    @patch("os.path.isfile", return_value=True)
    @patch("os.access", return_value=True)
    @patch("os.listdir", return_value=["executable_file"])
    def test_parse_file(self, mock_listdir, mock_stat, mock_isfile, mock_exists):
        # Mock run argparse and run our parse method.
        with patch("argparse.ArgumentParser.parse_args", return_value=argparse.Namespace(
            path="/path/to/malware",
            timeout=5,
            no_banner=False,
            verbose=True,
        )):
            result = ParsedArgs.parse()

        # Define expected results.
        expected_malware_samples = ["/path/to/malware"]
        expected_timeout = 5
        expected_banner = True
        expected_verbose = True

        # Perform assertions.
        self.assertEqual(result["malware_samples"], expected_malware_samples)
        self.assertEqual(result["timeout"], expected_timeout)
        self.assertEqual(result["banner"], expected_banner)
        self.assertEqual(result["verbose"], expected_verbose)

    @patch("os.path.exists", return_value=True)
    @patch("os.path.isfile", return_value=False)
    @patch("os.access", return_value=True)
    @patch("os.listdir", return_value=["malware1", "malware2"])
    def test_parse_folder(self, mock_listdir, mock_access, mock_isfile, mock_exists):
        # Mock run argparse and run our parse method.
        with patch("argparse.ArgumentParser.parse_args", return_value=argparse.Namespace(
            path="/path/to/",
            timeout=2,
            no_banner=False,
            verbose=False,
        )):
            result = ParsedArgs.parse()

        # Define expected results.
        expected_malware_samples = ["/path/to/malware1", "/path/to/malware2"]
        expected_timeout = 2
        expected_banner = True
        expected_verbose = False

        # Perform assertions.
        self.assertEqual(result["malware_samples"], expected_malware_samples)
        self.assertEqual(result["timeout"], expected_timeout)
        self.assertEqual(result["banner"], expected_banner)
        self.assertEqual(result["verbose"], expected_verbose)

    @patch("os.path.exists", return_value=True)
    @patch("os.path.isfile", return_value=False)
    @patch("os.access", return_value=False)
    @patch("os.listdir", return_value=["file1.txt", "file2.txt"])
    def test_parse_no_executable_files(self, mock_listdir, mock_access, mock_isfile, mock_exists):
        # Mock run argparse and run our parse method.
        with patch("argparse.ArgumentParser.parse_args", return_value=argparse.Namespace(
            path="/path/to/",
            timeout=2,
            no_banner=False,
            verbose=False,
        )):
            # Assert raise with argparse error - no executables found.
            with self.assertRaises(argparse.ArgumentTypeError):
                ParsedArgs.parse()

    @patch("os.path.exists", return_value=False)
    def test_parse_invalid_path(self, mock_exists):
        # Mock run argparse and run our parse method.
        with patch("argparse.ArgumentParser.parse_args", return_value=argparse.Namespace(
            path="/invalid/path",
            timeout=2,
            no_banner=False,
            verbose=False,
        )):
            # Assert raise with argparse error - invalid path.
            with self.assertRaises(FileNotFoundError):
                ParsedArgs.parse()
