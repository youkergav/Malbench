from io import StringIO
from colorama import Fore
from malbench.printer import Printer
from unittest import TestCase
from unittest.mock import patch


class TestPrinter(TestCase):
    @patch("sys.stdout", new_callable=StringIO)
    def test_banner(self, mock_stdout):
        Printer.banner()  # Run the banner print method.

        # Extract the results.
        results = mock_stdout.getvalue().strip().splitlines()
        results_banner = "\n".join(results[:-1])
        results_subtitle = results[-1]

        # Define expected results.
        with open("data/banner.txt", "r") as f:
            expected_banner = f.read().format(COLOR=Fore.CYAN, RESET=Fore.RESET)

        expected_subtitle = r"  .* v[0-9]\.[0-9]\.[0-9]"

        # Perform assertions.
        self.assertEqual(results_banner, expected_banner)
        self.assertRegex(results_subtitle, expected_subtitle)

    @patch("sys.stdout", new_callable=StringIO)
    def test_good(self, mock_stdout):
        Printer.good("This is a good message!")  # Run the good print method.

        result = mock_stdout.getvalue()  # Get the results
        expected = f"{Fore.GREEN}[+]{Fore.RESET} This is a good message!\n"  # Define expected result.

        self.assertEqual(result, expected)  # Perform assertion.

    @patch("sys.stdout", new_callable=StringIO)
    def test_bad(self, mock_stdout):
        Printer.bad("This is a bad message!")  # Run the bad print method.

        result = mock_stdout.getvalue()  # Get the results
        expected = f"{Fore.RED}[-]{Fore.RESET} This is a bad message!\n"  # Define expected result.

        self.assertEqual(result, expected)  # Perform assertion.

    @patch("sys.stdout", new_callable=StringIO)
    def test_info(self, mock_stdout):
        Printer.info("This is a info message!")  # Run the info print method.

        result = mock_stdout.getvalue()  # Get the results
        expected = f"{Fore.BLUE}[*]{Fore.RESET} This is a info message!\n"  # Define expected result.

        self.assertEqual(result, expected)  # Perform assertion.
