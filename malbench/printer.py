import random
import holidays
import pkg_resources
from colorama import Fore
from datetime import date
from malbench.version import Version


class Printer:
    """
    A static class to print various types of messages and banners.

    This class provides methods for printing different types of messages and banners
    with different colors and formats. It includes a method to print the Malbench banner.

    Methods:
        banner() -> None:
            Prints the Malbench banner, including a randomly selected tagline and the current version number.

        good(message: str) -> None:
            Prints a message with a green [+] prefix.

        bad(message: str) -> None:
            Prints a message with a red [-] prefix.

        info(message: str) -> None:
            Prints a message with a blue [*] prefix.

    Example:
        >>> Printer.good(This is a good message!)

        [+] This is a good message!
    """

    @staticmethod
    def banner() -> None:
        """
        Function to print banner.

        Prints the Malbench banner, including a randomly selected tagline and the current version number.
        """

        print(Printer._read_banner())
        print("  {:61} v{}\n".format(Printer._gen_tag_line(), Version.version()))

    @staticmethod
    def good(message: str) -> None:
        """
        Prints a message with a green [+] prefix.

        Args:
            message (str): The message to be printed.
        """

        print(f"{Fore.GREEN}[+]{Fore.RESET} {message}")

    @staticmethod
    def bad(message: str) -> None:
        """
        Prints a message with a red [-] prefix.

        Args:
            message (str): The message to be printed.
        """

        print(f"{Fore.RED}[-]{Fore.RESET} {message}")

    @staticmethod
    def info(message: str) -> None:
        """
        Prints a message with a blue [*] prefix.

        Args:
            message (str): The message to be printed.
        """

        print(f"{Fore.BLUE}[*]{Fore.RESET} {message}")

    @staticmethod
    def _read_banner() -> str:
        """Reads the banner from a text file and colors it."""

        with pkg_resources.resource_stream("malbench", "../data/banner.txt") as f:
            return f.read().decode("utf-8").format(COLOR=Fore.CYAN, RESET=Fore.RESET)

    @staticmethod
    def _gen_tag_line() -> str:
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
