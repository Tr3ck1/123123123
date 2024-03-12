import tkinter as tk

def display_text():
    text = entry.get()
    print(text)

root = tk.Tk()
root.title("Text Display App")

entry = tk.Entry(root, width=30)
entry.pack(pady=10)

button = tk.Button(root, text="Display Text", command=display_text)
button.pack(pady=10)

root.mainloop()

import tkinter as tk

def change_text():
    label.config(text="Text has been changed!")

root = tk.Tk()
root.title("Text Change App")

label = tk.Label(root, text="Original Text")
label.pack(pady=10)

button = tk.Button(root, text="Change Text", command=change_text)
button.pack(pady=10)

root.mainloop()

import tkinter as tk
from tkinter import colorchooser

def choose_color():
    color = colorchooser.askcolor()
    hex_value = color[1]  # Get the HEX value from the color tuple
    color_label.config(text=f"Selected Color: {hex_value}")

root = tk.Tk()
root.title("Color Picker App")

color_button = tk.Button(root, text="Choose Color", command=choose_color)
color_button.pack(pady=10)

color_label = tk.Label(root, text="Selected Color: ")
color_label.pack(pady=10)

root.mainloop()
