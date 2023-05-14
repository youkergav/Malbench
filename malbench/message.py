import random
import textwrap
import pkg_resources
from colorama import Fore
from datetime import date
from malbench.version import Version
from malbench.celebrations import Celebrations


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
        celebrations = Celebrations(today.year)

        if today in [celebrations.new_years_eve, celebrations.new_years_eve]:
            lines = [
                "Happy New Year!",
                "Time to start the New Year with some malware testing!",
                "Let's kick off the New Year with a bang, shall we?",
                "Ringing in the New Year with some malicious code!"
            ]
        elif today == celebrations.valentines_day:
            lines = [
                "Happy Valentine's Day!"
                "Who needs flowers and chocolates when you can test malware?",
                "Spread the love (and malware) this Valentine's Day!",
                "Sending virtual hugs and malware samples this Valentine's Day!"
            ]
        elif today == celebrations.st_patricks_day:
            lines = [
                "Happy St. Patrick's Day!"
                "Feeling lucky? Let's test some malware!",
                "Searching for a pot of gold... found malware samples instead!",
                "Don't forget to wear green while testing malware!"
            ]
        elif today == celebrations.birthday:
            age = today.year - celebrations.birthday.year

            lines = [
                f"Happy Birthday to me! Can you believe I am {age} years old?",
                f"Hey! Todays my Birthday, I am {age} years old!",
                f"Celebrating with some cake and malware! I am {age} years old.",
                f":: Malbench turns {age} years old today ::"
            ]
        elif today == celebrations.easter:
            lines = [
                "Happy Easter!",
                "Hatching plans to break your computer this Easter!",
                "Egg-cellent malware testing is our Easter tradition!",
                "Hop into the chaos this Easter!"
            ]
        elif today == celebrations.star_wars_day:
            lines = [
                "May the 4th be with you.",
                "May your computer be as secure as the Death Star!",
                "Testing antivirus from a galaxy far, far away...",
                "Test antivirus like a true Jedi Master!"
            ]
        elif today == celebrations.cinco_de_mayo:
            lines = [
                "Happy Cinco de Mayo!",
                "¡Feliz Cinco de Mayo! Celebrate with some spicy malware!",
                "Tacos, tequila, and malware, the perfect Cinco de Mayo!",
                "¡Salud! Here's to a malware-free Cinco de Mayo!",
            ]
        elif today == celebrations.mothers_day:
            lines = [
                "Happy Mother's Day!",
                "Wishing all the amazing moms a malware-free day!",
                "Thank you, Mom, for keeping me safe from malware.",
                "Malware testing with a sprinkle of mom's love and guidance!",
            ]
        elif today == celebrations.fathers_day:
            lines = [
                "Happy Father's Day!",
                "Wishing all the incredible dads a malware-free day!",
                "Thank you, Dad, for teaching me the importance of cybersecurity.",
                "Dads are the ultimate malware detectors. Happy Father's Day!",
            ]
        elif today == celebrations.labor_day:
            lines = [
                "Happy Labor Day!",
                "Labor Day: a time to relax, but not from malware!",
                "Wishing you a relaxing and malware-free Labor Day!",
                "Labor Day: a reminder of the importance of malware defense!"
            ]
        elif today == celebrations.independence_day:
            lines = [
                "Happy 4th of July!",
                "Celebrate freedom with some malware testing!",
                "Let's light up the sky... and your computer with some malware!",
                "Yeah fireworks are a thrill, but have you tried testing malware?"
            ]
        elif today == celebrations.halloween:
            lines = [
                "Happy Halloween!",
                "Beware of ghosts, ghouls, and malware! Happy Halloween!",
                "Things are about to get spooky on this malware ride!",
                "Unleashing monsters this Halloween night!",
            ]
        elif today == celebrations.thanksgiving:
            lines = [
                "Happy Thanksgiving!",
                "Gobble gobble... with some malware testing on the side!",
                "Thankful for all the new malware to test!",
                "Why watch the parade when you can test malware instead?"
            ]
        elif today in [celebrations.christmas_eve, celebrations.christmas]:
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
                "Loading pixels...? [===               ]",
                "I'm not saying my computer has malware, but it's acting like it.",
                "Why did the malware go to the doctor? It had a virus.",
                "Practice safe clicks, class!",
                "Malware: The gift that keeps on giving...to hackers.",
                "Why did the malware artist go to jail? A phishing addiction."

            ]

        return random.choice(lines)
