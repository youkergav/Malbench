from sys import exit
from textwrap import fill
from colorama import Fore
from malbench.printer import Printer
from malbench.args import ArgParser
from malbench.malware import MalwareLauncher, MalwareMetrics


def main():
    """
    Main entry point for application.

    Main function that initializes a ParsedArgs object to parse command-line arguments
    using argparse and extract relevant arguments for use in the Malbench project. If
    the --no-banner flag is not used, it prints the Malbench banner. It then prints
    the parsed arguments.
    """

    try:
        # Parse arguments and load tool.
        args = ArgParser.parse()

        if args["banner"]:
            Printer.banner()

        if args["warning"]:
            _confirm_continue()

        # Start the malware samples.
        print("Loading malware...")
        malwares = []

        for malware_path in args["malware_filepaths"]:
            malwares.append(MalwareLauncher(malware_path, timeout=args["timeout"]))

        # Monitor the malware processes for prevention.
        print("Monitoring malware for detection...")
        for malware in malwares:
            malware.run()

            if malware.detected:
                Printer.good(malware.name)
            else:
                Printer.bad(malware.name)

        # Calculate metrics and print results.
        results = MalwareMetrics(malwares)
        detection_rate = results.detection_rate()

        if detection_rate == 1:
            print(f"\nDone. Detection rate: {Fore.GREEN}100%{Fore.RESET}.")
            print("No malware went undetected!\n")
        else:
            undetected_malware = results.failed_samples()

            print(f"\nDone. Detection rate: {Fore.RED}{detection_rate:.0%}{Fore.RESET} ({len(undetected_malware)} failed):")

            for malware in undetected_malware:
                print(malware.name)
            print("")
    except KeyboardInterrupt:
        print("User cancelled. We were so close to greatness...")
    except Exception as e:
        if args["dev"]:
            raise e
        else:
            print(f"{Fore.RED}error{Fore.RESET}: an unexpected error has occurred")


def _confirm_continue() -> None:
    """Function to confirm an action and return true or false."""

    message = (f"{Fore.YELLOW}WARNING{Fore.RESET}: Malbench is designed to run malicious "
               "code that can harm your computer. Malbench should only be run on secure and isolated "
               "environments by users who know what they are doing. Do NOT run Malbench on a computer "
               "or network that contains sensitive information or data that you are not willing to lose "
               "or become compromised. By continuing, you acknowledge and understand the risks of using "
               "this software; and assume full responsibility for any damages that may result from running "
               "Malbench.")

    print(fill(message, width=80))

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
