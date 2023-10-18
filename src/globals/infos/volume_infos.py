import tkinter as tk
from hooks.infos.volume_infos import *

class volume_infos_class:
    def __init__(self, master):
        self.__num_of_channels = tk.IntVar(master, 1, name="num_of_channels")
        self.__num_of_channels.trace('w', num_of_channels_hook)

    def get_num_of_channels(self):
        return self.__num_of_channels.get()
    
    def set_num_of_channels(self, value):
        assert type(value) is int
        self.__num_of_channels.set(value)