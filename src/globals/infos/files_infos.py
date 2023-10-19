import tkinter as tk

class files_infos_class:
    def __init__(self, master):
        self.__image_file = None
        self.__mask_file = None

    def get_image_file(self):
        return self.__image_file
    
    def set_image_file(self, value):
        self.__image_file = value

    def get_mask_file(self):
        return self.__mask_file
    
    def set_mask_file(self, value):
        self.__mask_file = value