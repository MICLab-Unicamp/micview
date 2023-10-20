import tkinter as tk
from views.components.image_viewer.ImageCanvasView import ImageCanvasView

class ImagesFrame(tk.Frame):    
    def __init__(self, master):
        self.master = master
        super().__init__(self.master, bd=4, bg= '#d4fe3ee', highlightbackground='#759fe6', highlightthickness=2)
        self.place(x=205, rely=0, relwidth=1, relheight=1, width=-205)
        self.ConfigFrame()
        self.CreateWidgets()
    
    def ConfigFrame(self):
        for i in range(2):
            self.rowconfigure(index=i, weight=1, minsize=100)
            self.columnconfigure(index=i, weight=1, minsize=100)

    def CreateWidgets(self):######## trocar esses nomes depois
        self.axial = ImageCanvasView(self, id=0)
        self.axial.grid(row=0, column=0, padx=5, pady=5)
        #self.axial.place(relheight=0.47, rely=0.02, relwidth=0.47, relx=0.02)
        self.coronal = ImageCanvasView(self, id=1)
        self.coronal.grid(row=0, column=1, padx=5, pady=5)
        #self.coronal.place(relheight=0.47, rely=0.02, relwidth=0.47, relx=0.52)
        self.sagital = ImageCanvasView(self, id=2)
        #self.sagital.place(relheight=0.47, rely=0.52, relwidth=0.47, relx=0.52)
        self.sagital.grid(row=1, column=1, padx=5, pady=5)
        self.imageorientation = tk.Label(self)
        self.imageorientation.grid(row=1, column=0, padx=5, pady=5)
        #self.imageorientation.place(relheight=0.47, rely=0.52, relwidth=0.47, relx=0.02)