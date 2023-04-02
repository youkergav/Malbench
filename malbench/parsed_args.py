import os
import stat
import argparse
from typing import List

class ParsedArgs():
    def __init__(self) -> None:
        """
        Initializes a ParsedArgs object by parsing command-line arguments using argparse.
        Extracts and stores relevant arguments for use in the Malbench project.
        """

        parser = argparse.ArgumentParser()

        parser.add_argument("path", type=self._get_path, help="file or folder path to the malware samples")
        parser.add_argument("-v", "--verbose", action="store_true", help="prints additional info")
        parser.add_argument("-t", "--timeout", type=int, default=2, help="seconds malware should live before failing (2 default)")
        parser.add_argument("--no-banner", action="store_true", help="hides the banner logo")
            
        args = parser.parse_args()

        self.malware_samples = self._get_malware_samples(args.path)
        self.timeout = args.timeout
        self.banner = not args.no_banner
        self.verbose = args.verbose

    # Returns the absolute path of the value provided. Errors if does not exist.
    def _get_path(self, path: str) -> str:
        path = os.path.abspath(path)

        if not os.path.exists(path):
            raise FileNotFoundError(f"No file or folder found at '{path}'")
        
        return path

    # Checks if the provided path is executable.
    def _is_executable(self, path: str) -> bool:
        return stat.S_IXUSR & os.stat(path)[stat.ST_MODE]

    # Gets a list of malware samples by checking if the file(s) are executable.
    def _get_malware_samples(self, path: str) -> List[str]:
        files = []

        if os.path.isfile(path):
            if self._is_executable(path):
                files.append(path)
            else:
                raise argparse.ArgumentTypeError(f"'{path}' is not an executable file")
        else:
            for file in os.listdir(path):
                file = os.path.join(path, file)

                if self._is_executable(file):
                    files.append(file)

        if not len(files):
            raise argparse.ArgumentTypeError(f"no executable files found at '{path}'")

        return files