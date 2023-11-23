import tkinter as tk
from micview.views.components.toolframe.CursorTool import CursorTool

def Set_Tool(tool: object, master: tk.Tk) -> None:
    if(tool == "cursor"):
        master.set_actual_tool(CursorTool(master=master))