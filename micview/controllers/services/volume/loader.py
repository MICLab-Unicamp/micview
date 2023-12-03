from typing import Any, List
import numpy as np
from threading import Thread
from micview.controllers.services.volume.maskPallete import maskPallete
from micview.models.getters import data
from micview.controllers.services.files.file_reader import readImageFile, readMaskFile

class ImageAndMaskSyncLoader(Thread):
    def __init__(self, file: str, mask_file: str=None):
        super().__init__(daemon=True)
        self.file: str = file
        self.mask_file: str = mask_file
    
    def run(self) -> None:
        self.image_loader_thread = ImageVolumeLoader(path=self.file)
        self.image_loader_thread.start()
        self.image_loader_thread.join()
        if(self.mask_file is not None):
            self.mask_loader_thread = MaskVolumeLoader(path=self.mask_file)
            self.mask_loader_thread.start()
            self.mask_loader_thread.join()

class ImageVolumeLoader(Thread):
    def __init__(self, path: str) -> None:
        super().__init__(daemon=True)
        self.path: str = path

    def run(self) -> None:
        self.volume: List[Any] = readImageFile(path=self.path)
        if len(self.volume.shape) == 4 and np.argmin(self.volume.shape) == 3:
            self.volume = self.volume.transpose(3, 0, 1, 2)
            assert np.argmin(self.volume.shape) == 0, "Couldn't solve wrong dimension channel. Put channel on dimension 0."
        data['original_volume_data'].image_volume = self.volume
        setChannelsIntensity(volume=self.volume)
        self.volume = ((self.volume - self.volume.min())*(255/(self.volume.max() - self.volume.min()))).astype(np.uint8)
        data['changed_volume_data'].changed_image_volume = self.volume
        
class MaskVolumeLoader(Thread):
    def __init__(self, path: str) -> None:
        super().__init__(daemon=True)
        self.path: str = path

    def run(self) -> None:
        self.mask: List[Any] = readMaskFile(path=self.path)
        data['original_volume_data'].mask_volume = self.mask
        R: List[Any] = np.expand_dims(np.zeros_like(self.mask), axis=-1).astype(dtype=np.uint8)
        G: List[Any] = np.zeros_like(R)
        B: List[Any] = np.zeros_like(R)
        A: List[Any] = np.expand_dims(np.where(self.mask > 0, 255, 0), axis=-1)
        RGBA_mask: List[Any] = np.concatenate((R,G,B,A), axis=-1).astype(dtype=np.uint8)
        RGBA_mask: List[Any] = maskLabelColors(RGBA_mask=RGBA_mask, mask=self.mask)
        data['changed_volume_data'].changed_mask_volume = RGBA_mask

def settingMaskPallete(max) -> List[Any]:
    pallete: List[Any] = []
    for i in range(max):
        pallete.append(maskPallete(index=i))
    return pallete

def maskLabelColors(RGBA_mask: List[Any], mask: List[Any]) -> List[Any]:
    pallete: List[Any] = settingMaskPallete(max=mask.max())
    for label in pallete:
        RGBA_mask[:,:,:, 0] = np.where(mask == label["Number"], label["RGB"][0], RGBA_mask[:,:,:,0])
        RGBA_mask[:,:,:, 1] = np.where(mask == label["Number"], label["RGB"][1], RGBA_mask[:,:,:,1])
        RGBA_mask[:,:,:, 2] = np.where(mask == label["Number"], label["RGB"][2], RGBA_mask[:,:,:,2])
    del pallete
    return RGBA_mask

def setChannelsIntensity(volume: List[Any]) -> None:
    point: List[Any] = (np.array(volume.shape[-1:-4:-1][::-1])/2).astype(dtype=int)
    data['cursor_data'].current_point = point
    multichannel: bool = len(volume.shape) > 3
    if(multichannel):
        data['toolframe_data'].channel_intensity = str(list(volume[x, point[0], point[1], point[2]] for x in range(4)))
        data['original_volume_data'].num_of_channels = volume.shape[0]
    else:
        data['toolframe_data'].channel_intensity = str([volume[point[0], point[1], point[2]]])
        data['original_volume_data'].num_of_channels = 1