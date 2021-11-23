import os
import time
import subprocess

class Sample:
    def __init__(self, filepath, args=[], autorun=True):
        self.filepath = filepath
        self.args = args
        self.name = self.__get_name__(self.filepath)
        self.timestamp = time.time()
        self.detected = None

        if autorun:
            self.process = self.start()

    def __get_name__(self, path):
        return os.path.basename(path)

    def __update_detected__(self, state):
        self.detected = state
        return state

    def start(self):
        command = [self.filepath] + self.args

        try:
            return subprocess.Popen(command, creationflags=subprocess.CREATE_NEW_PROCESS_GROUP | subprocess.CREATE_BREAKAWAY_FROM_JOB)
        except WindowsError as error:
            # Skip process monitoring if the file was blocked on startup for malware detection.
            if error.winerror == 225:
                self.detected = True
                return None
            else:
                raise

    def monitor(self):
        return_code = self.process.poll()

        if time.time() - self.timestamp > 2:
            return self.__update_detected__(False)
        elif return_code != None:
            if return_code != 0:
                return self.__update_detected__(True)
            else:
                return self.__update_detected__(False)

        return self.__update_detected__(None)
