##
# @brief: This file contains the class that manages the loading states of the application.
#

# Imports
import tkinter as tk
from micview.controllers.hooks.loading_states_hooks import loadingHook

# Classes
class LoadingStatesClass:
    """!
    @brief: This class manages the loading states of the application.
    """
    def __init__(self, master: tk.Tk) -> None:
        """!
        @brief: The constructor of the class.
        @param: master: tk.Tk - The master window of the application.
        """
        super().__init__()
        self.__loading = tk.BooleanVar(master=master, value=False, name="loading")
        self.__loading.trace(mode='w', callback=loadingHook)       
        self.__image_is_loaded = False
        self.__mask_is_loaded = False

    @property
    def loading(self) -> bool:
        """!
        @brief: The getter method of the loading property.
        @return: bool
        """
        return self.__loading.get()
    
    @loading.setter
    def loading(self, value: bool) -> None:
        """!
        @brief: The setter method of the loading property.
        @param: value: bool - The value to be set.
        @return: None
        """
        assert type(value) is bool
        self.__loading.set(value=value)

    @property
    def image_is_loaded(self) -> bool:
        """!
        @brief: The getter method of the image_is_loaded property.
        @return: bool
        """
        return self.__image_is_loaded
    
    @image_is_loaded.setter
    def image_is_loaded(self, value: bool) -> None:
        """!
        @brief: The setter method of the image_is_loaded property.
        @param: value: bool - The value to be set.
        @return: None
        """
        assert type(value) is bool
        self.__image_is_loaded: bool = value
    
    @property
    def mask_is_loaded(self) -> bool:
        """!
        @brief: The getter method of the mask_is_loaded property.
        @return: bool
        """
        return self.__mask_is_loaded
    
    @mask_is_loaded.setter
    def mask_is_loaded(self, value: bool) -> None:
        """!
        @brief: The setter method of the mask_is_loaded property.
        @param: value: bool - The value to be set.
        @return: None
        """
        assert type(value) is bool
        self.__mask_is_loaded: bool = value