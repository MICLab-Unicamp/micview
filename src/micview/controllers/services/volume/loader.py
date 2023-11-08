import numpy as np
from threading import Thread
from src.micview.controllers.services.volume.controller import *
from src.micview.controllers.services.volume.Mask_Pallete import *
from src.micview.models.getters import data
from src.micview.controllers.services.files.file_reader import readImageFile, readMaskFile

class image_and_mask_sync_loader(Thread):
    def __init__(self, file, mask_file=None):
        super().__init__(daemon=True)
        self.file = file
        self.mask_file = mask_file
    
    def run(self):
        self.image_loader_thread = image_volume_loader(path=self.file)
        self.image_loader_thread.start()
        self.image_loader_thread.join()
        if(self.mask_file is not None):
            self.mask_loader_thread = mask_volume_loader(path=self.mask_file)
            self.mask_loader_thread.start()
            self.mask_loader_thread.join()

class image_volume_loader(Thread):
    def __init__(self, path):
        super().__init__(daemon=True)
        self.path = path

    def run(self):
        self.volume = readImageFile(self.path)
        if len(self.volume.shape) == 4 and np.argmin(self.volume.shape) == 3:
            self.volume = self.volume.transpose(3, 0, 1, 2)
            assert np.argmin(self.volume.shape) == 0, "Couldn't solve wrong dimension channel. Put channel on dimension 0."
        data['original_volume_data'].image_volume = self.volume
        set_channels_intensity(self.volume)
        self.volume = ((self.volume - self.volume.min())*(255/(self.volume.max() - self.volume.min()))).astype(np.uint8)
        data['changed_volume_data'].changed_image_volume = self.volume
        
class mask_volume_loader(Thread):
    def __init__(self, path):
        super().__init__(daemon=True)
        self.path = path

    def run(self):
        self.mask = readMaskFile(path=self.path)
        data['original_volume_data'].mask_volume = self.mask
        R = np.expand_dims(np.zeros_like(self.mask), axis=-1).astype(np.uint8)
        G = np.zeros_like(R)
        B = np.zeros_like(R)
        A = np.expand_dims(np.where(self.mask > 0, 255, 0), axis=-1)
        RGBA_mask = np.concatenate((R,G,B,A), axis=-1).astype(np.uint8)
        RGBA_mask = Mask_Label_Colors(RGBA_mask, self.mask)
        data['changed_volume_data'].changed_mask_volume = RGBA_mask

def SettingMaskPallete(max):
    pallete = []
    for i in range(max):
        pallete.append(MaskPallete(i))
    return pallete

def Mask_Label_Colors(RGBA_mask, mask):
    pallete = SettingMaskPallete(mask.max())
    for label in pallete:
        RGBA_mask[:,:,:, 0] = np.where(mask == label["Number"], label["RGB"][0], RGBA_mask[:,:,:,0])
        RGBA_mask[:,:,:, 1] = np.where(mask == label["Number"], label["RGB"][1], RGBA_mask[:,:,:,1])
        RGBA_mask[:,:,:, 2] = np.where(mask == label["Number"], label["RGB"][2], RGBA_mask[:,:,:,2])
    del pallete
    return RGBA_mask

def set_channels_intensity(volume):
    point = (np.array(volume.shape[-1:-4:-1][::-1])/2).astype(int)
    data['cursor_data'].current_point_original_vol = point
    data['cursor_data'].current_point = None
    multichannel = len(volume.shape) > 3
    if(multichannel):
        data['toolframe_data'].channel_intensity = str(list(volume[x, point[0], point[1], point[2]] for x in range(4)))
        data['original_volume_data'].num_of_channels = volume.shape[0]
    else:
        data['toolframe_data'].channel_intensity = str([volume[point[0], point[1], point[2]]])
        data['original_volume_data'].num_of_channels = 1