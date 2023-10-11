import SimpleITK as sitk
import math
import multiprocessing as mp
from threading import Thread
import os
from Components.Images.ImageFrame_Controller import *
from Components.CircularProgressbar import *
import Components.Volume.Volume_Initializer as Volinit
import Components.Volume.Volume_Controller as Volctrl

class ImageFrame_Loader:
    def __init__(self, parent):
        self.parent = parent
        self.root = parent.root
        self.path = None
        self.mask_path = None
        self.sitk_maskfile = None
        self.interpolation_order = 0

    def ImageSet(self, **kwargs):
        if(self.root.getvar(name="image_is_set")):
            self.Destroy_image()

        self.task = Thread(target=self.Load_Images, kwargs={**kwargs})
        self.task.start()
    
    def Load_Images(self, **kwargs):
        self.root.setvar(name="loading", value=True)
        self.checkKwargs(**kwargs)
        
        self.sitk_file = sitk.ReadImage(self.path)
        self.sitk_file = sitk.GetArrayFromImage(self.sitk_file)
        if(self.mask_path is not None): 
            self.sitk_maskfile = sitk.ReadImage(self.mask_path)
            self.sitk_maskfile = sitk.GetArrayFromImage(self.sitk_maskfile)
    
        size=math.floor(self.parent.axis0.winfo_height())        
        mp_images_params = [(self.sitk_file, True, self.sitk_maskfile, size, self.interpolation_order), (self.sitk_file, False, self.sitk_maskfile, size, self.interpolation_order)]
        self.square_image, self.image = self.MultiprocessReadFiles(mp_images_params, order=self.interpolation_order)
        
        self.CheckMultichannel()

        self.Controller = ImageFrame_Controller(self.root,self.parent.axis0, self.parent.axis1, self.parent.axis2, self.parent.imageorientation, self.image, self.square_image)
        square_image_boolean = self.root.getvar(name="square_image_boolean")
        Imupdate.Resize_Images_Check(self.Controller, square_image_boolean=square_image_boolean)
        
        self.parent.axis0.bind("<Configure>", self.BindConfigure)
        self.root.setvar(name="toolvar", value="cursor_tool")
        image_is_set = self.root.getvar(name="image_is_set")
        if not image_is_set: self.root.setvar(name="image_is_set", value=True)
        self.root.setvar(name="loading", value=False)

    def Destroy_image(self):
        self.task.join()
        self.root.setvar(name="image_is_set", value=False)
        self.parent.axis0.unbind("<Configure>")
        self.Controller.Unbindaxis()
        self.Controller.UnsetImages()
        self.mask_path = None
        del self.sitk_file
        del self.sitk_maskfile
        del self.square_image
        del self.image
        del self.Controller
        Volctrl.reset_current_point()

    def CheckMultichannel(self):
        point = self.image.handler_param["point_original_vol"]
        volume = self.image.handler_param["original_volume"] 
        if(len(self.sitk_file.shape) > 3): 
            intensity = list(volume[x, point[0], point[1], point[2]] for x in range(4))
            self.root.setvar(name="channel_select", value=0)
            self.root.setvar(name="num_of_channels", value=self.sitk_file.shape[3])
            self.root.setvar(name="channel_intensity", value=str(intensity))
        else:
            intensity = [volume[point[0], point[1], point[2]]]
            self.root.setvar(name="channel_select", value=-1)
            self.root.setvar(name="num_of_channels", value=1)
            self.root.setvar(name="channel_intensity", value=str(intensity))
    
    def checkKwargs(self, **kwargs):
        for key, value in kwargs.items():
            if(key == "file"):
                self.path = value
            elif(key == "resized"):
                self.root.setvar(name="square_image_boolean", value=value)
            elif(key == "order"):
                self.interpolation_order = value
            elif(key == "mask"):
                self.mask_path = value
        
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
    volume, square_image_boolean, mask, cube_side, order = params
    return Volinit.ImagesContainer(volume=volume, square_image_boolean=square_image_boolean, mask=mask, cube_side=cube_side, order=order)