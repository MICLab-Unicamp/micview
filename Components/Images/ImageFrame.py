import tkinter as tk

class ImageFrame(tk.Canvas):
    def __init__(self,root, background="lightblue"):
        super().__init__(root)
        self.root = root
        self.Image = None
        self.Mask = None

    def SetImage(self, imagedata):
        self.imagedata = imagedata
        self.SetCanvasDims()
        if(self.Image is None):
            self.Image = self.create_image((self.Width/2,self.Height/2),image=self.imagedata, anchor="center")
        else:
            self.itemconfig(self.Image, image=self.imagedata)

    def SetMask(self, maskdata):
        self.maskdata = maskdata
        self.SetCanvasDims()
        if(self.Mask is None):
            self.Mask = self.create_image((self.Width/2,self.Height/2),image=self.maskdata, anchor="center")
        else:
            self.itemconfig(self.Mask, image=self.maskdata)

    def SetCanvasDims(self):
        self.Width = self.winfo_width()
        self.Height = self.winfo_height()
        self.configure(width=self.Width, height=self.Height)