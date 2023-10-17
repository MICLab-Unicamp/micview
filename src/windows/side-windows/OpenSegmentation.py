import tkinter as tk
from tkinter import ttk
from Components.SideWindows.SideWindow import *

class OpenFileSegmentation(SideWindow):
    def __init__(self, parent, rootframe, windowtitle="Open Segmentation", TypeOfFile="Segmentation"):
        super().__init__(parent,rootframe, windowtitle, TypeOfFile)
        self.root.protocol("WM_DELETE_WINDOW", self.OnClosing)
        self.DefineClassOptions()

    def DefineClassOptions(self):
        self.cancel.configure(command=self.OnClosing)
        self.openbutton.configure(command=self.LoadNewSegmentation)

    def LoadNewSegmentation(self):
        self.parent.Loader.MaskSet(self.finalpath)
        self.OnClosing()