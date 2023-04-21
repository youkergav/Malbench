import os
import stat
import argparse
from malbench.version import Version
from typing import List, Dict


class ArgParser():
    """
    Parses command line arguments.

    This class is responsible for parsing the command-line arguments using argparse and extracting relevant
    arguments for use in the Malbench project.

    Attributes:
        None

    Methods:
        parse(): Initializes a ParsedArgs object by parsing command-line arguments using argparse. Extracts and
        stores relevant arguments for use in the Malbench project.

    Example:
        >>> parsed_args = ParsedArgs.parse()
        >>> print(parsed_args)

        {'malware_filepaths': ['samples/malware1'], 'timeout': 2, 'banner': True, 'verbose': False, 'warning': True}
    """

    @staticmethod
    def parse() -> Dict:
        """
        Method to parse arguments.

        Parses the command line arguments using argparse and extracts and stores relevant
        arguments for use in the Malbench project.

        Returns:
            A dictionary containing the following keys:
            - malware_filepaths: A list of file paths to malware samples.
            - timeout: The amount of time in seconds to allow a malware sample to run before killing it.
            - banner: A boolean indicating whether to show the Malbench banner logo.
            - verbose: A boolean indicating whether to print additional information.
            - warning: A boolean indicating whether to prompt the user for confirmation before running Malbench.
        """

        parser = argparse.ArgumentParser()

        parser.add_argument("path", type=ArgParser._get_path, help="file or folder path to the malware samples")
        parser.add_argument("-v", "--version", action="version", version=f"Malbench {Version.version()}")
        parser.add_argument("-t", "--timeout", type=int, default=2, help="malware TTL before being marked as failure (2 default)")
        parser.add_argument("-nB", "--no-banner", action="store_true", help="hides the banner logo")
        parser.add_argument("-nW", "--no-warning", action="store_true", help="Does prompt for user confirmation before running")

        args = parser.parse_args()

        return {
            "malware_filepaths": ArgParser._get_malware_filepaths(args.path),
            "timeout": args.timeout,
            "banner": not args.no_banner,
            "warning": not args.no_warning
        }

    @staticmethod
    def _get_path(path: str) -> str:
        """Returns the absolute path of the value provided. Errors if does not exist."""

        path = os.path.abspath(path)

        if not os.path.exists(path):
            raise FileNotFoundError(f"No file or folder found at '{path}'")

        return path

    @staticmethod
    def _is_executable(path: str) -> bool:
        """Determines if a path is executable or not."""

        return bool(stat.S_IXUSR & os.stat(path)[stat.ST_MODE])

    @staticmethod
    def _get_malware_filepaths(path: str) -> List[str]:
        """Gets a list of malware filepaths by checking if the file(s) are executable."""

        files = []

        if os.path.isfile(path):
            if ArgParser._is_executable(path):
                files.append(path)
            else:
                raise argparse.ArgumentTypeError(f"'{path}' is not an executable file")
        else:
            for file in os.listdir(path):
                filepath = os.path.join(path, file)

                if os.path.isfile(filepath) and ArgParser._is_executable(filepath):
                    files.append(filepath)

        if not len(files):
            raise argparse.ArgumentTypeError(f"no executable files found at '{path}'")

        return files
