import numpy as np
import multiprocessing as mp
from scipy.ndimage import zoom
import math

current_point = None
current_point_original_vol = None

def zoom_worker(x):
    channel, zoom_factor, order = x
    return zoom(channel, zoom_factor, order=order)


def multi_channel_zoom(full_volume, zoom_factors, order, C=None):
    '''
    full_volume: Full 4D volume (numpy)
    zoom_factors: intented shape / current shape
    order: 0 - 5, higher is slower but better results, 0 is fast and bad results
    C: how many cores to spawn, defaults to number of channels in volume
    '''
    assert len(full_volume.shape) == 4 and isinstance(full_volume, np.ndarray)

    if C is None:
        C = full_volume.shape[0]
        
    pool = mp.Pool(C)
    channels = [(channel, zoom_factors, order) for channel in full_volume]

    zoomed_volumes = []

    pool_iter = pool.map(zoom_worker, channels)

    for output in pool_iter:
        zoomed_volumes.append(output)

    return np.stack(zoomed_volumes)

def reset_current_point():
    global current_point
    global current_point_original_vol
    current_point = None
    current_point_original_vol = None

def get_current_point():
     global current_point
     return current_point

def get_original_vol_current_point():
    global current_point_original_vol
    return current_point_original_vol

def change_current_point(axis0, axis1, axis2, image):
    global current_point
    if(axis0 >=0):
        current_point[0] = axis0
    if(axis1 >=0):
        current_point[1] = axis1
    if(axis2 >=0):
        current_point[2] = axis2
    image.handler_param["point"] = current_point
    change_current_point_original_vol(image)

def change_current_point_original_vol(image):
    global current_point
    global current_point_original_vol
    interpolate = 1/np.array(image.handler_param["display_resize"])
    current_point_original_vol = current_point * interpolate
    for i in range(len(current_point_original_vol)):
         current_point_original_vol[i] = round(current_point_original_vol[i])
    current_point_original_vol = current_point_original_vol.astype(int)
    original_shape = image.handler_param["original_volume"].shape
    n = 1 if len(original_shape) > 3 else 0
    if(current_point_original_vol[0] >= original_shape[n]): current_point_original_vol[0] -= 1 
    if(current_point_original_vol[1] >= original_shape[n+1]): current_point_original_vol[1] -= 1 
    if(current_point_original_vol[2] >= original_shape[n+2]): current_point_original_vol[2] -= 1 
    image.handler_param["point_original_vol"] = current_point_original_vol

def get_image_slices(image, channel_select):
    global current_point
    if current_point is None:
        current_point = (np.array(image.volume.shape[-1:-4:-1][::-1])/2).astype(int)
        image.handler_param["point"] = current_point
        change_current_point_original_vol(image)

    if channel_select < 0:
        axis0 = image.volume[current_point[0], :, :]
        axis1 = image.volume[:, current_point[1], :]
        axis2 = image.volume[:, :, current_point[2]]
    else:
        try:
            axis0 = image.volume[channel_select, current_point[0], :, :]
            axis1 = image.volume[channel_select, :, current_point[1], :]
            axis2 = image.volume[channel_select, :, :, current_point[2]]

        except IndexError:
            channel_select = 0
            axis0 = image.volume[0, current_point[0], :, :]
            axis1 = image.volume[0, :, current_point[1], :]
            axis2 = image.volume[0, :, :, current_point[2]]

    image.handler_param["channel"] = channel_select
    Image_2D_slices = [axis0,axis1,axis2]
    return Image_2D_slices

def get_mask_slices(image):
    global current_point
    axis0 = image.mask[current_point[0], :, :, :]
    axis1 = image.mask[:, current_point[1], :, :]
    axis2 = image.mask[:, :, current_point[2], :]
    Mask_2D_slices = [axis0,axis1,axis2]
    return Mask_2D_slices    

def get_2D_slices(image, channel_select=-1, show_mask=True):
    image_slices = get_image_slices(image, channel_select)
    if(show_mask):
        mask_slices = get_mask_slices(image)
        return image_slices, mask_slices
    return image_slices


def ImageResizing(image,new_cube_size, channel_select):
        n = 1 if channel_select > -1 else 0
        sides = np.array(list(image.volume_shape))
        max_side = sides.max()
        new_sizes = {
             "axis0_x": math.floor((new_cube_size/max_side)*sides[n+1]),
             "axis0_y": math.floor((new_cube_size/max_side)*sides[n+2]),
             "axis1_x": math.floor((new_cube_size/max_side)*sides[n+2]),
             "axis1_y": math.floor((new_cube_size/max_side)*sides[n+0]),
             "axis2_x": math.floor((new_cube_size/max_side)*sides[n+1]),
             "axis2_y": math.floor((new_cube_size/max_side)*sides[n+0])
        }
        return new_sizes