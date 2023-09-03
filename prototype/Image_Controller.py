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

def display(volume, handler_param, resize_factor=2, channel_select=-1):
        global current_point

        last_channel = channel_select

        if current_point is None:
            current_point = (np.array(volume.shape[-1:-4:-1][::-1])/2).astype(int)

        if channel_select < 0:
            axis0 = volume[current_point[0], :, :]
            axis1 = volume[:, current_point[1], :]
            axis2 = volume[:, :, current_point[2]]
        else:
            try:
                axis0 = volume[channel_select, current_point[0], :, :]
                axis1 = volume[channel_select, :, current_point[1], :]
                axis2 = volume[channel_select, :, :, current_point[2]]
            except IndexError:
                print(f"Channel {channel_select} not found. Using 0")
                last_channel = 0
                axis0 = volume[0, current_point[0], :, :]
                axis1 = volume[0, :, current_point[1], :]
                axis2 = volume[0, :, :, current_point[2]]

        handler_param["channel"] = channel_select
        stacked_array =np.hstack((axis0, axis1, axis2))
        stacked_array = (stacked_array - stacked_array.min())
        stacked_array = stacked_array * (255/stacked_array.max())
        resized_array = Image.fromarray(cv.resize(stacked_array, (0, 0), fx=resize_factor, fy=resize_factor), mode='F')
        return resized_array