import numpy as np
import Components.Image_Controller as Imctrl

class ImagesContainer():
    def __init__(self, volume, mask=None, window_name="MultiViewer", cube_side=300, resize_factor=2, order=3, threaded=False):
        if len(volume.shape) == 4 and np.argmin(volume.shape) == 3:
            print("Channel dimension has to be 0, attempting transpose")
            volume = volume.transpose(3, 0, 1, 2)
            assert np.argmin(volume.shape) == 0, "Couldn't solve wrong dimension channel. Put channel on dimension 0."

        self.order = order
        self.threaded = threaded
        self.mask = mask

        original_min = volume.min()
        original_max = volume.max()
        self.volume = volume
        self.volume_shape = volume.shape

        multichannel = len(self.volume_shape) > 3
        self.multichannel = multichannel

        if multichannel:
            self.C = self.volume_shape[0]
            self.last_channel = 0
        
        sides = np.array(list(self.volume.shape))
        self.max_side = sides.max()
        
        zoom_factors = (cube_side/self.volume_shape[-3], cube_side/self.volume_shape[-2], cube_side/self.volume_shape[-1])
        mask_zoom = zoom_factors
        if multichannel:
            self.volume = Imctrl.multi_channel_zoom(self.volume, zoom_factors, order=order, threaded=threaded, tqdm_on=False)
        else:
            self.volume = Imctrl.zoom(self.volume, zoom_factors, order=order)

        if mask is not None:
            zoomed_mask = Imctrl.zoom(mask, mask_zoom, order=0).astype(np.float32)
            zoomed_mask = (zoomed_mask - zoomed_mask.min())/(zoomed_mask.max() - zoomed_mask.min())
            self.masked_volume = np.where(zoomed_mask == 0, self.volume, zoomed_mask)
            self.original_volume = self.volume
            self.volume = self.masked_volume
            self.displaying_mask = True

        self.volume_shape = self.volume.shape

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