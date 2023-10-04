import tkinter as tk
from tkinter import ttk
from Components.SideWindows.SideWindow import *

class OpenFileInputWindow(SideWindow):
    def __init__(self, parent, rootframe, windowtitle="Open Image", TypeOfFile="Image"):
        super().__init__(parent,rootframe, windowtitle, TypeOfFile)
        self.root.protocol("WM_DELETE_WINDOW", self.OnClosing)
        self.DefineClassOptions()
        self.OptionsComboboxes()

    def DefineClassOptions(self):
        self.zoomorder = tk.IntVar(self.root, value=0, name="zoom_order")
        self.resized_image = tk.BooleanVar(self.root, value=False, name="resized_image")
        self.cancel.configure(command=self.OnClosing)
        self.openbutton.configure(command=self.LoadNewImage)

    def OptionsComboboxes(self):
        imageformat_text = tk.Label(self.root, text="Image Format", font=('Helvetica', 10), anchor="w", justify="left")
        imageformat_text.place(rely=0.55, relx=0.02, relheight=0.1, relwidth=0.6)
        self.image_format= ttk.Combobox(self.root, values=["Normal", "Resized"], state="readonly", justify="center")
        self.image_format.option_add('*TCombobox*Listbox.Justify', 'center')
        self.image_format.set("Normal")
        self.image_format.bind('<<ComboboxSelected>>', self.WatchResizedImage)
        self.image_format.place(rely= 0.55, relx=0.68, relheight=0.1, relwidth=0.20)
        
        zoom_combobox_text = tk.Label(self.root, text="Zoom Interpolation Order", font=('Helvetica', 10), anchor="w", justify="left")
        zoom_combobox_text.place(rely=0.7, relx=0.02, relheight=0.1, relwidth=0.6)
        self.zoom_interpolation_order = ttk.Combobox(self.root, values=[ str(x) for x in range(6)], state="readonly", justify="center")
        self.zoom_interpolation_order.option_add('*TCombobox*Listbox.Justify', 'center')
        self.zoom_interpolation_order.set("0")
        self.zoom_interpolation_order.bind('<<ComboboxSelected>>', self.WatchZoomOrder)
        self.zoom_interpolation_order.place(rely= 0.7, relx=0.68, relheight=0.1, relwidth=0.10)

    def LoadNewImage(self):
        if(self.parent.root.getvar(name="image_is_set")):
            self.parent.ImageFrame.Destroy_image()
        self.OnClosing(loadimage=True)

    def WatchZoomOrder(self,*args):
        value = self.zoom_interpolation_order.get()
        self.zoomorder.set(int(value))

    def WatchResizedImage(self, *args):
        value = self.image_format.get()
        if(value == "Normal"):
            self.resized_image.set(False)
        else:
            self.resized_image.set(True)

    def OnClosing(self, loadimage=False):
        self.filepath.trace_remove("write", self.traceid1)
        self.currentdirectory.trace_remove("write", self.traceid2)
        self.root.destroy()
        self.root.update()
        if(loadimage):
            self.parent.ImageFrame.Load_Images(file=self.finalpath, order=self.zoomorder.get(), resized = self.resized_image.get())
        self.parent.menuframe.DelSideWindow()