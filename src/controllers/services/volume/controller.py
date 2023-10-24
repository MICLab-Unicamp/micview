import numpy as np
import multiprocessing as mp
from scipy.ndimage import zoom
from src.models.models import get_original_volume_data, get_changed_volume_data, get_cursor_data, get_toolframe_states

def zoom_worker(x):
    channel, zoom_factor, order = x
    return zoom(channel, zoom_factor, order=order)


def multi_channel_zoom(full_volume, zoom_factors, order):
    '''
    full_volume: Full 4D volume (numpy)
    zoom_factors: intented shape / current shape
    order: 0 - 5, higher is slower but better results, 0 is fast and bad results
    C: how many cores to spawn, defaults to number of channels in volume
    '''
    assert len(full_volume.shape) == 4 and isinstance(full_volume, np.ndarray)

    C = full_volume.shape[0]
        
    pool = mp.Pool(C)
    channels = [(channel, zoom_factors, order) for channel in full_volume]

    zoomed_volumes = []

    pool_iter = pool.map(zoom_worker, channels)

    for output in pool_iter:
        zoomed_volumes.append(output)

    return np.stack(zoomed_volumes)

def change_current_point(axis0, axis1, axis2):
    current_point = get_cursor_data().current_point
    if(axis0 >=0):
        current_point[0] = axis0
    if(axis1 >=0):
        current_point[1] = axis1
    if(axis2 >=0):
        current_point[2] = axis2
    get_cursor_data().current_point = current_point
    change_current_point_original_vol()

def change_current_point_original_vol():
    zoom_factors = get_changed_volume_data().zoom_factors
    current_point = get_cursor_data().current_point
    current_point_original_vol = get_cursor_data().current_point_original_vol    
    interpolate = 1/np.array(zoom_factors)
    current_point_original_vol = current_point * interpolate
    for i in range(len(current_point_original_vol)):
         current_point_original_vol[i] = round(current_point_original_vol[i])
    
    current_point_original_vol = current_point_original_vol.astype(int)
    original_shape = get_original_volume_data().image_volume.shape
    n = 1 if len(original_shape) > 3 else 0
    if(current_point_original_vol[0] >= original_shape[n]): current_point_original_vol[0] -= 1 
    if(current_point_original_vol[1] >= original_shape[n+1]): current_point_original_vol[1] -= 1 
    if(current_point_original_vol[2] >= original_shape[n+2]): current_point_original_vol[2] -= 1 
    get_cursor_data().current_point_original_vol = current_point_original_vol

def get_image_slices(axis):
    channel_select = get_toolframe_states().channel_select
    current_point = get_cursor_data().current_point
    volume = get_changed_volume_data().changed_image_volume
    if current_point is None:
        current_point = (np.array(volume.shape[-1:-4:-1][::-1])/2).astype(int)
        get_cursor_data().current_point = current_point
        change_current_point_original_vol()

    if get_original_volume_data().num_of_channels == 1:
        match axis:
            case 0:
                return volume[current_point[0], :, :]
            case 1:
                return volume[:, current_point[1], :]
            case 2:
                return volume[:, :, current_point[2]]
            case _:
                raise LookupError #Revisar os erros padroes
    else:
        match axis:
            case 0:
                return volume[channel_select, current_point[0], :, :]
            case 1:
                return volume[channel_select, :, current_point[1], :]
            case 2:
                return volume[channel_select, :, :, current_point[2]]
            case _:
                raise LookupError #Revisar os erros padroes


def get_mask_slices(axis):
    current_point = get_cursor_data().current_point
    mask = get_changed_volume_data().changed_mask_volume
    match axis:
        case 0:
            return mask[current_point[0], :, :, :]
        case 1:
            return mask[:, current_point[1], :, :]
        case 2:
            return mask[:, :, current_point[2], :]
        case _:
            raise LookupError #Revisar os erros padroes