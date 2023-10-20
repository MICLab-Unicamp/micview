import tkinter as tk
from controllers.hooks.toolframe_states_hooks import *

class toolframe_states_class:
    def __init__(self, master):        
        self.__channel_select = tk.IntVar(master, 0, name="channel_select")
        self.__channel_select.trace('w', channel_select_hook)
        self.__selected_tool = tk.StringVar(master, value="none", name="selected_tool")
        self.__selected_tool.trace('w', selected_tool_hook)
        self.__tool_is_set = tk.BooleanVar(master, value=False, name="tool_is_set")
        self.__tool_is_set.trace('w', tool_is_set_hook)

    @property
    def channel_select(self):
        return self.__channel_select.get()

    @channel_select.setter
    def channel_select(self, value):
        assert type(value) is int
        self.__channel_select.set(value)

    @property
    def selected_tool(self):
        return self.__selected_tool.get()

    @selected_tool.setter
    def selected_tool(self, value):
        assert type(value) is str
        self.__selected_tool.set(value)

    @property
    def tool_is_set(self):
        return self.__tool_is_set.get()
    
    @tool_is_set.setter
    def tool_is_set(self, value):
        assert type(value) is bool
        self.__tool_is_set.set(value)