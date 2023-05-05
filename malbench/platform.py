import sys
import subprocess
from typing import Any

if sys.platform.startswith('win'):
    CREATE_NEW_PROCESS_GROUP: Any = subprocess.CREATE_NEW_PROCESS_GROUP
    CREATE_BREAKAWAY_FROM_JOB: Any = subprocess.CREATE_BREAKAWAY_FROM_JOB
else:
    CREATE_NEW_PROCESS_GROUP: Any = 0
    CREATE_BREAKAWAY_FROM_JOB: Any = 0