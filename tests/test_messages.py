import unittest
from unittest.mock import patch
import malbench.messages as messages

class TestMessages(unittest.TestCase):
    def setUp(self):
        self.message = messages.Message()

    def test_red(self):
        self.assertEqual(self.message.red("test"), "\033[91mtest\033[00m")

    def test_green(self):
        self.assertEqual(self.message.green("test"), "\033[92mtest\033[00m")

    def test_blue(self):
        self.assertEqual(self.message.blue("test"), "\033[94mtest\033[00m")

    @patch("builtins.print")
    def test_good(self, mock_print):
        self.message.good("good message")
        mock_print.assert_called_once_with("[\x1b[92m+\x1b[00m] good message")

    @patch("builtins.print")
    def test_bad(self, mock_print):
        self.message.bad("bad message")
        mock_print.assert_called_once_with("[\x1b[91m-\x1b[00m] bad message")

    @patch("builtins.print")
    def test_info(self, mock_print):
        # Test without verbose attribute off.
        self.message.info("info message")
        mock_print.asset_not_called()

        # Test without verbose attribute on.
        self.message.verbose = True
        self.message.info("info message")
        mock_print.assert_called_once_with("[\x1b[94m*\x1b[00m] info message")

    @patch("builtins.print")
    def test_banner(self, mock_print):
        self.message.banner("1.0.0")
        mock_print.assert_called_with("                                                          v1.0.0\n")