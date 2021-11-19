import time
import subprocess

def run(filepath, args=[]):
    command = [filepath] + args

    try:
        process = subprocess.Popen(command, creationflags=subprocess.CREATE_NEW_PROCESS_GROUP | subprocess.CREATE_BREAKAWAY_FROM_JOB)

        return {
            "process": process,
            "timestamp": time.time(),
            "detected": None
        }
    except WindowsError as error:
        # Skip process monitoring if the file was blocked on startup for malware detection.
        if error.winerror == 225:
            return {
                "process": None,
                "timestamp": None,
                "detected": True
            }
        else:
            raise

def monitor(sample):
    return_code = sample["process"].poll()

    # Check for timeout
    if time.time() - sample["timestamp"] > 2:
        return False
    elif return_code != None:
        if return_code != 0:
            return True
        else:
            return False

    return None