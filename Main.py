# ====================================================== Imports =======================================================

from tkinter import *
import random
import datetime
import Sentence_generator
from Sentence_generator import sentence
import pyautogui
from tkinter import ttk, Tk
import tkinter.font as tk_font
import Game_objects

# ===================================================== Variables ======================================================

list_of_windows = []
list_of_windows_names = []
current_window = 0
place_holder = ["Back", "Start Game"]
game_buttons = ["Close Game"]
root_buttons = ["Exit", "Next"]
number_of_points = 0
minutes = 0
seconds = 0
final_time = 0
compiled_sentence = ""
counter_var = 0
time_list = []


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
    global number_of_points
    global counter_var
    global final_time
    global sentence_type
    global seconds
    """Initialize a Tk window with a certain title and a certain size"""
    # generate a window object and use the title provided in the parameters for the title
    window = Tk()
    window.title(window_title)
    window.geometry(dimensions)
    window.configure(bg="white")
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
            # because this loops twice for the other templates to work make sure it doesn't duplicate
            if i == 1:
                # create the exit game button
                exit_game_button = Button(window, text="Exit Game", command=lambda: [window.destroy(),
                                                                                     generate_tk_window("Start Menu",
                                                                                                        resolution,
                                                                                                        place_holder)])
                # exit game button parameters
                exit_game_button.grid(row=2, column=0, padx=70, pady=70)

                # set the font sizes for the label and entry
                default_font = tk_font.Font(family="Lucida Grande", size=30)

                # create the label to display the sentence the user will type
                sentence_to_type_label = Label(window, text=" ", font=default_font)
                sentence_to_type_label.grid(row=0, column=1, sticky="NSWE")

                user_entry = Text(window, font=default_font, height=1, width=25, bg="#F1F1F1", fg="black")
                user_entry.focus_set()
                user_entry.grid(row=1, column=1, sticky="W")

                # the function that will collect and analyse the user input once the enter key is pressed
                def press_on_enter_function(event):
                    global number_of_points
                    global compiled_sentence
                    global counter_var
                    global sentence_type
                    global time_list
                    # make sure that the sentence is being analysed before it is changed to the next one
                    if counter_var != 0:
                        # collect the user input
                        user_submission_string = user_entry.get("1.0", "end")
                        user_entry.delete('1.0', END)
                        point_gain = Game_objects.check_answer(user_submission_string.strip(),
                                                               compiled_sentence.strip())
                        number_of_points += point_gain
                        print(f"you gained {point_gain} points and now have {number_of_points} total points")
                    counter_var = 1
                    sentence_type = random.randint(0, len(Sentence_generator.type_of_sentence_structures) - 1)
                    sentence_object = sentence(sentence_type)
                    compiled_sentence = sentence_object.compile_sentence()
                    sentence_to_type_label.configure(text=compiled_sentence)

                press_on_enter_function(1)
                # the function that will be called when the user wants to submit
                time_label = Label(window, text="Error with the time.")
                time_label.grid(row=2, column=2, sticky="E")
                user_entry.bind("<Return>", press_on_enter_function)

                def countdown(time):
                    # change text in label
                    formatted_time = str(datetime.timedelta(seconds=time))
                    final_formatted_time = formatted_time[2:7]
                    if time > 0 and list_of_windows_names[len(list_of_windows_names) - 1] == "Game":
                        # call countdown again after 1000ms (1s)
                        root.after(1000, countdown, time - 1)
                        time_label['text'] = f"{final_formatted_time}"
                    elif time <= 0:
                        window.destroy()

                countdown(final_time)
        else:
            # generate appropriate widgets for a window
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

            if window_title == "Start Menu":
                settings_font = tk_font.Font(family="Lucida Grande", size=25)
                information_label = Label(text="Select a time to set the duration of the \n "
                                               "game as soon as the 'start game' button is \n "
                                               "pressed the game will begin.")
                information_label.grid(row=1, column=2, sticky="NE")
                option_label = Label(text="Time Settings", font=settings_font)
                option_label.grid(row=0, column=1, sticky="S")
                list_of_options = ["00:30", "01:00", "02:00", "05:00", "10:00", "30:00"]
                select_time = Listbox(height=len(list_of_options))
                final_time = 30

                def get_time():
                    global final_time
                    global minutes
                    global seconds
                    try:
                        time_str = select_time.get(ANCHOR)
                        time_str_list = time_str.split(":")
                        minutes = int((time_str_list[0]))
                        seconds = int((time_str_list[1]))
                        final_time = int((minutes * 60) + int(time_str_list[1]))
                    except ValueError:
                        print("You have selected no time")

                for y in list_of_options:
                    select_time.insert(END, y)
                select_time.grid(column=1, row=1, sticky="Nw")
                save_time_button = ttk.Button(text="Set Time", command=get_time)
                save_time_button.grid(row=1, column=2, sticky="S")

                if buttons[i] == "Start Game":  # generate start game button
                    start_game_button1 = ttk.Button(window, text=buttons[i],
                                                    command=lambda: [current_open_window.destroy(),
                                                                     generate_tk_window("Game", resolution,
                                                                                        place_holder)])
                    start_game_button1.grid(row=2, column=3, sticky="W")
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
root.mainloop()
