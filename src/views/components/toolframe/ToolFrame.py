import tkinter as tk
from toolframe.CursorTool import CursorTool
from globals.globals import toolframe_states, objects_ref

class ToolFrame(tk.Frame):
    def __init__(self, master):
        super().__init__(master=master, width=185, background="lightgray")
        self.place(x=0, rely=0.1, relheight=0.8)
        objects_ref.set_ToolFrame(self)
        self.actual_tool = None

    def set_actual_tool(self, ToolObject):
        self.actual_tool = ToolObject

    def del_actual_tool(self):
        if(self.actual_tool is not None):
            del self.actual_tool