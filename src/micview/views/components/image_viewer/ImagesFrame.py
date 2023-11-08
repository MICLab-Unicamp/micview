import tkinter as tk
from src.micview.views.components.image_viewer.ImageCanvasView import ImageCanvasView
from src.micview.models.getters import views

class ImagesFrame(tk.Frame):    
    def __init__(self, master):
        self.master = master
        super().__init__(self.master, bd=4, bg= '#dfe3ee', highlightbackground='#759fe6', highlightthickness=2)
        self.place(x=205, rely=0, relwidth=1, relheight=1, width=-205)
        self.ConfigFrame()
        self.CreateWidgets()

    def ConfigFrame(self):
        views['objects_ref'].ImagesFrame = self
        for i in range(2):
            self.rowconfigure(index=i, weight=1, minsize=150)
            self.columnconfigure(index=i, weight=1, minsize=150)

    def CreateWidgets(self):
        self.axial = ImageCanvasView(self, id=0)
        self.axial.grid(row=0, column=0, padx=5, pady=5, sticky='news')
        self.coronal = ImageCanvasView(self, id=1)
        self.coronal.grid(row=0, column=1, padx=5, pady=5, sticky='news')
        self.sagital = ImageCanvasView(self, id=2)
        self.sagital.grid(row=1, column=1, padx=5, pady=5, sticky='news')
        self.imageorientation = tk.Canvas(self, background='lightblue')
        self.imageorientation.grid(row=1, column=0, padx=5, pady=5, sticky='news')
