import tkinter as tk
from hooks.infos.toolframe_infos import *

class toolframe_infos_class:
        def __init__(self, master):
                self.__channel_intensity = tk.StringVar(master, "", name="channel_intensity")
                self.__channel_intensity.trace('w', channel_intensity_hook)

        def get_channel_intensity(self):
                return self.__channel_intensity.get()
        
        def set_channel_intensity(self, value):
                assert type(value) is str
                self.__channel_intensity.set(value)