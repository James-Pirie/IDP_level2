from tkinter import *
import random
import Sentence_generator
from Sentence_generator import sentence
import pyautogui


def generate_resolution_based_on_users_resolution():
    """Check the systems resolution to create an appropriately scaled program"""
    width = pyautogui.size().width/2
    height = pyautogui.size().height/2
    width_list = str(width).split(".")
    height_list = str(height).split(".")
    generated_resolution = f"{width_list[0]}x{height_list[0]}"
    return generated_resolution


def generate_tk_window(window_title, dimensions):
    """Initialize a Tk window with a certain title and a certain size"""
    window = Tk()
    window.title(window_title)
    window.geometry(dimensions)
    window.mainloop()
    return window


resolution = generate_resolution_based_on_users_resolution()
# root = generate_tk_window("Main Menu", resolution)
# game_menu = generate_tk_window("Game Menu", resolution)
# game_screen = generate_tk_window("Game", resolution)
# score_screen = generate_tk_window("Your Score", resolution)

# randomly select the sentence type
sentence_type = random.randint(0, len(Sentence_generator.type_of_sentence_structures) - 1)
final_sentence = sentence(sentence_type)
final_compiled_sentence = final_sentence.compile_sentence()


