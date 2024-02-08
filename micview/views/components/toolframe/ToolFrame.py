##
# @brief: This file is used to create the ToolFrame class, which is used to create the tool frame in the main window.
#

# Imports
import tkinter as tk
from micview.models.getters import views

# Classes
class ToolFrame(tk.Frame):
    """!
    @brief: This class is used to create the tool frame in the main window.
    """
    def __init__(self, master: tk.Tk) -> None:
        """!
        @brief: The constructor of the class.
        @param: master: tk.Tk - The master window of the application.
        """
        super().__init__(master=master, width=185, background="#f1f2f6")
        self.place(x=0, rely=0.1, relheight=0.8)
        views['objects_ref'].ToolFrame = self
        self.actual_tool = None

    def setActualTool(self, ToolObject: object) -> None:
        """!
        @brief: This method sets the actual tool in the tool frame.
        @param: ToolObject: object - The tool object to be set.
        @return: None
        """
        self.actual_tool: object = ToolObject

    def delActualTool(self) -> None:
        """!
        @brief: This method deletes the actual tool in the tool frame.
        @return: None
        """
        if(self.actual_tool is not None):
            for widget in self.winfo_children():
                widget.destroy()
            del self.actual_tool
            self.actual_tool = None