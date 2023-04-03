import toml
import random
from colorama import Fore

class Banner:
    @staticmethod
    def print():
        print(f"{Fore.BLUE}mMMMMMMMMMMMMMM{Fore.RESET}          ll bb                                  hh")
        print(f"{Fore.BLUE}mM  MM.  MM.  M{Fore.RESET}          ll bb                                  hh")
        print(f"{Fore.BLUE}mM  MMM  MMM  M{Fore.RESET} .aaaaaa. ll bbbbbbb. .eeeeee. nnnnnnn. .cccccc. hhhhhhh.")
        print(f"{Fore.BLUE}mM  MMM  MMM  M{Fore.RESET} aa'  `aa ll bb'  `bb eeeeeeee nn'  `nn cc'  `\"\" hh'  `hh")
        print(f"{Fore.BLUE}mM  MMM  MMM  M{Fore.RESET} aa.  .aa ll bb.  .bb ee.  ... nn    nn cc.  ... hh    hh")
        print(f"{Fore.BLUE}mM  MMM  MMM  M{Fore.RESET} `aaaaaaa ll bbbbbbb' `eeeeee' nn    nn `cccccc' hh    hh")
        print(f"{Fore.BLUE}mMMMMMMMMMMMMMM{Fore.RESET}")
        print("{:60} v{}\n".format(Banner._tag_line(), Banner._version()))

    @staticmethod
    def _version():
        config = toml.load("pyproject.toml")
        return config["tool"]["poetry"]["version"]
    
    @staticmethod
    def _tag_line():
        lines = [
            "We're the reason antivirus software needs therapy.",
            "Stressing out your antivirus since day one.",
            "Testing the untestable, one virus at a time.",
            "Chaos unleashed, solutions found.",
            "Your AV will need a lemonade after this!",
            "Choose an option: Persuade [] Intimidate [X] Leave []",
            "We promise we won't break your computer... too much.",
            "Are you tired of your AV working? Try Malbench today!",
            "You encountered a virus!  Run [] Hide [] Fight []",
            "Test malware, smash AV.",
        ]

        return random.choice(lines)