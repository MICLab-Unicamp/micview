import tkinter as tk
import importlib
from types import ModuleType
models: ModuleType = importlib.import_module(name='micview.models.getters')

class ZoomTool:
    def __init__(self, master: tk.Tk):
        super().__init__()