import tkinter as tk
from micview.controllers.hooks.image_canvas_hooks import action_on_child, update_all_childs

class image_canvas_states_class:
    def __init__(self, master: tk.Tk) -> None:
        super().__init__()
        self.__action_on_child = tk.IntVar(master=master, value=0, name="action_on_child")
        self.__action_on_child.trace_add(mode="write", callback=action_on_child)
        self.__update_all_childs = tk.BooleanVar(master=master, value=False, name="update_all_childs")
        self.__update_all_childs.trace_add(mode="write", callback=update_all_childs)

    @property
    def action_on_child(self) -> int:
        return self.__action_on_child.get()

    @action_on_child.setter
    def action_on_child(self, value: int) -> None:
        self.__action_on_child.set(value=value)

    @property
    def update_all_childs(self) -> bool:
        return self.__update_all_childs.get()
    
    @update_all_childs.setter
    def update_all_childs(self, value: bool) -> None:
        self.__update_all_childs.set(value=value)