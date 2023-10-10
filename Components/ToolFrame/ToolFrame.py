import tkinter as tk
from Components.ToolFrame.CursorTool import *
from threading import Thread

class ToolFrame(Thread):
    def __init__(self, parent, rootframe):
        super().__init__()
        self.parent = parent
        self.rootframe = rootframe
        self.start()

    def run(self):
        self.toolframe = tk.Frame(self.rootframe, width=185, background="lightgray")
        self.toolframe.place(x=0, rely=0.1, relheight=0.8)
        self.tool_is_set = False
        self.setted_tool = "none"

    def WatchToolsVar(self, var):
        if(var == "cursor_tool"):
            if(self.tool_is_set):
                self.DelActualTool()
            self.actual_tool = CursorTool(self.parent, self.toolframe)
            self.tool_is_set = True
            self.setted_tool = var
        if(var == "channel_intensity" and self.tool_is_set and self.setted_tool == "cursor_tool"):
            self.actual_tool.Update_intensity()
        if(var == "image_unset"):
            self.tool_is_set = False
            self.DelActualTool()

    def DelActualTool(self):
        self.setted_tool = "none"
        del self.actual_tool