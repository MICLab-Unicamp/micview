import numpy as np
from threading import Thread
from src.controllers.services.volume.controller import *
from src.controllers.services.volume.Mask_Pallete import *
from src.models.models import get_cursor_data, get_original_volume_data, get_changed_volume_data, get_toolframe_data, get_loading_states, get_options_states
from src.controllers.services.files.file_reader import readImageFile, readMaskFile

class image_and_mask_sync_loader(Thread):
    def __init__(self, file, order=0, image_is_square=False, mask_file=None):
        super().__init__()
        self.file = file
        self.order = order
        self.image_is_square = image_is_square
        self.mask_file = mask_file
    
    def run(self):
        self.image_loader_thread = image_volume_loader(path=self.file, order=self.order, image_is_square=self.image_is_square, ends_loading = False)
        self.mask_loader_thread = mask_volume_loader(path=self.mask_file)
        self.image_loader_thread.start()
        self.image_loader_thread.join()
        self.mask_loader_thread.start()
        self.mask_loader_thread.join()

class image_volume_loader(Thread):
    def __init__(self, path, order=0, image_is_square=False, ends_loading = True):
        super().__init__()
        self.path = path
        self.order = order
        self.image_is_square = image_is_square
        self.ends_loading = ends_loading

    def run(self):
        self.volume = readImageFile(self.path)
        if len(self.volume.shape) == 4 and np.argmin(self.volume.shape) == 3:
            self.volume = self.volume.transpose(3, 0, 1, 2)
            assert np.argmin(self.volume.shape) == 0, "Couldn't solve wrong dimension channel. Put channel on dimension 0."
        get_original_volume_data().image_volume = self.volume
        set_channels_intensity(self.volume)
        self.volume = zoom_volume(self.volume, order=self.order)
        self.volume = ((self.volume - self.volume.min())*(255/(self.volume.max() - self.volume.min()))).astype(np.uint8)
        get_changed_volume_data().changed_image_volume = self.volume
        get_loading_states().image_is_loaded = True
        get_options_states().image_is_square = self.image_is_square
        if(self.ends_loading):
            get_loading_states().loading =  False
        
class mask_volume_loader(Thread):
    def __init__(self, path):
        super().__init__()
        self.path = path

    def run(self):
        self.mask = readMaskFile(path=self.path)
        mask_zoom = get_changed_volume_data().zoom_factors
        get_original_volume_data().mask_volume = self.mask
        zoomed_mask = zoom(self.mask, mask_zoom, order=0).astype(np.uint8)
        R = np.expand_dims(np.zeros_like(zoomed_mask), axis=-1).astype(np.uint8)
        G = np.zeros_like(R)
        B = np.zeros_like(R)
        A = np.expand_dims(np.where(zoomed_mask > 0, 255, 0), axis=-1)
        RGBA_mask = np.concatenate((R,G,B,A), axis=-1).astype(np.uint8)
        RGBA_mask = Mask_Label_Colors(RGBA_mask, zoomed_mask)
        get_changed_volume_data().changed_mask_volume = RGBA_mask
        get_loading_states().image_is_loaded = True
        get_loading_states().mask_is_loaded = True
        get_options_states().mask_is_set = True
        if(get_loading_states().image_is_loaded):
            get_loading_states().loading = False

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

def set_channels_intensity(volume):
    point = (np.array(volume.shape[-1:-4:-1][::-1])/2).astype(int)
    get_cursor_data().current_point_original_vol = point
    get_cursor_data().current_point = None
    multichannel = len(volume.shape) > 3
    if(multichannel):
        get_toolframe_data().channel_intensity = str(list(volume[x, point[0], point[1], point[2]] for x in range(4)))
        get_original_volume_data().num_of_channels = volume.shape[0]
    else:
        get_toolframe_data().channel_intensity = str([volume[point[0], point[1], point[2]]])
        get_original_volume_data().num_of_channels = 1

def zoom_volume(volume, order, cube_side=200):
    multichannel = len(volume.shape) > 3
    sides = np.array(list(volume.shape))
    max_side = sides.max()
    get_changed_volume_data().zoom_factors = (cube_side/max_side, cube_side/max_side, cube_side/max_side)
    if multichannel:
        volume = multi_channel_zoom(volume, get_changed_volume_data().zoom_factors, order=order)
    else:
        volume = zoom(volume, get_changed_volume_data().zoom_factors, order=order)
    return volume