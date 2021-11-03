import os
import time
import argparse
import subprocess

def print_good(message):
    print("[\033[92m+\033[00m] " + message)

def print_bad(message):
    print("[\033[91m!\033[00m] " + message)

def dir_path(path):
    if os.path.isdir(path):
        return os.path.abspath(path)
    else:
        raise argparse.ArgumentTypeError(path + " is not a valid path")

results = {
    "passed": [],
    "failed": []
}

parser = argparse.ArgumentParser()
parser.add_argument("filepath", type=dir_path, help="filepath to the malware samples")
args = parser.parse_args()

print("Running sample malware...\n")
processes = []

# Start the malware samples.
for filename in os.listdir(args.filepath):
    process = subprocess.Popen([filename])
    processes.append(process)

    time.sleep(.2)

# Monitor the malware processes for execution and prevention.
while len(processes) != 0:
    for process in processes:
        name = process.args[0]
        return_code = process.poll()

        if return_code != None:
            if return_code != 0:
                print_good(name)
                results["passed"].append(name)
            else:
                print_bad(name)
                results["failed"].append(name)
            
            processes.remove(process)

    time.sleep(.2)

# Print the results.
if results["failed"]:
    print("\nDone. Found \033[91m{}\033[00m samples failed to detect:".format(len(results["failed"])))

    for result in results["failed"]:
        print(result)
    print("")
else:
    print("\nDone. All malware detected.")