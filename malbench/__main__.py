from malbench.banner import Banner
from malbench.parsed_args import ParsedArgs


def main():
    """
    Main entry point for application.

    Main function that initializes a ParsedArgs object to parse command-line arguments
    using argparse and extract relevant arguments for use in the Malbench project. If
    the --no-banner flag is not used, it prints the Malbench banner. It then prints
    the parsed arguments.
    """

    args = ParsedArgs()

    if args.banner:
        Banner.print()

    print("Arguments are as follows:\n")
    print(f"Samples: {args.malware_samples}")
    print(f"Timeout: {args.timeout}")
    print(f"Banner: {args.banner}")
    print(f"Verbose: {args.verbose}")


if __name__ == "__main__":
    main()
