'''
Simple multiview visualization implementation
'''
import numpy as np
import cv2 as cv
import multiprocessing as mp
from scipy.ndimage import zoom
from tqdm import tqdm


current_point = None


def image_print(img, st, org=(20, 20), scale=1, color=1, font=cv.FONT_HERSHEY_SIMPLEX):
    '''
    Simplifies printing text on images
    '''
    if st is None:
        return img
    else:
        return cv.putText(img, str(st), org, font, scale, color)


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


def mouse_handler(event, x, y, flags, param):
    '''
    OpenCV mouse event handler
    '''
    global current_point

    if current_point is None:
        print("Using params point")
        current_point = param["point"]

    volume, window_name = param["volume"], param["window_name"]
    x = x//param["display_resize"]
    y = y//param["display_resize"]

    if ((event == cv.EVENT_LBUTTONDOWN or param["dragging"]) and param["previous_x"] != x and param["previous_y"] != y) or event == cv.EVENT_MBUTTONDOWN:

        window = param["get_current_window"][x]
        param["dragging"] = True
        param["previous_x"] = x
        param["previous_y"] = y

        current_point[window] += (flags == 4)*1 - (flags == 12)*1

        if window == 0:
            current_point = [current_point[0], y, x]
        elif window == 1:
            current_point = [y, current_point[1], x - param["cube_size"]]
        elif window == 2:
            current_point = [y, x - param["cube_size"]*2, current_point[2]]
        param["point"] = current_point

        if x is not None and y is not None:
            if param["channel"] > -1:
                volume = volume[param["channel"]]

            axis0 = np.copy(volume[current_point[0], :, :])
            axis1 = np.copy(volume[:, current_point[1], :])
            axis2 = np.copy(volume[:, :, current_point[2]])

            axis0 = image_print(axis0, current_point[0], org=(20, 30))
            axis0 = image_print(axis0, param["channel"], org=(20, 60))
            displayed_value = volume[current_point[0], current_point[1], current_point[2]]
            original_value = displayed_value*(param["max"] - param["min"]) + param["min"]
            axis0 = image_print(axis0, displayed_value, org=(20, 90))
            axis0 = image_print(axis0, original_value, org=(20, 120))
            axis1 = image_print(axis1, current_point[1], org=(20, 30))
            axis2 = image_print(axis2, current_point[2], org=(20, 30))

            axis0 = cv.circle(axis0, (current_point[2], current_point[1]), 2, 1)
            axis1 = cv.circle(axis1, (current_point[2], current_point[0]), 2, 1)
            axis2 = cv.circle(axis2, (current_point[1], current_point[0]), 2, 1)

            axis0 = cv.line(axis0, (0, current_point[1]), (param["cube_size"] - 1, current_point[1]), 1)
            axis0 = cv.line(axis0, (current_point[2], 0), (current_point[2], param["cube_size"] - 1), 1)

            axis1 = cv.line(axis1, (current_point[2], 0), (current_point[2], param["cube_size"] - 1), 1)
            axis1 = cv.line(axis1, (0, current_point[0]), (param["cube_size"] - 1, current_point[0]), 1)

            axis2 = cv.line(axis2, (current_point[1], 0), (current_point[1], param["cube_size"] - 1), 1)
            axis2 = cv.line(axis2, (0, current_point[0]), (param["cube_size"] - 1, current_point[0]), 1)

        display = np.hstack((axis0, axis1, axis2))
        cv.imshow(window_name, cv.resize(display, (0, 0), fx=param["display_resize"], fy=param["display_resize"]))
    elif event == cv.EVENT_LBUTTONUP:
        param["dragging"] = False


