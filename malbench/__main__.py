import textwrap
from sys import exit
from colorama import Fore
from malbench.printer import Printer
from malbench.parsed_args import ParsedArgs
from malbench.malware_launcher import MalwareLauncher


def main():
    """
    Main entry point for application.

    Main function that initializes a ParsedArgs object to parse command-line arguments
    using argparse and extract relevant arguments for use in the Malbench project. If
    the --no-banner flag is not used, it prints the Malbench banner. It then prints
    the parsed arguments.
    """

    args = ParsedArgs.parse()

    if args["banner"]:
        Printer.banner()

    if args["warning"]:
        _confirm_continue()

    print("Running malware samples...")
    for malware_path in args["malware_filepaths"]:
        malware = MalwareLauncher(malware_path, timeout=args["timeout"])

        if malware.run():
            Printer.bad(malware.name)
        else:
            Printer.good(malware.name)

    print()


def _confirm_continue() -> None:
    """Function to confirm an action and return true or false."""

    message = (f"{Fore.YELLOW}WARNING{Fore.RESET}: Malbench is designed to run malicious "
               "code that can harm your computer. Malbench should only be run on secure and isolated "
               "environments. Do NOT run Malbench on a computer or network that contains sensitive "
               "information or data that you are not willing to lose or become compromised. By "
               "continuing, you acknowledge that you understand the risks and assume full responsibility "
               "for any damage that may result from running Malbench.")

    print(textwrap.fill(message, width=80))

    while True:
        default = "n"
        response = input("\nDo you want to continue? (y/N): ") or default

        if response.lower() in ["y", "yes"]:
            print("")
            return
        elif response.lower() in ["n", "no"]:
            print("Aborting. Until next time!\n")
            exit()
        else:
            print("Invalid response. Please enter 'Y' or 'N'.")


if __name__ == "__main__":
    main()
