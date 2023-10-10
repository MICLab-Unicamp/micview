import tkinter as tk
import Components.ImageFrame.ImageFrame_Update as Imupdate
import Components.ImageFrame.ImageFrame_Loader as Loader
from PIL import ImageTk, Image

class ImageFrame:
    def __init__(self,root,frame):
        self.root = root
        self.frame = frame
        self.canvasaxis0 = self.AxisLabel(relheight=0.47, rely=0.02, relwidth=0.47, relx=0.02)
        self.canvasaxis1 = self.AxisLabel(relheight=0.47, rely=0.02, relwidth=0.47, relx=0.52)
        self.canvasaxis2 = self.AxisLabel(relheight=0.47, rely=0.52, relwidth=0.47, relx=0.52)
        self.imageorientation = self.AxisLabel(relheight=0.47, rely=0.52, relwidth=0.47, relx=0.02)
        self.Loader = Loader.ImageFrame_Loader(self)

    def AxisLabel(self, relheight, rely, relwidth, relx, fig=None):
        canvasaxis = tk.Canvas(self.frame, background="red")
        canvasaxis.place(relheight=relheight, rely=rely, relwidth=relwidth, relx=relx)
        labelaxis = tk.Label(canvasaxis, image=fig, background="lightblue")
        labelaxis.pack(expand=True, fill=tk.BOTH)
        return {"Canvas": canvasaxis, "Label": labelaxis}
