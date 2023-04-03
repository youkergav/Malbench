import toml
import random
from colorama import Fore

class Banner:
    @staticmethod
    def print() -> None:
        """
        Prints the Malbench banner, including a randomly selected tagline and the current version number.
        """
        
        print(f"{Fore.BLUE}mMMMMMMMMMMMMMM{Fore.RESET}          ll bb                                  hh")
        print(f"{Fore.BLUE}mM  MM.  MM.  M{Fore.RESET}          ll bb                                  hh")
        print(f"{Fore.BLUE}mM  MMM  MMM  M{Fore.RESET} .aaaaaa. ll bbbbbbb. .eeeeee. nnnnnnn. .cccccc. hhhhhhh.")
        print(f"{Fore.BLUE}mM  MMM  MMM  M{Fore.RESET} aa'  `aa ll bb'  `bb eeeeeeee nn'  `nn cc'  `\"\" hh'  `hh")
        print(f"{Fore.BLUE}mM  MMM  MMM  M{Fore.RESET} aa.  .aa ll bb.  .bb ee.  ... nn    nn cc.  ... hh    hh")
        print(f"{Fore.BLUE}mM  MMM  MMM  M{Fore.RESET} `aaaaaaa ll bbbbbbb' `eeeeee' nn    nn `cccccc' hh    hh")
        print(f"{Fore.BLUE}mMMMMMMMMMMMMMM{Fore.RESET}")
        print("  {:61} v{}\n".format(Banner._tag_line(), Banner._version()))

    @staticmethod
    def _version(filename: str = "./pyproject.toml") -> str:
        config = toml.load(filename)
        return config["tool"]["poetry"]["version"]
    
    @staticmethod
    def _tag_line() -> str:
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