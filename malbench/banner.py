import toml
import random
from colorama import Fore


class Banner:
    """
    Static class to print Banner.

    This class provides methods for printing the Malbench banner including
    a tagline and version number.
    """

    @staticmethod
    def print() -> None:
        """
        Function to print banner.

        Prints the Malbench banner, including a randomly selected tagline and the current version number.
        """

        print(Banner._read_banner())
        print("  {:61} v{}\n".format(Banner._tag_line(), Banner._version()))

    @staticmethod
    def _read_banner() -> str:
        """Reads the banner for text file and colors it."""

        with open("data/banner.txt", "r") as f:
            banner = f.read().format(COLOR=Fore.CYAN, RESET=Fore.RESET)

        return banner

    @staticmethod
    def _version(filename: str = "./pyproject.toml") -> str:
        """Extracts the version for the project config file."""

        config = toml.load(filename)
        return config["tool"]["poetry"]["version"]

    @staticmethod
    def _tag_line() -> str:
        """Chooses a tag line at random."""

        lines = [
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
            "Disabling algorithms...",
            "Loading awesomeness [===============   ]",
            "Loading pixels...? [===               ]"
        ]

        return random.choice(lines)
