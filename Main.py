from tkinter import *
import random
import Sentence_generator
from Sentence_generator import sentence


def generate_tk_window(window_title, dimensions):
    """Initialize a Tk window with a certain title and a certain size"""
    window = Tk()
    window.title(window_title)
    window.geometry(dimensions)
    window.mainloop()
    return window


root = generate_tk_window("Main Menu", "800x600")

# randomly select the sentence type 
sentence_type = random.randint(0, len(Sentence_generator.type_of_sentence_structures)-1)
final_sentence = sentence(sentence_type)
final_compiled_sentence = final_sentence.compile_sentence()




