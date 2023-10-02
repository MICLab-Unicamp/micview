import Components.Volume.Volume_Controller as Volctrl
import Components.ImageFrame.ImageFrame_Update as Imupdate
import Components.ImageFrame.ImageFrame as ImFrame
import math
import tkinter as tk

class ImageFrame_Controller:
    def __init__(self, root, axis0, axis1, axis2, imageorientation, image, square_image):
        self.root = root
        self.axis0 = axis0
        self.axis1 = axis1
        self.axis2 = axis2
        self.imageorientation = imageorientation
        self.image = image
        self.square_image = square_image
        self.CreateVars()

    def CreateVars(self):
        self.axis0['Label'].bind('<Button-1>', self.UpdatePointAxis0)
        self.axis0['Label'].bind('<B1-Motion>', self.UpdatePointAxis0)
        self.axis1['Label'].bind('<Button-1>', self.UpdatePointAxis1)
        self.axis1['Label'].bind('<B1-Motion>', self.UpdatePointAxis1)
        self.axis2['Label'].bind('<Button-1>', self.UpdatePointAxis2)
        self.axis2['Label'].bind('<B1-Motion>', self.UpdatePointAxis2)
        self.label_h = None
        self.label_w = None
        self.previous_label_h = None
        self.previous_label_w = None

    def UpdateImage(self):
        square_image_boolean = self.root.getvar(name="square_image_boolean")
        Imupdate.UpdateImages(self, square_image_boolean)       

    def UpdateImageResetPoint(self):
        square_image_boolean = self.root.getvar(name="square_image_boolean")
        Volctrl.reset_current_point()
        Imupdate.UpdateImages(self, square_image_boolean)

    def UpdateImageSize(self,images_sizes, label_w, label_h):
        self.images_sizes = images_sizes
        self.label_w = label_w
        self.label_h = label_h

    def UpdatePointAxis0(self, event):
        click = event.__dict__
        x = click['x']; y = click['y']
        new_point_x, new_point_y = self.UpdatePoint(self.images_sizes['axis0_x'], self.images_sizes['axis0_y'], x, y)
        if(new_point_x != None and new_point_y != None):
            square_image_boolean = self.root.getvar(name="square_image_boolean")
            Volctrl.change_current_point(-1,new_point_y,new_point_x, self.square_image) if square_image_boolean else Volctrl.change_current_point(-1,new_point_y,new_point_x, self.image)
            self.ChangeChannelsIntensity()
            Imupdate.UpdateImages(self,square_image_boolean)

    def UpdatePointAxis1(self, event):
        click = event.__dict__
        x = click['x']; y = click['y']
        new_point_x, new_point_y = self.UpdatePoint(self.images_sizes['axis1_x'], self.images_sizes['axis1_y'], x, y)
        if(new_point_x != None and new_point_y != None):
            square_image_boolean = self.root.getvar(name="square_image_boolean")
            Volctrl.change_current_point(new_point_y,-1,new_point_x, self.square_image) if square_image_boolean else Volctrl.change_current_point(new_point_y,-1,new_point_x, self.image)
            self.ChangeChannelsIntensity()
            Imupdate.UpdateImages(self,square_image_boolean)

    def UpdatePointAxis2(self, event):
        click = event.__dict__
        x = click['x']; y = click['y']
        new_point_x, new_point_y = self.UpdatePoint(self.images_sizes['axis2_x'], self.images_sizes['axis2_y'], x, y)
        if(new_point_x != None and new_point_y != None):
            square_image_boolean = self.root.getvar(name="square_image_boolean")
            Volctrl.change_current_point(new_point_y,new_point_x,-1, self.square_image) if square_image_boolean else Volctrl.change_current_point(new_point_y,new_point_x,-1, self.image)
            self.ChangeChannelsIntensity()
            Imupdate.UpdateImages(self,square_image_boolean)

    def UpdatePoint(self, image_size_x, image_size_y, x, y):
        center = (self.label_w/2, self.label_h/2)
        if(x < center[0] - image_size_x/2 or x > center[0] + image_size_x/2 or y < center[1] - image_size_y/2 or y > center[1] + image_size_y/2):
            return None, None #Clicked outside the image
        offsetx = math.floor((self.label_w - image_size_x)/2)
        new_point_x = int(x - offsetx) -1
        offsety = math.floor((self.label_h - image_size_y)/2)
        new_point_y = int(y - offsety) -1
        return new_point_x,new_point_y
    
    def ChangeChannelsIntensity(self):
        original_vol = self.image.handler_param["original_volume"]
        original_shape = original_vol.shape
        point = Volctrl.get_original_vol_current_point()
        multi = True if len(original_shape) > 3 else False
        intensity = []
        if(multi):
            for i in range(original_shape[0]):
                intensity.append(original_vol[i,point[0],point[1],point[2]])
        else:
            intensity.append(original_vol[point[0],point[1],point[2]])
        self.root.setvar(name="channel_intensity", value=str(intensity))