import tkinter as tk
import math
import SimpleITK as sitk
import multiprocessing as mp
import os
import Components.Volume.Volume_Initializer as Volinit
import Components.Volume.Volume_Controller as Volctrl
import Components.ImageFrame.ImageFrame_Update as Imupdate
from Components.ImageFrame.ImageFrame_Controller import *

class ImageFrame:
    def __init__(self,root,frame):
        self.root = root
        self.frame = frame
        self.interpolation_order = 0
        self.path = None
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

    def Load_Images(self, **kwargs):
        self.checkKwargs(**kwargs)
        image_is_set = self.root.getvar(name="image_is_set")
        if not image_is_set: self.root.setvar(name="image_is_set", value=True)
        self.sitk_file = sitk.ReadImage(self.path)
        self.sitk_file = sitk.GetArrayFromImage(self.sitk_file)
        size=math.floor(self.canvasaxis0['Label'].winfo_height())        
        mp_images_params = [(self.sitk_file, True, size, self.interpolation_order), (self.sitk_file, False, size, self.interpolation_order)]
        self.square_image, self.image = self.MultiprocessReadFiles(mp_images_params, order=self.interpolation_order)
        self.Controller = ImageFrame_Controller(self.root,self.canvasaxis0, self.canvasaxis1, self.canvasaxis2, self.imageorientation, self.image, self.square_image)
        square_image_boolean = self.root.getvar(name="square_image_boolean")
        Imupdate.Resize_Images_Check(self.Controller, square_image_boolean=square_image_boolean)
        self.canvasaxis0['Label'].bind("<Configure>", self.BindConfigure)

    def Destroy_image(self):
        self.root.setvar(name="image_is_set", value=False)
        del self.sitk_file
        del self.square_image
        del self.image
        del self.Controller
        self.canvasaxis0['Label'].unbind_all("<Configure>")
        Volctrl.reset_current_point()
    
    def checkKwargs(self, **kwargs):
        for key, value in kwargs.items():
            if(key == "file"):
                self.path = value
            elif(key == "resized"):
                self.root.setvar(name="square_image_boolean", value=value)
            elif(key == "order"):
                self.interpolation_order = value

    def BindConfigure(self,event=None):
        square_image_boolean = self.root.getvar(name="square_image_boolean")
        Imupdate.Resize_Images_Check(self.Controller, square_image_boolean=square_image_boolean)

    def MultiprocessReadFiles(self, params, order):
        if(order > 0):
            p = mp.Pool(os.cpu_count())
            result = p.map(auxargs, params)
            p.close()
            p.join()
        else:
            result = map(auxargs, params)
        return result
    
def auxargs(params):
    volume, square_image_boolean, cube_side, order = params
    return Volinit.ImagesContainer(volume=volume, square_image_boolean=square_image_boolean, cube_side=cube_side, order=order)