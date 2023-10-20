import tkinter as tk
from controllers.hooks.optional_states_hooks import *

class options_states_class:
        def __init__(self, master):
                self.__image_is_square = tk.BooleanVar(master, False, name="image_is_square")
                self.__image_is_square.trace('w', image_is_square_hook)
                self.__mask_is_set = tk.BooleanVar(master, False, name="mask_is_set")
                self.__mask_is_set.trace('w', mask_is_set_hook)

        @property
        def image_is_square(self):
                return self.__image_is_square.get()
        
        @image_is_square.setter
        def image_is_square(self, value: bool):
                assert type(value) is bool
                self.__image_is_square.set(value)

        @property
        def mask_is_set(self):
                return self.__mask_is_set
        
        @mask_is_set.setter
        def mask_is_set(self, value: bool):
                self.__mask_is_set.set(value)