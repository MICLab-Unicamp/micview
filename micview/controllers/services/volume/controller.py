##
# @brief This file contains the controller functions for the volume data.
#

# Imports
from typing import Any, List
import numpy as np
import importlib
models = importlib.import_module(name='micview.models.getters')

# Functions
def changeCurrentPoint(axis0: int, axis1: int, axis2: int) -> None:
    """!
    @brief: This function is responsible for changing the current point of the cursor.
    @param: axis0: int - The value of the first axis.
    @param: axis1: int - The value of the second axis.
    @param: axis2: int - The value of the third axis.
    @return: None
    """
    current_point: "tuple[int]" = models.data['cursor_data'].current_point
    if (axis0 >= 0):
        current_point[0] = axis0
    if (axis1 >= 0):
        current_point[1] = axis1
    if (axis2 >= 0):
        current_point[2] = axis2
    models.data['cursor_data'].current_point = current_point
    models.views['objects_ref'].ImagesFrame.refreshSurface()
    changeLabelUnderCursor(current_point=current_point)

def changeLabelUnderCursor(current_point: "tuple[int]") -> None:
    """!
    @brief: This function is responsible for changing the label under the cursor.
    @param: current_point: tuple[int] - The current point of the cursor.
    @return: None
    """
    mask: List[Any] = models.data['original_volume_data'].mask_volume
    if mask is not None:
        models.data['cursor_data'].label_under_cursor = mask[current_point[0], current_point[1], current_point[2]]
    else:
        models.data['cursor_data'].label_under_cursor = 0

def changeVolumeContrast(min: int, max: int) -> None:    
    """!
    @brief: This function is responsible for changing the contrast of the volume.
    @param: min: int - The minimum value of the contrast.
    @param: max: int - The maximum value of the contrast.
    @return: None
    """
    original = models.data['original_volume_data'].image_volume
    clipped = np.zeros_like(original)
    original.clip(min, max, out=clipped)
    models.data['changed_volume_data'].changed_image_volume = ((clipped - min)*(255/(max - min))).astype(np.uint8)

def getImageSlices(axis: int) -> List[Any]:
    """!
    @brief: This function returns the slices of the image.
    @param: axis: int - The axis of the image.
    @return: List[Any]
    """
    channel_select: int = models.states['toolframe_states'].channel_select
    current_point: "tuple[int]" = models.data['cursor_data'].current_point
    volume: List[Any] = models.data['changed_volume_data'].changed_image_volume
    if current_point is None:
        current_point = (np.array(volume.shape[-1:-4:-1][::-1])/2).astype(int)
        models.data['cursor_data'].current_point = current_point
    if models.data['original_volume_data'].num_of_channels == 1:
        if (axis == 0):
            return volume[current_point[0], :, :]
        elif (axis == 1):
            return volume[:, current_point[1], :]
        elif (axis == 2):
            return volume[:, :, current_point[2]]
        else:
            raise IndexError
    else:
        if (axis == 0):
            return volume[channel_select, current_point[0], :, :]
        elif (axis == 1):
            return volume[channel_select, :, current_point[1], :]
        elif (axis == 2):
            return volume[channel_select, :, :, current_point[2]]
        else:
            raise IndexError


def getMaskSlices(axis: int) -> List[Any]:
    """!
    @brief: This function returns the slices of the mask.
    @param: axis: int - The axis of the mask.
    @return: List[Any]
    """
    current_point: "tuple[int]" = models.data['cursor_data'].current_point
    mask: List[Any] = models.data['changed_volume_data'].changed_mask_volume
    if (axis == 0):
        return mask[current_point[0], :, :, :]
    elif (axis == 1):
        return mask[:, current_point[1], :, :]
    elif (axis == 2):
        return mask[:, :, current_point[2], :]
    else:
        raise IndexError
