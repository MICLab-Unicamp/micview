from typing import Any, Tuple, List
import numpy as np
from micview.models.getters import states, data

def changeCurrentPoint(axis0: int, axis1: int, axis2: int) -> None:
    current_point: Tuple[int] = data['cursor_data'].current_point
    if (axis0 >= 0):
        current_point[0] = axis0
    if (axis1 >= 0):
        current_point[1] = axis1
    if (axis2 >= 0):
        current_point[2] = axis2
    data['cursor_data'].current_point = current_point
    changeLabelUnderCursor(current_point)

def changeLabelUnderCursor(current_point: Tuple[int]) -> None:
    mask: List[Any] = data['original_volume_data'].mask_volume
    if mask is not None:
        data['cursor_data'].label_under_cursor = mask[current_point[0], current_point[1], current_point[2]]
    else:
        data['cursor_data'].label_under_cursor = 0

def getImageSlices(axis: int) -> List[Any]:
    channel_select: int = states['toolframe_states'].channel_select
    current_point: Tuple[int] = data['cursor_data'].current_point
    volume: List[Any] = data['changed_volume_data'].changed_image_volume
    if current_point is None:
        current_point = (np.array(volume.shape[-1:-4:-1][::-1])/2).astype(int)
        data['cursor_data'].current_point = current_point
    if data['original_volume_data'].num_of_channels == 1:
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
    current_point: Tuple[int] = data['cursor_data'].current_point
    mask: List[Any] = data['changed_volume_data'].changed_mask_volume
    if (axis == 0):
        return mask[current_point[0], :, :, :]
    elif (axis == 1):
        return mask[:, current_point[1], :, :]
    elif (axis == 2):
        return mask[:, :, current_point[2], :]
    else:
        raise IndexError
