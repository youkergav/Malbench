from sys import exit
from malbench.message import Message
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
        message = Message(args["color"])

        if args["banner"]:
            print(message.banner())

        if args["warning"]:
            print(message.disclaimer())
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
                print(message.good(malware.name))
            else:
                print(message.bad(malware.name))

        # Calculate metrics and print results.
        results = MalwareMetrics(malwares)
        detection_rate = results.detection_rate()

        if detection_rate == 1:
            print(f"\nDone. Detection rate:  {message.green('100%')}.")
            print("No malware went undetected!\n")
        else:
            detection_rate_percent = f"{round(detection_rate * 100)}%"
            undetected_malware = results.failed_samples()

            print(f"\nDone. Detection rate: { message.red(detection_rate_percent)} ({len(undetected_malware)} failed):")

            for malware in undetected_malware:
                print(malware.name)
            print("")
    except KeyboardInterrupt:
        print("User :cancelled. We were so close to greatness...")
    except Exception as e:
        if args["dev"]:
            raise e
        else:
            print(f"{message.red('error')}: an unexpected error has occurred")


def _confirm_continue() -> None:
    """Function to confirm an action and return true or false."""

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
