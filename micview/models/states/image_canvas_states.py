##
# @brief: This file contains the class that holds the states of the image canvas.
#

# Imports
import tkinter as tk
from micview.controllers.hooks.image_canvas_hooks import actionOnChild, updateAllChilds

# Classes
class ImageCanvasStatesClass:
    """!
    @brief: This class holds the states of the image canvas.
    """
    def __init__(self, master: tk.Tk) -> None:
        """!
        @brief: The constructor of the class.
        @param: master: tk.Tk - The master window of the application.
        """
        super().__init__()
        self.__action_on_child = tk.IntVar(master=master, value=0, name="action_on_child")
        self.__action_on_child.trace_add(mode="write", callback=actionOnChild)
        self.__update_all_childs = tk.BooleanVar(master=master, value=False, name="update_all_childs")
        self.__update_all_childs.trace_add(mode="write", callback=updateAllChilds)

    @property
    def action_on_child(self) -> int:
        """!
        @brief: The getter method of the action_on_child property.
        @return: int
        """
        return self.__action_on_child.get()

    @action_on_child.setter
    def action_on_child(self, value: int) -> None:
        """!
        @brief: The setter method of the action_on_child property.
        @param: value: int - The value to be set.
        @return: None
        """
        self.__action_on_child.set(value=value)

    @property
    def update_all_childs(self) -> bool:
        """!
        @brief: The getter method of the update_all_childs property.
        @return: bool
        """
        return self.__update_all_childs.get()
    
    @update_all_childs.setter
    def update_all_childs(self, value: bool) -> None:
        """!
        @brief: The setter method of the update_all_childs property.
        @param: value: bool - The value to be set.
        @return: None
        """
        self.__update_all_childs.set(value=value)