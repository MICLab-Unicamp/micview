import numpy as np
from scipy.ndimage import zoom
import Components.Volume.Volume_Controller as Volctrl

class ImagesContainer():
    def __init__(self, volume, square_image_boolean=False, mask=None, window_name="MultiViewer", cube_side=200, resize_factor=1, order=0, clip=(-1024,600)):
        if len(volume.shape) == 4 and np.argmin(volume.shape) == 3:
            print("Channel dimension has to be 0, attempting transpose")
            volume = volume.transpose(3, 0, 1, 2)
            assert np.argmin(volume.shape) == 0, "Couldn't solve wrong dimension channel. Put channel on dimension 0."

        self.order = order
        self.mask = mask
        self.original_volume = volume 
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
        if(square_image_boolean):
            zoom_factors = (cube_side/self.volume_shape[-3], cube_side/self.volume_shape[-2], cube_side/self.volume_shape[-1])
        else:
            zoom_factors = (cube_side/self.max_side, cube_side/self.max_side, cube_side/self.max_side)
        
        mask_zoom = zoom_factors
        if multichannel:
            self.volume = Volctrl.multi_channel_zoom(self.volume, zoom_factors, order=order, tqdm_on=False)
        else:
            self.volume = zoom(self.volume, zoom_factors, order=order)

        self.volume = np.clip(self.volume, a_min=clip[0], a_max=clip[1])
        self.volume = self.volume - self.volume.min()
        self.volume = (self.volume * (255/self.volume.max())).astype(np.uint8)

        if mask is not None:
            zoomed_mask = Volctrl.zoom(mask, mask_zoom, order=0).astype(np.float32)
            zoomed_mask = (zoomed_mask - zoomed_mask.min())/(zoomed_mask.max() - zoomed_mask.min())
            self.masked_volume = np.where(zoomed_mask == 0, self.volume, zoomed_mask)
            self.original_volume = self.volume
            self.volume = self.masked_volume
            self.displaying_mask = True

        self.volume_shape = self.volume.shape

        self.current_point = (np.array(self.volume_shape[-1:-4:-1][::-1])/2).astype(int)
        self.window_name = window_name
        self.resize_factor = zoom_factors

        self.handler_param = {"window_name": self.window_name, "original_volume": self.original_volume,
                              "point": self.current_point, "cube_size": cube_side, "initial_x": cube_side/2,
                              "initial_y": cube_side/2, "dragging": False, "display_resize": resize_factor,
                              "min": original_min, "max": original_max}