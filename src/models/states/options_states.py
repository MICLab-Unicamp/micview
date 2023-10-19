import tkinter as tk
from hooks.states.optional_states import *

class optional_states_class:
        def __init__(self, master):
                self.__image_is_square = tk.BooleanVar(master, False, name="image_is_square")
                self.__image_is_square.trace('w', image_is_square_hook)

        def get_image_is_square(self):
                return self.__image_is_square.get()
        
        def set_image_is_square(self, value):
                assert type(value) is bool
                self.__image_is_square.set(value)