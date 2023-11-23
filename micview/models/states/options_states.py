import tkinter as tk
from micview.controllers.hooks.optional_states_hooks import image_is_square_hook, mask_is_set_hook

class options_states_class:
        def __init__(self, master: tk.Tk) -> None:
                super().__init__()
                self.__image_is_square = tk.BooleanVar(master=master, value=False, name="image_is_square")
                self.__image_is_square.trace_add(mode="write", callback=image_is_square_hook)
                self.__mask_is_set = tk.BooleanVar(master=master, value=False, name="mask_is_set")
                self.__mask_is_set.trace_add(mode="write", callback=mask_is_set_hook)

        @property
        def image_is_square(self) -> bool:
                return self.__image_is_square.get()
        
        @image_is_square.setter
        def image_is_square(self, value: bool) -> None:
                assert type(value) is bool
                self.__image_is_square.set(value=value)

        @property
        def mask_is_set(self) -> bool:
                return self.__mask_is_set.get()
        
        @mask_is_set.setter
        def mask_is_set(self, value: bool) -> None:
                self.__mask_is_set.set(value=value)