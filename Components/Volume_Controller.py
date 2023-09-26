import numpy as np
import multiprocessing as mp
from scipy.ndimage import zoom
from tqdm import tqdm
import math

current_point = None

def zoom_worker(x):
    channel, zoom_factor, order = x
    return zoom(channel, zoom_factor, order=order)


def multi_channel_zoom(full_volume, zoom_factors, order, C=None, tqdm_on=True):
    '''
    full_volume: Full 4D volume (numpy)
    zoom_factors: intented shape / current shape
    order: 0 - 5, higher is slower but better results, 0 is fast and bad results
    C: how many cores to spawn, defaults to number of channels in volume
    tqdm_on: verbose computation
    '''
    assert len(full_volume.shape) == 4 and isinstance(full_volume, np.ndarray)

    if C is None:
        C = full_volume.shape[0]
        
    pool = mp.Pool(C)
    channels = [(channel, zoom_factors, order) for channel in full_volume]

    zoomed_volumes = []

    pool_iter = pool.map(zoom_worker, channels)
    if tqdm_on:
        iterator = tqdm(pool_iter, total=len(channels), desc="Computing zooms...")
    else:
        iterator = pool_iter

    for output in iterator:
        zoomed_volumes.append(output)

    return np.stack(zoomed_volumes)

def reset_current_point():
    global current_point
    current_point = None

def change_current_point(axis0, axis1, axis2):
    global current_point
    if(axis0 >=0):
        current_point[0] = axis0
    if(axis1 >=0):
        current_point[1] = axis1
    if(axis2 >=0):
        current_point[2] = axis2

def get_2D_slices(image, channel_select=-1):
        global current_point
        print(f"Image volume shape: {image.volume.shape}")
        if current_point is None:
            current_point = (np.array(image.volume.shape[-1:-4:-1][::-1])/2).astype(int)
            image.handler_param["point"] = current_point

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
                print(f"Channel {channel_select} not found. Using 0")
                channel_select = 0
                axis0 = image.volume[0, current_point[0], :, :]
                axis1 = image.volume[0, :, current_point[1], :]
                axis2 = image.volume[0, :, :, current_point[2]]

        image.handler_param["channel"] = channel_select
        Image_2D_slices = [axis0,axis1,axis2]
        return Image_2D_slices

def ImageResizing(image,new_cube_size):
        sides = np.array(list(image.volume_shape))
        max_side = sides.max()
        new_sizes = {
             "axis0_x": math.floor((new_cube_size/max_side)*sides[1]),
             "axis0_y": math.floor((new_cube_size/max_side)*sides[2]),
             "axis1_x": math.floor((new_cube_size/max_side)*sides[2]),
             "axis1_y": math.floor((new_cube_size/max_side)*sides[0]),
             "axis2_x": math.floor((new_cube_size/max_side)*sides[1]),
             "axis2_y": math.floor((new_cube_size/max_side)*sides[0])
        }
        return new_sizes