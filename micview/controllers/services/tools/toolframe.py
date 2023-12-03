import tkinter as tk
from micview.views.components.toolframe.CursorTool import CursorTool

def setTool(tool: object, master: tk.Tk) -> None:
    if(tool == "cursor"):
        master.setActualTool(CursorTool(master=master))