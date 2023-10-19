import tkinter as tk
from hooks.infos.volume_infos import *

class volume_infos_class:
    def __init__(self, master):
        self.__num_of_channels = tk.IntVar(master, 1, name="num_of_channels")
        self.__num_of_channels.trace('w', num_of_channels_hook)
        self.__current_point = None
        self.__current_point_original_vol = None
        #image, image_square, mask, mask_square

    def get_num_of_channels(self):
        return self.__num_of_channels.get()
    
    def set_num_of_channels(self, value):
        assert type(value) is int
        self.__num_of_channels.set(value)

    def get_current_point(self):
        return self.__current_point
    
    def set_current_point(self, value):
        self.__current_point = value

    def get_current_point_original_vol(self):
        return self.__current_point_original_vol
    
    def set_current_point_original_vol(self, value):
        self.__current_point_original_vol = value