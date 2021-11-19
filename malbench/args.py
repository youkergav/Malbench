import os
import stat
import argparse

def __is_executable__(path):
    return stat.S_IXUSR & os.stat(path)[stat.ST_MODE]

def __get_path__(path):
    files = []
    path = os.path.abspath(path)

    if os.path.isfile(path):
        if __is_executable__(path):
            files.append(path)
        else:
            raise argparse.ArgumentTypeError(path + " is not executable")
    else:
        for file in os.listdir(path):
            file = os.path.join(path, file)

            if __is_executable__(file):
                files.append(file)

    if not len(files):
        raise argparse.ArgumentTypeError("no executable files found in " + path)

    return files

def get_args():
    parser = argparse.ArgumentParser()

    parser.add_argument("path", type=__get_path__, help="file or folder path to the malware samples")
    parser.add_argument("-v", "--verbose", action="store_true", help="prints additional info")
    parser.add_argument("--no-banner", action="store_true", help="hides the banner logo")
    
    return parser.parse_args()