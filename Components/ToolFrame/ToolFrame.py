import tkinter as tk
from Components.ToolFrame.CursorTool import *

class ToolFrame:
    def __init__(self, parent, rootframe):
        self.parent = parent
        self.rootframe = rootframe
        self.toolframe = tk.Frame(self.rootframe, width=185, background="lightgray")
        self.toolframe.place(x=0, rely=0.1, relheight=0.8)
        self.tool_is_set = False

    def WatchToolsVar(self, var):
        if(var == "cursor_tool"):
            if(self.tool_is_set):
                self.DelActualTool()
            self.actual_tool = CursorTool(self.parent, self.toolframe)
            self.tool_is_set = True
        if(var == "channel_intensity" and self.tool_is_set):
            self.actual_tool.Update_intensity()

    def DelActualTool(self):
        del self.actual_tool