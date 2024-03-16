##
# @brief: This file contains the loader for the image and mask volumes.
#

# Imports
import tkinter as tk
import os
from typing import Any, List
import numpy as np
from threading import Thread
from micview.controllers.services.volume.maskPallete import maskPallete
from micview.models.getters import data
from micview.controllers.services.files.file_reader import readImageFile, readMaskFile

# Classes
class ImageAndMaskSyncLoader(Thread):
    """!
    @brief: This class is responsible for loading the image and mask volumes.
    """
    def __init__(self, file: str, mask_file: str=None, array: bool=False) -> None:
        """!
        @brief: The constructor of the class.
        @param: file: str - The path of the image volume.
        @param: mask_file: str - The path of the mask volume.
        @param: array: bool - The array state of the volume.
        """
        super().__init__(daemon=True)
        self.file: str = file
        self.mask_file: str = mask_file
        self.array: bool = array    
    def run(self) -> None:
        """!
        @brief: The run method of the class.
        @return: None
        """
        self.image_loader_thread = ImageVolumeLoader(path=self.file, array=self.array)
        self.image_loader_thread.start()
        self.image_loader_thread.join()
        if(self.mask_file is not None):
            self.mask_loader_thread = MaskVolumeLoader(path=self.mask_file, array=self.array)
            self.mask_loader_thread.start()
            self.mask_loader_thread.join()

class ImageVolumeLoader(Thread):
    """!
    @brief: This class is responsible for loading the image volume.
    """
    def __init__(self, path: str, array: bool=False) -> None:
        """!
        @brief: The constructor of the class.
        @param: path: str - The path of the image volume.
        @param: array: bool - The array state of the volume.
        """
        super().__init__(daemon=True)
        self.path: str = path
        self.array: bool = array

    def run(self) -> None:
        """!
        @brief: The run method of the class.
        @return: None
        """
        del data['original_volume_data'].mask_volume
        del data['changed_volume_data'].changed_mask_volume
        data['cursor_data'].label_under_cursor = 0
        del data['original_volume_data'].image_volume
        del data['changed_volume_data'].changed_image_volume        
        if(self.array):
            data['files_data'].flipped_axes = (False, False, False)
            data['files_data'].orient_text = dict({0: False, 1: False, 2: False})
            self.volume: List[Any] = np.load(self.path + '.npy')
            os.unlink(self.path)
        else:
            self.volume: List[Any] = readImageFile(path=self.path)
        if len(self.volume.shape) == 4 and np.argmin(self.volume.shape) == 3:
            self.volume = self.volume.transpose(3, 0, 1, 2)
            assert np.argmin(self.volume.shape) == 0, "Couldn't solve wrong dimension channel. Put channel on dimension 0."
        data['original_volume_data'].image_volume = self.volume
        data['original_volume_data'].min_and_max_values = (self.volume.min(), self.volume.max())
        data['changed_volume_data'].min_and_max_values = (self.volume.min(), self.volume.max())
        setChannelsIntensity(volume=self.volume)
        self.volume = ((self.volume - self.volume.min())*(255/(self.volume.max() - self.volume.min()))).astype(np.uint8)
        data['changed_volume_data'].changed_image_volume = self.volume
        
class MaskVolumeLoader(Thread):
    """!
    @brief: This class is responsible for loading the mask volume.
    """
    def __init__(self, path: str, array: bool=False) -> None:
        """!
        @brief: The constructor of the class.
        @param: path: str - The path of the mask volume.
        @param: array: bool - The array state of the volume.
        @return: None
        """
        super().__init__(daemon=True)
        self.path: str = path
        self.array: bool = array

    def run(self) -> None:
        """!
        @brief: The run method of the class.
        @return: None
        """
        del data['original_volume_data'].mask_volume
        del data['changed_volume_data'].changed_mask_volume
        if(self.array):
            self.mask: List[Any] = np.load(self.path + '.npy')
            os.unlink(self.path)
        else:
            self.mask: List[Any] = readMaskFile(path=self.path)
            if(self.mask is not None):
                data['original_volume_data'].mask_volume = self.mask
                setLabelUnderCursor(mask=self.mask)
                R: List[Any] = np.expand_dims(np.zeros_like(self.mask), axis=-1).astype(dtype=np.uint8)
                G: List[Any] = np.zeros_like(R)
                B: List[Any] = np.zeros_like(R)
                A: List[Any] = np.expand_dims(np.where(self.mask > 0, 255, 0), axis=-1)
                RGBA_mask: List[Any] = np.concatenate((R,G,B,A), axis=-1).astype(dtype=np.uint8)
                RGBA_mask: List[Any] = maskLabelColors(RGBA_mask=RGBA_mask, mask=self.mask)
                data['changed_volume_data'].changed_mask_volume = RGBA_mask
                data['changed_volume_data'].pre_edit_changed_mask_volume = RGBA_mask.copy()

def settingMaskPallete(max) -> List[Any]:
    """!
    @brief: This function returns a list of colors for the mask.
    @param max: int - The maximum number of labels.
    @return: List[Any]
    """
    pallete: List[Any] = []
    for i in range(max):
        pallete.append(maskPallete(index=i))
    return pallete

def maskLabelColors(RGBA_mask: List[Any], mask: List[Any]) -> List[Any]:
    """!
    @brief: This function returns the mask with the colors.
    @param RGBA_mask: List[Any] - The mask with the colors.
    @param mask: List[Any] - The mask.
    @return: List[Any]
    """
    pallete: List[Any] = settingMaskPallete(max=mask.max())
    for label in pallete:
        RGBA_mask[:,:,:, 0] = np.where(mask == label["Number"], label["RGB"][0], RGBA_mask[:,:,:,0])
        RGBA_mask[:,:,:, 1] = np.where(mask == label["Number"], label["RGB"][1], RGBA_mask[:,:,:,1])
        RGBA_mask[:,:,:, 2] = np.where(mask == label["Number"], label["RGB"][2], RGBA_mask[:,:,:,2])
    del pallete
    return RGBA_mask

def setChannelsIntensity(volume: List[Any]) -> None:
    """!
    @brief: This function sets the channels intensity.
    @param volume: List[Any] - The volume.
    @return: None
    """
    point: List[Any] = (np.array(volume.shape[-1:-4:-1][::-1])/2).astype(dtype=int)
    data['cursor_data'].current_point = point
    multichannel: bool = len(volume.shape) > 3
    if(multichannel):
        data['toolframe_data'].channel_intensity = str(list(volume[x, point[0], point[1], point[2]] for x in range(4)))
        data['original_volume_data'].num_of_channels = volume.shape[0]
    else:
        data['toolframe_data'].channel_intensity = str([volume[point[0], point[1], point[2]]])
        data['original_volume_data'].num_of_channels = 1

def setLabelUnderCursor(mask: List[Any]) -> None:
    """!
    @brief: This function sets the label under the cursor.
    @param mask: List[Any] - The mask.
    @return: None
    """
    point: List[Any] = (np.array(mask.shape[-1:-4:-1][::-1])/2).astype(dtype=int)
    data['cursor_data'].current_point = point
    data['cursor_data'].label_under_cursor = str(mask[point[0], point[1], point[2]])