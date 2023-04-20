import subprocess
import argparse


commands = {
    "typecheck": lambda: subprocess.run(["mypy", "malbench"]),
    "lint": lambda: subprocess.run(["flake8", "malbench"]),
    "tests": lambda: subprocess.run(["coverage", "run", "-m", "unittest", "discover", "-s", "tests"]),
    "coverage": lambda: subprocess.run(["coverage", "report"]),
    "docs": lambda: subprocess.run(["pdoc", "-o", "docs", "malbench"])
}

# Get program arguments
parser = argparse.ArgumentParser(prog="malbench-dev", description="used to run devops commands for malbench")
parser.add_argument("command", type=str, choices=commands.keys(), help="The dev tool to use")
args = parser.parse_args()

commands[args.command]()
