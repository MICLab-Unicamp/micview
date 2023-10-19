import tkinter as tk
from components.image_viewer.ImageCanvas import ImageCanvas

class ImagesFrame(tk.Frame):    
    def __init__(self, master):
        self.master = master
        super().__init__(self.master, bd=4, bg= '#d4fe3ee', highlightbackground='#759fe6', highlightthickness=2)
        self.place(x=205, rely=0, relwidth=1, relheight=1, width=-205)
        self.CreateWidgets()

    def CreateWidgets(self):
        self.axial = ImageCanvas(self)
        self.axial.place(relheight=0.47, rely=0.02, relwidth=0.47, relx=0.02)
        self.coronal = ImageCanvas(self)
        self.coronal.place(relheight=0.47, rely=0.02, relwidth=0.47, relx=0.52)
        self.sagital = ImageCanvas(self)
        self.sagital.place(relheight=0.47, rely=0.52, relwidth=0.47, relx=0.52)
        self.imageorientation = ImageCanvas(self)
        self.imageorientation.place(relheight=0.47, rely=0.52, relwidth=0.47, relx=0.02)