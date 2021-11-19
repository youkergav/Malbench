import os
import argparse

def __get_path__(path):
    if os.path.isdir(path):
        return os.path.abspath(path)
    else:
        raise argparse.ArgumentTypeError(path + " is not a valid path")

def get_args():
    parser = argparse.ArgumentParser()

    parser.add_argument("path", type=__get_path__, help="path to the malware samples")
    parser.add_argument("--no-banner", default=False, action="store_true", help="hides the banner logo")
    
    return parser.parse_args()