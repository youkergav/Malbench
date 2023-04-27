import os
import stat
import dotenv
import argparse
from malbench.version import Version
from typing import List, Dict


class ArgPathNotFoundError(Exception):
    """Raised when the provided path is not executable."""

    def __init__(self, path):
        """Initializes an instance of ArgPathNotFoundError."""

        self.path = path

    def __str__(self):
        """Returns a string describing the error."""

        return f"error: no file or folder found at '{self.path}'"


class ArgPathNotExecutableError(Exception):
    """Raised when the provided path is not executable."""

    def __init__(self, path):
        """Initializes an instance of ArgPathNotExecutableError."""

        self.path = path

    def __str__(self):
        """Returns a string describing the error."""

        return f"error: no executable files found at '{self.path}'"


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

        parser.add_argument("path", type=ArgParser._get_path, help="file or folder path of malware executables")
        parser.add_argument("-v", "--version", action="version", version=f"Malbench {Version.version()}")
        parser.add_argument("-t", "--timeout", type=int, default=2, help="malware TTL before being marked as failure (2 default)")
        parser.add_argument("-nC", "--no-color", action="store_true", help="disables colored output")
        parser.add_argument("-nB", "--no-banner", action="store_true", help="hides the banner logo")
        parser.add_argument("-nW", "--no-warning", action="store_true", help="bypasses user confirmation before running")
        parser.add_argument("-d", "--dev", action="store_true", help="enables stack tracing")

        try:
            args = parser.parse_args()
            dotenv.load_dotenv()

            return {
                "malware_filepaths": ArgParser._get_malware_filepaths(args.path),
                "timeout": args.timeout,
                "color": not args.no_color,
                "banner": not args.no_banner,
                "warning": not args.no_warning,
                "dev": args.dev or os.getenv("MALBENCH_DEV", "false").lower() in ["true", "1"]
            }
        except (ArgPathNotFoundError, ArgPathNotExecutableError) as e:
            parser.print_usage()
            print(f"{parser.prog}: {e}")

            exit(1)

    @staticmethod
    def _get_path(path: str) -> str:
        """Returns the absolute path of the value provided. Errors if does not exist."""

        path = os.path.abspath(path)

        if not os.path.exists(path):
            raise ArgPathNotFoundError(path)

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
                raise ArgPathNotExecutableError(path)
        else:
            for file in os.listdir(path):
                filepath = os.path.join(path, file)

                if os.path.isfile(filepath) and ArgParser._is_executable(filepath):
                    files.append(filepath)

        if not len(files):
            raise ArgPathNotExecutableError(path)

        return files
