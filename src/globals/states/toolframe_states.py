import tkinter as tk
from hooks.states.toolframe_states import *

class toolframe_states_class:
    def __init__(self, master):        
        self.__channel_select = tk.IntVar(master, -1, name="channel_select")
        self.__channel_select.trace('w', channel_select_hook)
        self.__selected_tool = tk.StringVar(master, value="none", name="selected_tool")
        self.__selected_tool.trace('w', selected_tool_hook)

    def get_channel_select(self):
        self.__channel_select.get()

    def set_channel_select(self, value):
        assert type(value) is int
        self.__channel_select.set(value)

    def get_selected_tool(self):
        self.__selected_tool.get()

    def set_selected_tool(self, value):
        assert type(value) is str
        self.__selected_tool.set(value)