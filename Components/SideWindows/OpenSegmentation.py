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
        #if(self.parent.root.getvar(name="seg_is_set")):        
        if(self.parent.root.getvar(name="image_is_set")):
            self.parent.ImageFrame.Destroy_image()
        self.OnClosing(loadimage=True)

    def OnClosing(self, loadimage=False):
        self.filepath.trace_remove("write", self.traceid1)
        self.currentdirectory.trace_remove("write", self.traceid2)
        self.root.destroy()
        self.root.update()
        if(loadimage):
            self.parent.ImageFrame.Load_Images(file=self.finalpath)
        self.parent.menuframe.DelSideWindow()