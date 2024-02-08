##
# @brief: This file contains the class that holds the optional states of the application.
#

# Imports
import tkinter as tk
from micview.controllers.hooks.optional_states_hooks import imageIsSquareHook, maskIsSetHook

# Classes
class OptionsStatesClass:
        """!
        @brief: This class holds the optional states of the application.
        """
        def __init__(self, master: tk.Tk) -> None:
                """!
                @brief: The constructor of the class.
                @param: master: tk.Tk - The master window of the application.
                """
                super().__init__()
                self.__image_is_square = tk.BooleanVar(master=master, value=False, name="image_is_square")
                self.__image_is_square.trace_add(mode="write", callback=imageIsSquareHook)
                self.__mask_is_set = tk.BooleanVar(master=master, value=False, name="mask_is_set")
                self.__mask_is_set.trace_add(mode="write", callback=maskIsSetHook)

        @property
        def image_is_square(self) -> bool:
            """!
                @brief: The getter method of the image_is_square property.
                @return: bool
            """
            return self.__image_is_square.get()
        
        @image_is_square.setter
        def image_is_square(self, value: bool) -> None:
                """!
                @brief: The setter method of the image_is_square property.
                @param: value: bool - The value to be set.
                @return: None
                """
                assert type(value) is bool
                self.__image_is_square.set(value=value)

        @property
        def mask_is_set(self) -> bool:
                """!
                @brief: The getter method of the mask_is_set property.
                @return: bool
                """
                return self.__mask_is_set.get()
        
        @mask_is_set.setter
        def mask_is_set(self, value: bool) -> None:
                """!
                @brief: The setter method of the mask_is_set property.
                @param: value: bool - The value to be set.
                @return: None
                """
                self.__mask_is_set.set(value=value)