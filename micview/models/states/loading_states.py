import tkinter as tk
from micview.controllers.hooks.loading_states_hooks import loadingHook

class LoadingStatesClass:
    def __init__(self, master: tk.Tk) -> None:
        super().__init__()
        self.__loading = tk.BooleanVar(master=master, value=False, name="loading")
        self.__loading.trace(mode='w', callback=loadingHook)       
        self.__image_is_loaded = False
        self.__mask_is_loaded = False

    @property
    def loading(self) -> bool:
        return self.__loading.get()
    
    @loading.setter
    def loading(self, value: bool) -> None:
        assert type(value) is bool
        self.__loading.set(value=value)

    @property
    def image_is_loaded(self) -> bool:
        return self.__image_is_loaded
    
    @image_is_loaded.setter
    def image_is_loaded(self, value: bool) -> None:
        assert type(value) is bool
        self.__image_is_loaded: bool = value
    
    @property
    def mask_is_loaded(self) -> bool:
        return self.__mask_is_loaded
    
    @mask_is_loaded.setter
    def mask_is_loaded(self, value: bool) -> None:
        assert type(value) is bool
        self.__mask_is_loaded: bool = value