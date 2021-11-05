import os
import time
import datetime
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

def calc_detection_rate(samples):
    failed = 0
    total = 0

    for sample in samples.values():
        if sample["detected"] == True:
            failed += 1

        total += 1

    return (failed / total) * 100
        
def get_failed_samples(samples):
    failed = []

    for filepath, sample in samples.items():
        if sample["detected"] == False:
            failed.append(filepath)

    return failed

parser = argparse.ArgumentParser()
parser.add_argument("filepath", type=dir_path, help="filepath to the malware samples")
args = parser.parse_args()

print("Running sample malware...\n")
samples = {}
keys = []

# Start the malware samples.
for filename in os.listdir(args.filepath):
    filepath = os.path.join(args.filepath, filename)

    try:
        process = subprocess.Popen([filepath], creationflags=subprocess.CREATE_NEW_PROCESS_GROUP | subprocess.CREATE_BREAKAWAY_FROM_JOB)
        
        keys.append(filepath)
        samples[filepath] = {
            "process": process,
            "timestamp": time.time(),
            "detected": None
        }
    except WindowsError as error:
        # Skip process monitoring if the file was blocked on startup.
        if error.winerror == 225:
            print_good(filepath)

            samples[filepath] = {
                "process": None,
                "timestamp": None,
                "detected": True
            }

    time.sleep(.2)

# Monitor the malware processes for execution and prevention.
while len(keys) != 0:
    for key in keys:
        sample = samples[key]

        name = sample["process"].args[0]
        return_code = sample["process"].poll()

        if time.time() - sample["timestamp"] > 2:
            print_bad(name)
            sample["detected"] = False

            keys.remove(key)
        elif return_code != None:
            if return_code != 0:
                print_good(name)
                sample["detected"] = True
            else:
                print_bad(name)
                sample["detected"] = False
            
            keys.remove(key)

    time.sleep(.2)

detection_rate = calc_detection_rate(samples)

if detection_rate == 100:
    print("\nDone. Detection rate: \033[92m{}\033[00m".format(detection_rate))
else:
    failed = get_failed_samples(samples)

    print("\nDone. Detection rate: \033[91m{}%\033[00m ({} samples):".format(detection_rate, len(failed)))
    for filename in failed:
        print(filename)
    print("")
