import tkinter as tk
from src.micview.models.getters import views

class ToolFrame(tk.Frame):
    def __init__(self, master):
        super().__init__(master=master, width=185, background="lightgray")
        self.place(x=0, rely=0.1, relheight=0.8)
        views['objects_ref'].ToolFrame = self
        self.actual_tool = None

    def set_actual_tool(self, ToolObject):
        self.actual_tool = ToolObject

    def del_actual_tool(self):
        if(self.actual_tool is not None):
            del self.actual_tool