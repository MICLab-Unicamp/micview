import tkinter as tk
from micview.models.getters import views

class ToolFrame(tk.Frame):
    def __init__(self, master: tk.Tk) -> None:
        super().__init__(master=master, width=185, background="#f1f2f6")
        self.place(x=0, rely=0.1, relheight=0.8)
        views['objects_ref'].ToolFrame = self
        self.actual_tool = None

    def setActualTool(self, ToolObject: object) -> None:
        self.actual_tool: object = ToolObject

    def delActualTool(self) -> None:
        if(self.actual_tool is not None):
            for widget in self.winfo_children():
                widget.destroy()
            del self.actual_tool
            self.actual_tool = None