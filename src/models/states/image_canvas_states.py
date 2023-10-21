import tkinter as tk
from src.controllers.hooks.image_canvas_hooks import *

class image_canvas_states_class:
    def __init__(self, master):
        self.__action_on_child = tk.IntVar(master, 0, name="action_on_child")
        self.__action_on_child.trace_add("write", action_on_child)

    @property
    def action_on_child(self):
        return self.__action_on_child.get()

    @action_on_child.setter
    def action_on_child(self, value: int):
        self.__action_on_child.set(value)