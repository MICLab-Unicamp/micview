##
# @brief: This file contains the EditTool class, which is a component of the ToolFrame class.
#

# Imports
import tkinter as tk
import importlib
from types import ModuleType
models: ModuleType = importlib.import_module(name='micview.models.getters')

# Classes
class EditTool:
    """!
    @brief: This class represents the edit tool in the toolframe.
    """
    def __init__(self, master: tk.Tk):
        super().__init__()