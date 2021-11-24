import os
import stat
import argparse

class Args:
    def __new__(cls, commands=[]):
        parser = argparse.ArgumentParser()

        parser.add_argument("path", type=Args.__get_path__, help="file or folder path to the malware samples")
        parser.add_argument("-v", "--verbose", action="store_true", help="prints additional info")
        parser.add_argument("-t", "--timeout", type=int, default=2, help="seconds malware should live before failing (2 default)")
        parser.add_argument("--no-banner", action="store_true", help="hides the banner logo")
        
        if commands:
            return parser.parse_args(commands)
            
        return parser.parse_args()

    def __is_executable__(path):
        if stat.S_IXUSR & os.stat(path)[stat.ST_MODE]:
            return True

        return False

    def __get_path__(path):
        files = []
        path = os.path.abspath(path)

        if os.path.isfile(path):
            if Args.__is_executable__(path):
                files.append(path)
            else:
                raise argparse.ArgumentTypeError(path + " is not executable")
        else:
            for file in os.listdir(path):
                file = os.path.join(path, file)

                if Args.__is_executable__(file):
                    files.append(file)

        if not len(files):
            raise argparse.ArgumentTypeError("no executable files found in " + path)

        return files
