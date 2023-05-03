import textwrap
from colorama import Fore
from malbench.message import Message
from unittest import TestCase
from unittest.mock import patch


class TestMessage(TestCase):
    @classmethod
    def setUpClass(cls):
        cls.message = Message()

    def test_banner(self):
        banner = self.message.banner()  # Run the banner method.

        # Extract the results.
        results = banner[:-1].split("\n")
        results_banner = "\n".join(results[:-1])
        results_subtitle = results[-1]

        # Define expected results.
        with open("malbench/data/banner.txt", "r") as f:
            expected_banner = f.read().format(COLOR=Fore.BLUE, RESET=Fore.RESET)

        expected_subtitle = r"  .* v[0-9]\.[0-9]\.[0-9]"

        # Perform assertions.
        self.assertEqual(results_banner, expected_banner)
        self.assertRegex(results_subtitle, expected_subtitle)

    def test_disclaimer(self):
        result = self.message.disclaimer()  # Run the disclaimer method.

        # Define expected results.
        with open("malbench/data/disclaimer.txt", "r") as f:
            expected = textwrap.fill(f.read().format(COLOR=Fore.YELLOW, RESET=Fore.RESET), width=80)

        self.assertEqual(result, expected)  # Perform assertion.

    def test_good(self):
        result = self.message.good("The good ending")  # Run the good method.
        expected = f"{Fore.GREEN}[+]{Fore.RESET} The good ending"  # Define expected result.

        self.assertEqual(result, expected)  # Perform assertions.

    def test_bad(self):
        result = self.message.bad("The bad ending")  # Run the bad method.
        expected = f"{Fore.RED}[-]{Fore.RESET} The bad ending"  # Define expected result.

        self.assertEqual(result, expected)  # Perform assertions.

    def test_red(self):
        result = self.message.red("A red message")  # Run the red method.
        expected = f"{Fore.RED}A red message{Fore.RESET}"  # Define expected result.

        self.assertEqual(result, expected)  # Perform assertions.

    def test_yellow(self):
        result = self.message.yellow("A yellow message")  # Run the yellow method.
        expected = f"{Fore.YELLOW}A yellow message{Fore.RESET}"  # Define expected result.

        self.assertEqual(result, expected)  # Perform assertions.

    def test_green(self):
        result = self.message.green("A green message")  # Run the green method.
        expected = f"{Fore.GREEN}A green message{Fore.RESET}"  # Define expected result.

        self.assertEqual(result, expected)  # Perform assertions.

    def test_blue(self):
        result = self.message.blue("A blue message")  # Run the blue method.
        expected = f"{Fore.BLUE}A blue message{Fore.RESET}"  # Define expected result.

        self.assertEqual(result, expected)  # Perform assertions.

    def test_no_color(self):
        message = Message(color=False)

        result = message.green("A colorless message")  # Run the green method without color.
        expected = "A colorless message"  # Define expected result.

        self.assertEqual(result, expected)  # Perform assertions.
