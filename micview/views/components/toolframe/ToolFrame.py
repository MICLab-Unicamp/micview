import tkinter as tk
from micview.models.getters import views

class ToolFrame(tk.Frame):
    def __init__(self, master: tk.Tk) -> None:
        super().__init__(master=master, width=185, background="#f1f2f6")
        self.place(x=0, rely=0.1, relheight=0.8)
        views['objects_ref'].ToolFrame = self
        self.actual_tool = None

    def set_actual_tool(self, ToolObject: object) -> None:
        self.actual_tool: object = ToolObject

    def del_actual_tool(self) -> None:
        if(self.actual_tool is not None):
            del self.actual_tool