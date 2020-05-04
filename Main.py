# ====================================================== Imports =======================================================

from tkinter import *
import random
import Sentence_generator
from Sentence_generator import sentence
import pyautogui
from tkinter import ttk, Tk

# ===================================================== Variables ======================================================

list_of_windows = []
list_of_windows_names = []
current_window = 0
place_holder = ["Back", "Start Game"]
game_buttons = ["Close Game"]
root_buttons = ["Exit", "Next"]

# ===================================================== Functions ======================================================


def generate_resolution_based_on_users_resolution():
    """Check the systems resolution to create an appropriately scaled program"""
    width = pyautogui.size().width / 2
    height = pyautogui.size().height / 2
    width_list = str(width).split(".")
    height_list = str(height).split(".")
    generated_resolution = f"{width_list[0]}x{height_list[0]}"
    return generated_resolution


def generate_tk_window(window_title, dimensions, buttons):
    """Initialize a Tk window with a certain title and a certain size"""
    # generate a window object and use the title provided in the parameters for the title
    window = Tk()
    window.title(window_title)
    window.geometry(dimensions)
    list_of_windows.append(window)  # record the  window object in a list to be used in future
    list_of_windows_names.append(window_title)  # record the window name in another list in the same location
    current_open_window: Tk = window
    # organize the window grid layout so buttons can be placed in correct locations
    window.grid_rowconfigure(0, weight=1)
    window.grid_columnconfigure(7, weight=1)
    # generate buttons based upon what type of window from my templates the window being generated is
    for i in range(len(buttons)):

        # generate buttons appropriate for game window
        if window_title == "Game":
            exit_game_button = Button(window, text="Exit Game", command=lambda: [window.destroy(),
                                                                                 generate_tk_window("Start Menu",
                                                                                 resolution,
                                                                                 place_holder)])
            exit_game_button.grid(row=2, column=0, padx=70, pady=70)
        else:
            # generate appropriate buttons for a menu window
            if buttons[i] == "Back":  # generate back button
                back_button = ttk.Button(window, text=buttons[i], command=lambda: [window.destroy(),
                                                                                   generate_tk_window("Main Menu",
                                                                                   resolution,
                                                                                   root_buttons)])
                back_button.grid(row=2, column=0, padx=70, pady=70)
            if buttons[i] == "Exit":  # generate back button
                back_button = ttk.Button(window, text=buttons[i], command=lambda: [window.destroy()])
                back_button.grid(row=2, column=0, padx=70, pady=70)
            if buttons[i] == "Next":  # generate next button
                # assign the generate window command to this button, so it opens a new window upon being pressed
                # also assign a destroy command to the current window, so no more than one window is open at once
                # note: window generated depends on parameters provided by type of button
                next_button1 = ttk.Button(window, text=buttons[i],
                                          command=lambda: [current_open_window.destroy(),
                                                           generate_tk_window("Start Menu", resolution, place_holder)])
                next_button1.grid(row=2, column=10, padx=70, pady=70)
            if buttons[i] == "Start Game":  # generate start game button
                # assign the generate window command to this button, so it opens a new window upon being pressed
                # also assign a destroy command to the current window, so no more than one window is open at once
                # note: window generated depends on parameters provided by type of button
                start_game_button1 = ttk.Button(window, text=buttons[i],
                                                command=lambda: [current_open_window.destroy(),
                                                                 generate_tk_window("Game", resolution, place_holder)])
                start_game_button1.grid(row=2, column=10, padx=70, pady=70)
    return window


# ======================================================== Code ========================================================

# set a variable to a custom resolution size to be used as the size for the windows of the program
resolution = generate_resolution_based_on_users_resolution()

# randomly select the sentence type from the list of sentence types in types of sentences list in Sentence_generator.py
sentence_type = random.randint(0, len(Sentence_generator.type_of_sentence_structures) - 1)
final_sentence = sentence(sentence_type)
final_compiled_sentence = final_sentence.compile_sentence()

# ======================================================== Root Menu ===================================================

root = generate_tk_window("Main Menu", resolution, root_buttons)

# ======================================================== Game Menu ===================================================

root.mainloop()
