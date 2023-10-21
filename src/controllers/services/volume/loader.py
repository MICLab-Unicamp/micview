import numpy as np
from src.controllers.services.volume.controller import *
from src.controllers.services.volume.Mask_Pallete import *
from src.models.models import get_cursor_data, get_original_volume_data, get_changed_volume_data, get_toolframe_data

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
############### dividir essa função depois
def image_volume_loader(volume, order=0, cube_side=200):
        if len(volume.shape) == 4 and np.argmin(volume.shape) == 3:
            volume = volume.transpose(3, 0, 1, 2)
            assert np.argmin(volume.shape) == 0, "Couldn't solve wrong dimension channel. Put channel on dimension 0."
        get_original_volume_data().image_volume = volume
        point = (np.array(volume.shape[-1:-4:-1][::-1])/2).astype(int)
        get_cursor_data().current_point_original_vol = point
        multichannel = len(volume) > 3
        if(multichannel):
            get_toolframe_data().channel_intensity = list(volume[x, point[0], point[1], point[2]] for x in range(4))
            get_original_volume_data().num_of_channels = volume.shape[3]
        else:
            get_toolframe_data().channel_intensity = [volume[point[0], point[1], point[2]]]
            get_original_volume_data().num_of_channels = 1
        sides = np.array(list(volume.shape))
        max_side = sides.max()
        get_changed_volume_data().zoom_factors = (cube_side/max_side, cube_side/max_side, cube_side/max_side)
        if multichannel:
            volume = multi_channel_zoom(volume, get_changed_volume_data().zoom_factors, order=order)
        else:
            volume = zoom(volume, get_changed_volume_data().zoom_factors, order=order)
        volume = ((volume - volume.min())*(255/(volume.max() - volume.min()))).astype(np.uint8)
        get_changed_volume_data().changed_image_volume = volume  
        
def mask_volume_loader(mask):
    mask_zoom = get_changed_volume_data().zoom_factors
    get_original_volume_data().mask_volume = mask
    zoomed_mask = zoom(mask, mask_zoom, order=0).astype(np.uint8)
    R = np.expand_dims(np.zeros_like(zoomed_mask), axis=-1).astype(np.uint8)
    G = np.zeros_like(R)
    B = np.zeros_like(R)
    A = np.expand_dims(np.where(zoomed_mask > 0, 255, 0), axis=-1)
    RGBA_mask = np.concatenate((R,G,B,A), axis=-1).astype(np.uint8)
    RGBA_mask = Mask_Label_Colors(RGBA_mask, zoomed_mask)
    get_changed_volume_data().changed_mask_volume = RGBA_mask
