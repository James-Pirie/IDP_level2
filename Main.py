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
start_menu_buttons = ["Back", "Start Game"]
game_buttons = ["Close Game"]
root_buttons = ["Exit", "Next"]
game_over_buttons = ["Exit", "Next"]
total_amount_of_points = 0
minutes = 0
seconds = 0
final_time = 0
compiled_sentence = ""
counter_var = 0
time_list = []
total_amount_of_letters = 0
total_amount_of_sentences = 0
total_amount_of_words = 0
values = {}
final_formatted_time = ""
total_amount_of_correct_words = 0
total_amount_of_correct_letters = 0
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
    global total_amount_of_points, accuracy_per_word, accuracy_per_letter
    global counter_var
    global final_time
    global sentence_type
    global seconds
    global total_amount_of_sentences
    global total_amount_of_letters
    global total_amount_of_words
    global total_amount_of_correct_words
    global total_amount_of_correct_letters
    global values
    global final_formatted_time
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

        if window_title == "Main Menu":
            print(total_amount_of_correct_words)
            print(total_amount_of_correct_letters)
            total_amount_of_sentences = 0
            total_amount_of_letters = 0
            total_amount_of_words = 0
            total_amount_of_correct_words = 0
            total_amount_of_points = 0
            total_amount_of_correct_letters = 0
            title_font = tk_font.Font(family="Lucida Grande", size=30)
            title_label = Label(text="Typing Game", font=title_font)
            title_label.grid(row=0, column=1, columnspan=8)

        # generate buttons appropriate for game window
        if window_title == "Game":
            # because this loops twice for the other templates to work make sure it doesn't duplicate
            if i == 1:
                # create the exit game button
                exit_game_button = Button(window, text="Exit Game", command=lambda: [window.destroy(),
                                                                                     generate_tk_window("Start Menu",
                                                                                                        resolution,
                                                                                                        start_menu_buttons)])
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
                    global total_amount_of_points
                    global compiled_sentence
                    global counter_var
                    global sentence_type
                    global time_list
                    global total_amount_of_letters
                    global total_amount_of_sentences
                    global total_amount_of_words
                    global total_amount_of_correct_words
                    global total_amount_of_correct_letters
                    global values
                    global final_formatted_time
                    # make sure that the sentence is being analysed before it is changed to the next one
                    if counter_var != 0:
                        # collect the user input
                        user_submission_string = user_entry.get("1.0", "end")
                        user_entry.delete('1.0', END)
                        values = Game_objects.check_answer(user_submission_string.strip(),
                                                               compiled_sentence.strip())
                        print(values)
                        point_gain = values["Score"]
                        total_amount_of_points += point_gain
                        total_amount_of_letters += values["Letters"]
                        total_amount_of_words += values["Words"]
                        total_amount_of_sentences += values["Sentences"]
                        total_amount_of_correct_words += values["Correct_words"]
                        total_amount_of_correct_letters += values["Correct_letters"]

                        print(f"you gained {point_gain} points and now have {total_amount_of_points} total points")
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
                    global final_formatted_time
                    # change text in label
                    formatted_time = str(datetime.timedelta(seconds=time))
                    final_formatted_time = formatted_time[2:7]
                    if time > 0 and list_of_windows_names[len(list_of_windows_names) - 1] == "Game":
                        # call countdown again after 1000ms (1s)
                        root.after(1000, countdown, time - 1)
                        time_label['text'] = f"{final_formatted_time}"
                    elif time <= 0:
                        window.destroy()
                        generate_tk_window("Game Over", resolution, game_over_buttons)


                countdown(final_time)
        else:
            # generate appropriate widgets for a window

            if buttons[i] == "Start Game":  # generate start game button
                start_game_button1 = ttk.Button(window, text=buttons[i],
                                                command=lambda: [current_open_window.destroy(),
                                                                 generate_tk_window("Game", resolution,
                                                                                    start_menu_buttons)])
                start_game_button1.grid(row=2, column=3, sticky="W")

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
                next_button1 = ttk.Button(window, text=buttons[i],
                                          command=lambda: [current_open_window.destroy(),
                                                           generate_tk_window("Start Menu", resolution, start_menu_buttons)])
                if window_title == "Game Over":
                    next_button1.configure(text="Play Again")

                next_button1.grid(row=2, column=10, padx=70, pady=70)

            if window_title == "Game Over":
                results_font = tk_font.Font(family="Lucida Grande", size=18)
                score_label = Label(font=results_font, text=f"You got {total_amount_of_points} points!")
                try:
                    words_per_minute = int(total_amount_of_words/(final_time/60))
                    letters_per_minute = int(total_amount_of_letters/(final_time/60))
                    sentence_per_minute = int(total_amount_of_sentences/(final_time/60))
                    accuracy_per_word = total_amount_of_correct_words/total_amount_of_words
                    accuracy_per_word_str = str(accuracy_per_word*100)
                    accuracy_per_letter = total_amount_of_correct_letters/total_amount_of_letters
                    accuracy_per_letter_str = str(accuracy_per_letter*100)
                except ZeroDivisionError:
                    words_per_minute = "0"
                    letters_per_minute = "0"
                    sentence_per_minute = "0"
                    accuracy_per_word_str = "0"
                    accuracy_per_letter_str = "0"

                if accuracy_per_word or accuracy_per_letter != 0:
                    print(f"letters: {total_amount_of_correct_letters}/{total_amount_of_letters}")
                    print(f"words: {total_amount_of_correct_words}/{total_amount_of_words}")
                    results_label1 = Label(text=f"Total letters: {total_amount_of_letters}\n\n"
                                            f"Letters per Minute: {letters_per_minute}\n\n "
                                            f"Total words: {total_amount_of_words}\n\n"
                                            f"Words per minutes: {words_per_minute}\n\n "
                                            f"Total Sentences: {total_amount_of_sentences}\n\n"
                                            f"Sentences per Minute: {sentence_per_minute}\n\n"
                                            f"Accuracy per word: {accuracy_per_word_str[0:5]}%\n\n"
                                            f"Accuracy per letter: {accuracy_per_letter_str[0:5]}%\n\n")
                else:
                    accuracy_per_word = values["Sim"]
                    results_label1 = Label(text=f"Total letters: {total_amount_of_letters}\n\n"
                                                f"Letters per Minute: {letters_per_minute}\n\n "
                                                f"Total words: {total_amount_of_words}\n\n"
                                                f"Words per minutes: {words_per_minute}\n\n "
                                                f"Total Sentences: {total_amount_of_sentences}\n\n"
                                                f"Sentences per Minute: {sentence_per_minute}\n\n"
                                                f"Accuracy per word: {accuracy_per_word_str[0:5]}%\n\n"
                                                f"Accuracy per letter: {accuracy_per_letter_str[0:5]}%\n\n")



                score_label.grid(column=1, row=0, columnspan=8)
                results_label1.grid(column=1, row=1, sticky="N", columnspan=8)

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
