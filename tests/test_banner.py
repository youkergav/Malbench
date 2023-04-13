from io import StringIO
from colorama import Fore
from malbench.banner import Banner
from unittest import TestCase
from unittest.mock import patch


class TestBanner(TestCase):
    @patch("sys.stdout", new_callable=StringIO)
    def test_print(self, mock_stdout):
        Banner.print()  # Run the banner print method.

        # Extract the results.
        results = mock_stdout.getvalue().strip().splitlines()
        results_banner = "\n".join(results[:-1])
        results_subtitle = results[-1]

        # Define expected results.
        with open("data/banner.txt", "r") as f:
            expected_banner = f.read().format(COLOR=Fore.CYAN, RESET=Fore.RESET)

        expected_subtitle = r"  .* v[1-9]\.[0-9]\.[0-9]"

        # Perform assertions.
        self.assertEqual(results_banner, expected_banner)
        self.assertRegex(results_subtitle, expected_subtitle)
