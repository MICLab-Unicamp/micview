import tkinter as tk
import Components.Images.ImageFrame_Update as Imupdate
import Components.Images.ImageFrame_Loader as Loader
from Components.Images.ImageFrame import *

class ImagesContainer:
    def __init__(self,root,frame):
        self.root = root
        self.frame = frame
        self.axis0 = ImageFrame(self.frame)
        self.axis0.place(relheight=0.47, rely=0.02, relwidth=0.47, relx=0.02)
        self.axis1 = ImageFrame(self.frame)
        self.axis1.place(relheight=0.47, rely=0.02, relwidth=0.47, relx=0.52)
        self.axis2 = ImageFrame(self.frame)
        self.axis2.place(relheight=0.47, rely=0.52, relwidth=0.47, relx=0.52)
        self.imageorientation = ImageFrame(self.frame)
        self.imageorientation.place(relheight=0.47, rely=0.52, relwidth=0.47, relx=0.02)
        self.Loader = Loader.ImageFrame_Loader(self)

    def AxisLabel(self, relheight, rely, relwidth, relx, fig=None):
        canvasaxis = tk.Canvas(self.frame, background="lightblue")
        canvasimage = canvasaxis.create_image(0,0,image=fig)
        canvasaxis.place(relheight=relheight, rely=rely, relwidth=relwidth, relx=relx)
        labelaxis = tk.Label(canvasaxis, image=fig)
        labelaxis.pack(expand=True, fill=tk.BOTH)
        return {"Canvas": canvasaxis, "Label": labelaxis, "CanvasImage": canvasimage}
