import numpy as np
from scipy.ndimage import zoom
from services.volume.controller import *
from services.volume.Mask_Pallete import *

def SettingMaskPallete(max):
    pallete = []
    for i in range(max):
        pallete.append(MaskPallete(i))
    return pallete

def Mask_Label_Colors(RGBA_mask, zoomed_mask):
    pallete = SettingMaskPallete(zoomed_mask.max())
    for label in pallete:
        RGBA_mask[:,:,:, 0] = np.where(zoomed_mask == label["Number"], label["RGB"][0], RGBA_mask[:,:,:,0])
        RGBA_mask[:,:,:, 1] = np.where(zoomed_mask == label["Number"], label["RGB"][1], RGBA_mask[:,:,:,1])
        RGBA_mask[:,:,:, 2] = np.where(zoomed_mask == label["Number"], label["RGB"][2], RGBA_mask[:,:,:,2])
    del pallete
    return RGBA_mask

def image_volume_loader(volume, square_image_boolean=False, order=0, cube_side=200):
        if len(volume.shape) == 4 and np.argmin(volume.shape) == 3:
            volume = volume.transpose(3, 0, 1, 2)
            assert np.argmin(volume.shape) == 0, "Couldn't solve wrong dimension channel. Put channel on dimension 0."
        #set original volume
        #set point_originalvol = (np.array(self.volume_shape[-1:-4:-1][::-1])/2).astype(int)
        #multichannel = len(self.volume_shape) > 3
        '''
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
        '''

        #sides = np.array(list(self.volume.shape))
        #self.max_side = sides.max()
        #if(square_image_boolean):
            #zoom_factors = (cube_side/self.volume_shape[-3], cube_side/self.volume_shape[-2], cube_side/self.volume_shape[-1])
        #else:
            #zoom_factors = (cube_side/self.max_side, cube_side/self.max_side, cube_side/self.max_side)
        #mask_zoom = zoom_factors
        #if multichannel:
            #self.volume = Volctrl.multi_channel_zoom(self.volume, zoom_factors, order=order)
        #else:
            #self.volume = zoom(self.volume, zoom_factors, order=order)
        
        #self.volume = ((self.volume - self.volume.min())*(255/(self.volume.max()-self.volume.min()))).astype(np.uint8)
        
        
def mask_volume_loader(mask=mask, square_image_boolean=False, cube_side=200):
    self.original_mask = mask
    zoomed_mask = Volctrl.zoom(mask, mask_zoom, order=0).astype(np.uint8)
    R = np.expand_dims(np.zeros_like(zoomed_mask), axis=-1).astype(np.uint8)
    G = np.zeros_like(R)
    B = np.zeros_like(R)
    A = np.expand_dims(np.where(zoomed_mask > 0, 255, 0), axis=-1)
    RGBA_mask = np.concatenate((R,G,B,A), axis=-1).astype(np.uint8)
    RGBA_mask = Mask_Label_Colors(RGBA_mask, zoomed_mask)
    self.mask = RGBA_mask