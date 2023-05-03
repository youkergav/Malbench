import random
import holidays
import textwrap
import pkg_resources
from colorama import Fore
from datetime import date
from malbench.version import Version


class Message():
    """
    Provides helper functions to print messages in the console.

    This class provides several helper functions to print messages in the console using colors and
    formatting.

    Attributes:
        color (bool): A boolean indicating whether to use colors in the console output.

    Methods:
        banner(): Prints the Malbench banner, including a randomly selected tagline and the current version number.
        disclaimer(): Reads the disclaimer from a text file and formats it.
        good(message: str) -> str: Prints a message with a green [+] prefix.
        bad(message: str) -> str: Prints a message with a red [-] prefix.
        red(message: str) -> str: Colors a string in red if color is enabled.
        yellow(message: str) -> str: Colors a string in yellow if color is enabled.
        green(message: str) -> str: Colors a string in green if color is enabled.
        blue(message: str) -> str: Colors a string in blue if color is enabled.
        _gen_tag_line() -> str: Chooses a tag line at random or based on holiday date.
    """

    def __init__(self, color: bool = True):
        """
        Initializes a new instance of the Message class.

        Args:
            color (bool): A boolean indicating whether to use colors in the console output.
        """

        self.color = color

    def banner(self) -> str:
        """
        Prints the Malbench banner, including a randomly selected tagline and the current version number.

        Returns:
            A string containing the banner.
        """

        with pkg_resources.resource_stream("malbench", "data/banner.txt") as f:
            banner = f.read().decode("utf-8").replace("\r", "").format(
                COLOR=Fore.BLUE if self.color else "",
                RESET=Fore.RESET if self.color else ""
            )

        return "{}\n  {:61} v{}\n".format(banner, self._gen_tag_line(), Version.version())

    def disclaimer(self) -> str:
        """
        Reads the disclaimer from a text file and formats it.

        Returns:
            A formatted string containing the disclaimer.
        """

        with pkg_resources.resource_stream("malbench", "data/disclaimer.txt") as f:
            message = f.read().decode("utf-8").replace("\r", "").format(
                COLOR=Fore.YELLOW if self.color else "",
                RESET=Fore.RESET if self.color else ""
            )

        return textwrap.fill(message, width=80)

    def good(self, message: str) -> str:
        """
        Prints a message with a green [+] prefix.

        Args:
            message (str): The message to be printed.

        Returns:
            A string containing the formatted message.
        """

        return f"{self.green('[+]')} {message}"

    def bad(self, message: str) -> str:
        """
        Prints a message with a red [-] prefix.

        Args:
            message (str): The message to be printed.

        Returns:
            A string containing the formatted message.
        """

        return f"{self.red('[-]')} {message}"

    def red(self, message: str) -> str:
        """
        Colors a string in red if color is enabled.

        Args:
            message (str): The message to be colored.

        Returns:
            A string containing the colored message.
        """

        message = str(message)

        if not self.color:
            return message

        return Fore.RED + message + Fore.RESET

    def yellow(self, message: str) -> str:
        """
        Colors a string in yellow if color is enabled.

        Args:
            message (str): The message to be colored.

        Returns:
            A string containing the colored message.
        """

        message = str(message)

        if not self.color:
            return message

        return Fore.YELLOW + message + Fore.RESET

    def green(self, message: str) -> str:
        """
        Colors a string in green if color is enabled.

        Args:
            message (str): The message to be colored.

        Returns:
            A string containing the colored message.
        """

        message = str(message)

        if not self.color:
            return message

        return Fore.GREEN + message + Fore.RESET

    def blue(self, message: str) -> str:
        """
        Colors a string in blue if color is enabled.

        Args:
            message (str): The message to be colored.

        Returns:
            A string containing the colored message.
        """

        message = str(message)

        if not self.color:
            return message

        return Fore.BLUE + message + Fore.RESET

    def _gen_tag_line(self) -> str:
        """Chooses a tag line at random or based on holiday date."""

        today = date.today()
        birthday = date(2023, 4, 1)

        if today.month == birthday.month and today.day == birthday.day:
            holiday = "birthday"
        else:
            holiday = holidays.US(years=today.year).get(today, "").lower()

        if "new year" in holiday:
            lines = [
                "Happy New Year!",
                "Time to start the New Year with some malware testing!",
                "Let's kick off the New Year with a bang, shall we?",
                "Ringing in the New Year with some malicious code!"
            ]
        elif "birthday" in holiday:
            age = today.year - birthday.year

            lines = [
                f"Happy Birthday to me! Can you believe I am {age} years old?",
                f"Hey! Todays my Birthday, I am {age} years old!",
                f"Celebrating with some cake and malware! I am {age} years old.",
                f":: Malbench turns {age} years old today ::"
            ]
        elif "independence day" in holiday:
            lines = [
                "Happy 4th of July!",
                "Celebrate freedom with some malware testing!",
                "Let's light up the sky... and your computer with some malware!",
                "Yeah fireworks are a thrill, but have you tried testing malware?"
            ]
        elif "thanksgiving" in holiday:
            lines = [
                "Happy Thanksgiving!",
                "Gobble gobble... with some malware testing on the side!",
                "Thankful for all the new malware to test!",
                "Why watch the parade when you can test malware instead?"
            ]
        elif "christmas" in holiday:
            lines = [
                "Merry Christmas!"
                "All we want for Christmas is some new malware to test!",
                "Tis the season for malware and mayhem!",
                "Deck the halls with bytes of malware!"
            ]
        else:
            lines = [
                "Would you like a black hat or white hat today?"
                "Good morning. The weather in Malibu is 72 degrees.",
                "Wake up Neo..."
                "We're the reason antivirus software needs therapy.",
                "Stressing out your antivirus since 1/1/1970.",
                "Testing the untestable, one virus at a time.",
                "Chaos unleashed, solutions found.",
                "Your AV will need a vacation after this one!",
                "Choose an option: Persuade [] Intimidate [X] Leave []",
                "We promise we won't break your computer... too much.",
                "Are you tired of your AV working? Try Malbench today!",
                "You encountered a virus!  Run [] Hide [] Fight []",
                "Test malware, smash AV.",
                "Time to go to plan B!",
                "Kiss your computer goodbye!",
                "\"I didn't run this program, did you run this program?!\"",
                "Disabling their algorithms...",
                "Loading awesomeness [===============   ]",
                "Loading pixels...? [===               ]"
            ]

        return random.choice(lines)
