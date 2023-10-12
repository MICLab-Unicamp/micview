import tkinter as tk

class ImageFrame(tk.Canvas):
    def __init__(self,root, background="lightblue"):
        super().__init__(root, background=background)
        self.root = root
        self.Width = 0
        self.Height = 0
        self.prev_center_x = None
        self.prev_center_y = None
        self.Image = None
        self.Mask = None

    def SetImage(self, imagedata):
        self.imagedata = imagedata
        self.SetCanvasDims()
        if(self.Image is None):
            self.Image = self.create_image((self.Width/2,self.Height/2),image=self.imagedata, anchor="center")
        else:
            self.itemconfig(self.Image, image=self.imagedata)
            self.move(self.Image, self.Width/2 - self.prev_center_x, self.Height/2 - self.prev_center_y)

    def SetMask(self, maskdata):
        self.maskdata = maskdata
        if(self.Mask is None):
            self.Mask = self.create_image((self.Width/2,self.Height/2),image=self.maskdata, anchor="center")
        else:
            self.itemconfig(self.Mask, image=self.maskdata)
            self.move(self.Mask, self.Width/2 - self.prev_center_x, self.Height/2 - self.prev_center_y)

    def SetCanvasDims(self):
        self.prev_center_x = self.Width/2
        self.prev_center_y = self.Height/2
        self.Width = self.winfo_width()
        self.Height = self.winfo_height()
        self.configure(width=self.Width, height=self.Height)

    def clean_screen(self):
        self.delete(self.Image)
        self.delete(self.Mask)
        self.Image = None
        self.Mask = None