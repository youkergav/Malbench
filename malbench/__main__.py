from malbench.banner import Banner
from malbench.parsed_args import ParsedArgs


def main():
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
