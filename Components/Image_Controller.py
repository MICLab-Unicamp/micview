import numpy as np
import multiprocessing as mp
from scipy.ndimage import zoom
from tqdm import tqdm
import cv2 as cv
from PIL import Image

current_point = None

def zoom_worker(x):
    channel, zoom_factor, order = x
    return zoom(channel, zoom_factor, order=order)


def multi_channel_zoom(full_volume, zoom_factors, order, C=None, tqdm_on=True, threaded=False):
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
    if threaded:
        pool = mp.pool.ThreadPool(C)
    else:
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

def update_POV(image, channel_select=-1):
        global current_point

        last_channel = channel_select

        if current_point is None:
            current_point = (np.array(image.volume.shape[-1:-4:-1][::-1])/2).astype(int)

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
                last_channel = 0
                axis0 = image.volume[0, current_point[0], :, :]
                axis1 = image.volume[0, :, current_point[1], :]
                axis2 = image.volume[0, :, :, current_point[2]]

        image.handler_param["channel"] = channel_select
        Axisarray = [axis0,axis1,axis2]
        Imagearray = []
        for axis in Axisarray:
            axis = np.clip(axis, a_min=-1024, a_max=600)
            axis = (axis - axis.min())
            axis = axis * (255/axis.max())
            axis = Image.fromarray(axis, mode='F')
            Imagearray.append(axis)
        return Imagearray

def ImageResizing(image,new_cube_size):
        zoom_factors = (new_cube_size/image.volume_shape[-3], new_cube_size/image.volume_shape[-2], new_cube_size/image.volume_shape[-1])
        mask_zoom = zoom_factors
        if image.multichannel:
            image.volume = multi_channel_zoom(image.volume, zoom_factors, order=image.order, threaded=image.threaded, tqdm_on=False)
        else:
            image.volume = zoom(image.volume, zoom_factors, order=image.order)

        if image.mask is not None:
            zoomed_mask = zoom(image.mask, mask_zoom, order=0).astype(np.float32)
            zoomed_mask = (zoomed_mask - zoomed_mask.min())/(zoomed_mask.max() - zoomed_mask.min())
            image.masked_volume = np.where(zoomed_mask == 0, image.volume, zoomed_mask)
            image.original_volume = image.volume
            image.volume = image.masked_volume
            image.displaying_mask = True
            image.handler_param["volume"] = image.volume
            image.handler_param["cube_size"] = new_cube_size

        global current_point
        current_point = (np.array(image.volume.shape[-1:-4:-1][::-1])/2).astype(int)
        
        return image