class MultiViewer():
    def __init__(self, volume, mask=None, normalize=False, window_name="MultiViewer", cube_side=200, resize_factor=2, order=3,
                 threaded=False):
        if len(volume.shape) == 4 and np.argmin(volume.shape) == 3:
            print("Channel dimension has to be 0, attempting transpose")
            volume = volume.transpose(3, 0, 1, 2)
            assert np.argmin(volume.shape) == 0, "Couldn't solve wrong dimension channel. Put channel on dimension 0."

        original_min = volume.min()
        original_max = volume.max()

        if normalize:
            self.volume = (volume - volume.min()) / (volume.max() - volume.min())
        else:
            self.volume = volume

        self.volume_shape = volume.shape

        multichannel = len(self.volume_shape) > 3
        self.multichannel = multichannel

        if multichannel:
            self.C = self.volume_shape[0]
            self.last_channel = 0

        if self.volume_shape != (cube_side, cube_side, cube_side):
            zoom_factors = (cube_side/self.volume_shape[-3], cube_side/self.volume_shape[-2], cube_side/self.volume_shape[-1])
            mask_zoom = zoom_factors

            if multichannel:
                self.volume = multi_channel_zoom(self.volume, zoom_factors, order=order, threaded=threaded, tqdm_on=False)
            else:
                self.volume = zoom(self.volume, zoom_factors, order=order)

        if mask is not None:
            zoomed_mask = zoom(mask, mask_zoom, order=0).astype(np.float32)
            zoomed_mask = (zoomed_mask - zoomed_mask.min())/(zoomed_mask.max() - zoomed_mask.min())
            self.masked_volume = np.where(zoomed_mask == 0, self.volume, zoomed_mask)
            self.original_volume = self.volume
            self.volume = self.masked_volume
            self.displaying_mask = True

        self.volume_shape = self.volume.shape
        assert self.volume_shape[-1:-4:-1][::-1] == (cube_side, cube_side, cube_side)

        self.current_point = (np.array(self.volume_shape[-1:-4:-1][::-1])/2).astype(int)
        self.window_name = window_name
        self.resize_factor = resize_factor

        get_current_window = np.concatenate((np.zeros(self.volume_shape[-3]),
                                             np.ones(self.volume_shape[-2]),
                                             2*np.ones(self.volume_shape[-1]))).astype(np.uint8)
        self.handler_param = {"get_current_window": get_current_window, "window_name": self.window_name, "volume": self.volume,
                              "point": self.current_point, "cube_size": cube_side, "previous_x": cube_side/2,
                              "previous_y": cube_side/2, "dragging": False, "display_resize": resize_factor,
                              "min": original_min, "max": original_max}

    def reset_current_point(self):
        global current_point
        current_point = None

    def display(self, channel_select=-1):
        global current_point

        self.last_channel = channel_select

        if current_point is None:
            current_point = self.current_point

        if channel_select < 0:
            axis0 = self.volume[current_point[0], :, :]
            axis1 = self.volume[:, current_point[1], :]
            axis2 = self.volume[:, :, current_point[2]]
        else:
            try:
                axis0 = self.volume[channel_select, current_point[0], :, :]
                axis1 = self.volume[channel_select, :, current_point[1], :]
                axis2 = self.volume[channel_select, :, :, current_point[2]]
            except IndexError:
                print(f"Channel {channel_select} not found. Using 0")
                self.last_channel = 0
                axis0 = self.volume[0, current_point[0], :, :]
                axis1 = self.volume[0, :, current_point[1], :]
                axis2 = self.volume[0, :, :, current_point[2]]

        self.handler_param["channel"] = channel_select
        cv.namedWindow(self.window_name)
        cv.setMouseCallback(self.window_name, mouse_handler, param=self.handler_param)
        cv.imshow(self.window_name, cv.resize(np.hstack((axis0, axis1, axis2)), (0, 0),
                                              fx=self.resize_factor, fy=self.resize_factor))
        key = cv.waitKey(0)
        if key == 27:
            return 'ESC'
        elif key == 13:
            return 'ENTER'
        elif key == 115:
            # Hide/show mask
            if self.displaying_mask:
                self.volume = self.original_volume
                self.displaying_mask = False
            else:
                self.volume = self.masked_volume
                self.displaying_mask = True
            self.handler_param["volume"] = self.volume

            return(self.display(channel_select=self.last_channel))
        elif self.multichannel:
            # Change displayed channel
            channel = key - 48

            if channel in range(self.C):
                return(self.display(channel_select=channel))
            else:
                return(self.display(channel_select=self.last_channel))


def brats_preparation(npz):
    '''
    Assumes npz with multichannel data and softmax target
    '''
    if npz["target"].shape[0] == 4:
        target = npz["target"][1:].astype(np.float32)  # discarding background
        for i, channel in enumerate(target):
            target[i] = (i+1)*channel/3
    elif npz["target"].shape[0] == 3:
        target = npz["target"].astype(np.float32)
        for i, channel in enumerate(target):
            target[i] = channel/3
    else:
        raise ValueError("Unsupported target for brats visualization preparation")

    target = target.sum(axis=0)
    data = npz["data"]
    return data, target


if __name__ == "__main__":
    print("Loading...")
    import argparse
    import SimpleITK as sitk

    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--input', type=str, required=True)
    args = parser.parse_args()

    npz_path = args.input

    if npz_path.endswith(".nii.gz"):
        image = sitk.GetArrayFromImage(sitk.ReadImage(npz_path))
        image = np.clip(image, a_min=-1024, a_max=600)
        image = (image - image.min())/(image.max() - image.min())
        MultiViewer(image).display(channel_select=-1)
    elif npz_path.split('.')[-1] == 'npz':
        npz = np.load(npz_path)
        data, target = brats_preparation(npz)
        print(data.shape, target.shape)
        MultiViewer(data, mask=target).display(channel_select=0 if len(data.shape) > 3 else -1)
    else:
        raise ValueError("File format not supported.")
