import subprocess
import sys


def main():
    args = ["poetry", "run", "python", "-m", "malbench"] + sys.argv[1:]
    subprocess.run(args)
