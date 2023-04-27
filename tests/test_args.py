import os
import argparse
from unittest import TestCase
from unittest.mock import patch
from malbench.args import ArgParser


class TestArgParser(TestCase):
    @patch("os.path.exists", return_value=True)
    @patch("os.path.isfile", return_value=True)
    @patch("os.access", return_value=True)
    @patch("os.listdir", return_value=["executable_file"])
    @patch("malbench.args.ArgParser._is_executable", return_value=True)
    @patch("dotenv.load_dotenv", return_value=None)
    def test_parse_file(self, mock_load_dotenv, mock_exec, mock_listdir, mock_stat, mock_isfile, mock_exists):
        # Mock run argparse and run our parse method.
        with patch("argparse.ArgumentParser.parse_args", return_value=argparse.Namespace(
            path="/path/to/malware",
            timeout=5,
            no_color=False,
            no_banner=False,
            no_warning=True,
            dev=True,
        )):
            result = ArgParser.parse()

        # Define expected results.
        expected_malware_filepaths = ["/path/to/malware"]
        expected_timeout = 5
        expected_color = True
        expected_banner = True
        expected_warning = False
        expected_dev = True

        # Perform assertions.
        self.assertEqual(result["malware_filepaths"], expected_malware_filepaths)
        self.assertEqual(result["timeout"], expected_timeout)
        self.assertEqual(result["color"], expected_banner)
        self.assertEqual(result["banner"], expected_banner)
        self.assertEqual(result["warning"], expected_warning)
        self.assertEqual(result["dev"], expected_dev)

    @patch("os.path.exists", return_value=True)
    @patch("os.path.isfile", side_effect=[False, True, True])
    @patch("os.listdir", return_value=["malware1", "malware2"])
    @patch("malbench.args.ArgParser._is_executable", return_value=True)
    @patch("dotenv.load_dotenv", return_value=None)
    def test_parse_folder(self, mock_load_dotenv, mock_exec, mock_listdir, mock_isfile, mock_exists):

        # Mock run argparse and run our parse method.
        with patch("argparse.ArgumentParser.parse_args", return_value=argparse.Namespace(
            path="/path/to/",
            timeout=2,
            no_color=False,
            no_banner=False,
            no_warning=True,
            dev=True,
        )):
            result = ArgParser.parse()

        # Define expected results.
        expected_malware_filepaths = ["/path/to/malware1", "/path/to/malware2"]
        expected_timeout = 2
        expected_color = True
        expected_banner = True
        expected_warning = False
        expected_dev = True

        # Perform assertions.
        self.assertEqual(result["malware_filepaths"], expected_malware_filepaths)
        self.assertEqual(result["timeout"], expected_timeout)
        self.assertEqual(result["color"], expected_banner)
        self.assertEqual(result["banner"], expected_banner)
        self.assertEqual(result["warning"], expected_warning)
        self.assertEqual(result["dev"], expected_dev)

    @patch("os.path.exists", return_value=True)
    @patch("os.path.isfile", return_value=False)
    @patch("os.access", return_value=False)
    @patch("os.listdir", return_value=["file1.txt", "file2.txt"])
    @patch("dotenv.load_dotenv", return_value=None)
    def test_parse_no_executable_files(self, mock_load_dotenv, mock_listdir, mock_access, mock_isfile, mock_exists):
        # Mock run argparse and run our parse method.
        with patch("argparse.ArgumentParser.parse_args", return_value=argparse.Namespace(
            path="/path/to/",
            timeout=2,
            no_banner=False,
            no_warning=True,
            dev=True,
        )):
            # Assert raise with argparse error - no executables found.
            with self.assertRaises(SystemExit) as cm:
                ArgParser.parse()

            self.assertEqual(cm.exception.code, 1)

    @patch("os.path.exists", return_value=False)
    @patch("os.listdir", return_value=[])
    @patch("dotenv.load_dotenv", return_value=None)
    def test_parse_invalid_path(self, mock_load_dotenv, mock_listdir, mock_exists):
        # Mock run argparse and run our parse method.
        with patch("argparse.ArgumentParser.parse_args", return_value=argparse.Namespace(
            path="/invalid/path",
            timeout=2,
            no_banner=False,
            no_warning=True,
            dev=True,
        )):
            # Assert raise with argparse error - invalid path.
            with self.assertRaises(SystemExit) as cm:
                ArgParser.parse()

            self.assertEqual(cm.exception.code, 1)
