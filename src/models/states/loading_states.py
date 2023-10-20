import tkinter as tk
import tkinter as tk
from controllers.hooks.loading_states_hooks import *

class loading_states_class:
    def __init__(self, master):
        self.__loading = tk.BooleanVar(master, False, name="loading")
        self.__loading.trace('w', loading_hook)       
        self.__image_is_loaded = tk.BooleanVar(master, False, name="image_is_loaded")
        self.__image_is_loaded.trace('w', image_is_loaded_hook)
        self.__mask_is_loaded = tk.BooleanVar(master, False, name="mask_is_loaded")
        self.__mask_is_loaded.trace('w', mask_is_loaded_hook)

    @property
    def loading(self):
        return self.__loading.get()
    
    @loading.setter
    def loading(self, value):
        assert type(value) is bool
        self.__loading.set(value)

    @property
    def image_is_loaded(self):
        return self.__image_is_loaded.get()
    
    @image_is_loaded.setter
    def image_is_loaded(self, value):
        assert type(value) is bool
        return self.__image_is_loaded.set(value)
    
    @property
    def mask_is_loaded(self):
        return self.__mask_is_loaded.get()
    
    @mask_is_loaded.setter
    def mask_is_loaded(self, value):
        assert type(value) is bool
        self.__mask_is_loaded.set(value)