import tkinter as tk
import math
import multiprocessing as mp
from PIL import Image, ImageTk
import Components.Volume_Initializer as Volinit
import Components.Volume_Controller as Volctrl
import Components.ImageFrame_Update as Imupdate
from Components.ImageFrame_Controller import *

square_image = False

def Square_Image_True():
    global square_image
    square_image = True
    
def Square_Image_False():
    global square_image
    square_image = False

def Get_Square_Image():
     global square_image
     return square_image

class ImageFrame:
    def __init__(self,frame):
        self.frame = frame
        self.canvasaxis0 = self.AxisLabel(relheight=0.47, rely=0.02, relwidth=0.47, relx=0.02)
        self.canvasaxis1 = self.AxisLabel(relheight=0.47, rely=0.02, relwidth=0.47, relx=0.52)
        self.canvasaxis2 = self.AxisLabel(relheight=0.47, rely=0.52, relwidth=0.47, relx=0.52)
        self.imageorientation = self.AxisLabel(relheight=0.47, rely=0.52, relwidth=0.47, relx=0.02)

    def AxisLabel(self, relheight, rely, relwidth, relx, fig=None):
        canvasaxis = tk.Canvas(self.frame, background="red")
        canvasaxis.place(relheight=relheight, rely=rely, relwidth=relwidth, relx=relx)
        labelaxis = tk.Label(canvasaxis, image=fig, background="lightblue")
        labelaxis.pack(expand=True, fill=tk.BOTH)
        return {"Canvas": canvasaxis, "Label": labelaxis}

    def Load_Images(self, image_sitk):
        self.image_sitk = image_sitk
        size=math.floor(self.canvasaxis0['Label'].winfo_height())
        self.squared_image = Volinit.ImagesContainer(image_sitk,square=True, cube_side=size)
        self.image = Volinit.ImagesContainer(image_sitk,square=False, cube_side=size)
        self.Labeled_images = self.Label_Images(self.image)
        self.Labeled_squared_images = self.Label_Images(self.squared_image)

        self.Controller = ImageFrame_Controller(self.canvasaxis0, self.canvasaxis1, self.canvasaxis2, self.imageorientation, self.image, self.squared_image)
        Imupdate.Resize_Images_Check(self.Controller, square_image=False)
        self.canvasaxis0['Label'].bind("<Configure>", self.BindConfigure)

    def Label_Images(self, image):
        image_data = Volctrl.get_2D_slices(image)
        Labeled_image = [Image.fromarray(image_data[0],mode='L'),Image.fromarray(image_data[1],mode='L'),Image.fromarray(image_data[2],mode='L')]
        Imgs = [ImageTk.PhotoImage(Labeled_image[0]), ImageTk.PhotoImage(Labeled_image[1]), ImageTk.PhotoImage(Labeled_image[2])]
        return Imgs
    
    def BindConfigure(self,event=None):
        global square_image
        Imupdate.Resize_Images_Check(self.Controller, square_image=square_image)