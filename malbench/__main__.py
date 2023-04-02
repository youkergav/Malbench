from malbench.parsed_args import ParsedArgs

def main():
    print("Welcome to the Malbench project!\n")

    args = ParsedArgs()

    print("Arguments are as follows:\n")
    print(f"Samples: {args.malware_samples}")
    print(f"Timeout: {args.timeout}")
    print(f"Banner: {args.banner}")
    print(f"Verbose: {args.verbose}")

if __name__ == "__main__":
    main()
