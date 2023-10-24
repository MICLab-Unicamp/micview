import tkinter as tk
from src.controllers.hooks.loading_states_hooks import *

class loading_states_class:
    def __init__(self, master):
        self.__loading = tk.BooleanVar(master, False, name="loading")
        self.__loading.trace('w', loading_hook)       
        self.__image_is_loaded = False
        self.__mask_is_loaded = False

    @property
    def loading(self):
        return self.__loading.get()
    
    @loading.setter
    def loading(self, value):
        assert type(value) is bool
        self.__loading.set(value)

    @property
    def image_is_loaded(self):
        return self.__image_is_loaded
    
    @image_is_loaded.setter
    def image_is_loaded(self, value):
        assert type(value) is bool
        self.__image_is_loaded = value
    
    @property
    def mask_is_loaded(self):
        return self.__mask_is_loaded
    
    @mask_is_loaded.setter
    def mask_is_loaded(self, value):
        assert type(value) is bool
        self.__mask_is_loaded = value