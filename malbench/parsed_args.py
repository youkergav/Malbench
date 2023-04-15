import os
import argparse
from typing import List, Dict


class ParsedArgs():
    """
    Parses command line arguments.

    Parses the command-line arguments using argparse and extracts relevant
    arguments for use in the Malbench project.
    """

    @staticmethod
    def parse() -> Dict:
        """
        Method to parse arguments.

        Initializes a ParsedArgs object by parsing command-line arguments
        using argparse. Extracts and stores relevant arguments for use in the
         Malbench project.
        """

        parser = argparse.ArgumentParser()

        parser.add_argument("path", type=ParsedArgs._get_path, help="file or folder path to the malware samples")
        parser.add_argument("-v", "--verbose", action="store_true", help="prints additional info")
        parser.add_argument("-t", "--timeout", type=int, default=2, help="malware TTL before failing (2 default)")
        parser.add_argument("--no-banner", action="store_true", help="hides the banner logo")

        args = parser.parse_args()

        return {
            "malware_samples": ParsedArgs._get_malware_samples(args.path),
            "timeout": args.timeout,
            "banner": not args.no_banner,
            "verbose": args.verbose
        }

    @staticmethod
    def _get_path(path: str) -> str:
        """Returns the absolute path of the value provided. Errors if does not exist."""

        path = os.path.abspath(path)

        if not os.path.exists(path):
            raise FileNotFoundError(f"No file or folder found at '{path}'")

        return path

    @staticmethod
    def _get_malware_samples(path: str) -> List[str]:
        """Gets a list of malware samples by checking if the file(s) are executable."""

        files = []

        if os.path.isfile(path):
            if os.access(path, os.X_OK):
                files.append(path)
            else:
                raise argparse.ArgumentTypeError(f"'{path}' is not an executable file")
        else:
            for file in os.listdir(path):
                file = os.path.join(path, file)

                if os.access(file, os.X_OK):
                    files.append(file)

        if not len(files):
            raise argparse.ArgumentTypeError(f"no executable files found at '{path}'")

        return files
