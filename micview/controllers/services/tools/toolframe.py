##
# @brief: This file contains the services for the toolframe
#

# Imports
import importlib
import tkinter as tk
from types import ModuleType
from micview.views.components.toolframe.EditTool import EditTool
from micview.views.components.toolframe.ZoomTool import ZoomTool
from micview.views.components.toolframe.ImageContrast import ImageContrast
from micview.views.components.toolframe.CursorTool import CursorTool
models: ModuleType = importlib.import_module(name='micview.models.getters')

# Functions
def setTool(tool: object, master: tk.Tk) -> None:
    """!
    @brief: This function is responsible for setting the actual tool.
    @param: tool: object - The tool to be set.
    @param: master: tk.Tk - The master window.
    @return: None
    """
    delTool(master=master)
    if(tool == "cursor"):
        master.setActualTool(CursorTool(master=master))
    if(tool == "contrast"):
        master.setActualTool(ImageContrast(master=master))
    if(tool == "zoom"):
        master.setActualTool(ZoomTool(master=master))
    if(tool == "edit"):
        master.setActualTool(EditTool(master=master))

def delTool(master: tk.Tk) -> None:
    """!
    @brief: This function is responsible for deleting the actual tool.
    @param: master: tk.Tk - The master window.
    @return: None
    """
    master.delActualTool()
    del models.views['objects_ref'].ToolFrame
    