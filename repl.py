import os
import sys

from signal import signal, SIGINT
from threading import Thread
from watchfiles import watch

SOURCE_DIR = "./src"

def watch_src_changes():
    for changes in watch(SOURCE_DIR):
        the_file = None
        for change in changes:
            if change[1].endswith(".py"):
                the_file = change[1]
                break
        if the_file:
            os.execl(sys.executable, "python", "-qi", the_file)

thread = Thread(target=watch_src_changes)
thread.daemon = True
thread.start()

def signal_handler(sig, frame):
    sys.exit(0)

signal(SIGINT, signal_handler)

# print(f"{sys.path=}")
print(f"{sys.argv=}")
