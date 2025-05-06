import os

POS_FILE = "log_position.txt"

def read_last_position():
    if os.path.exists(POS_FILE):
        with open(POS_FILE, "r") as f:
            try:
                return int(f.read().strip())
            except ValueError:
                return 0
    return 0

def write_current_position(pos):
    with open(POS_FILE, "w") as f:
        f.write(str(pos))