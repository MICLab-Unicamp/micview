import tkinter as tk
import math
from PIL import Image, ImageTk
import Components.Volume_Initializer as Volinit
import Components.Volume_Controller as Volctrl
from Components.ImageFrame_Controller import *

square_image = False

class ImageFrame:
    def __init__(self,frame):
        self.frame = frame
        self.image_h = None
        self.image_w = None
        self.previous_image_h = None
        self.previous_image_w = None
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
        
        self.squared_image = Volinit.ImagesContainer(self.image_sitk,square=True, cube_side=size)
        self.image = Volinit.ImagesContainer(self.image_sitk, cube_side=size)
        
        self.Labeled_images = self.Label_Images(self.image)
        self.Labeled_squared_images = self.Label_Images(self.squared_image)

        self.Controller = ImageFrame_Controller(self.canvasaxis0, self.canvasaxis1, self.canvasaxis2, self.imageorientation)
        self.Resize_Images()
        self.canvasaxis0['Label'].bind("<Configure>", self.Resize_Images)
    
    def Label_Images(self, image):
        image_data = Volctrl.update_volume_point(self.image)
        Labeled_image = [Image.fromarray(image_data[0],mode='F'),Image.fromarray(image_data[1],mode='F'),Image.fromarray(image_data[2],mode='F')]
        Imgs = [ImageTk.PhotoImage(Labeled_image[0]), ImageTk.PhotoImage(Labeled_image[1]), ImageTk.PhotoImage(Labeled_image[2])]
        return Imgs
    
    def UpdateSquareImage(self):
        global square_image
        square_image = True
        self.UpdateImages()
    
    def UpdateNormalImage(self):
        global square_image
        square_image = False
        self.UpdateImages()
    
    def UpdateImages(self, resized_window=False):
        if(self.image_h == None or self.image_h <= 1): # Screen Not Open Yet
            return
        global square_image
        if(not resized_window):
            self.image_w = self.canvasaxis0['Label'].winfo_width()
            self.image_h = self.canvasaxis0['Label'].winfo_height()
        if(square_image):
            new_sizes = Volctrl.ImageResizing(self.squared_image, self.image_h)
        else:
            new_sizes = Volctrl.ImageResizing(self.image, self.image_h)

        image_data = Volctrl.update_volume_point(self.image)
        Labeled_image = [Image.fromarray(image_data[0],mode='F'),Image.fromarray(image_data[1],mode='F'),Image.fromarray(image_data[2],mode='F')]
        Imgs = [ImageTk.PhotoImage(Labeled_image[0].resize((new_sizes["axis0_x"],new_sizes["axis0_y"]))),
                ImageTk.PhotoImage(Labeled_image[1].resize((new_sizes["axis1_x"],new_sizes["axis1_y"]))), 
                ImageTk.PhotoImage(Labeled_image[2].resize((new_sizes["axis2_x"],new_sizes["axis2_y"])))]
        self.Labeled_images = Imgs
        self.images_sizes = new_sizes
        self.canvasaxis0['Label'].configure(image=Imgs[0])
        self.canvasaxis0['Label'].image = Imgs[0]
        self.canvasaxis1['Label'].configure(image=Imgs[1])
        self.canvasaxis1['Label'].image = Imgs[1]
        self.canvasaxis2['Label'].configure(image=Imgs[2])
        self.canvasaxis2['Label'].image = Imgs[2]
    
    def Resize_Images(self,e=None):
        self.image_w = self.canvasaxis0['Label'].winfo_width()
        self.image_h = self.canvasaxis0['Label'].winfo_height()
        if(self.image_h != self.previous_image_h or self.image_w != self.previous_image_w):
            self.previous_image_w = self.canvasaxis0['Label'].winfo_width()
            self.previous_image_h = self.canvasaxis0['Label'].winfo_height()
            self.UpdateImages(resized_window=True)