from tkinter import *


def generate_tk_window(window_title, dimensions):
    """Initialize a Tk window with a certain title and a certain size"""
    window = Tk()
    window.title(window_title)
    window.geometry(dimensions)
    window.mainloop()
    return window


root = generate_tk_window("Main Menu", "800x600")
