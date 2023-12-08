import array
from typing import Any, Dict
from threading import Event, Thread
from micview.controllers.validations.validate_kwargs import checkKwargs
from micview.models.getters import states, data
from micview.controllers.services.volume.loader import ImageVolumeLoader, MaskVolumeLoader, ImageAndMaskSyncLoader
from micview.controllers.services.image_viewer.ImageFrameController import LoadingCircles, enableAllCanvas, disableAllCanvas

class LoadImageFromShell(Thread):
    def __init__(self, **kwargs: Dict[str, Any]) -> None:
        self.params: Dict[str, Any] = checkKwargs(**kwargs)
        super().__init__(daemon=True)

    def run(self) -> None:
        states['loading_states'].loading = True
        disableAllCanvas()
        self.event = Event()
        self.animation = LoadingCircles(event=self.event)
        self.animation.start()
        self.loading_process = ImageAndMaskSyncLoader(file=self.params["file"], mask_file=self.params["mask"], array=self.params["array"])
        self.loading_process.start()
        self.loading_process.join()
        self.event.set()
        self.animation.join()
        states['loading_states'].image_is_loaded = True
        if(self.params["mask"] is not None):
            states['loading_states'].mask_is_loaded = True
            states['options_states'].mask_is_set = True
        states['options_states'].image_is_square = self.params["resized"]
        enableAllCanvas()
        states['loading_states'].loading =  False

class LoadNewImage(Thread):
    def __init__(self, **kwargs: Dict[str, Any]) -> None:
        self.params: Dict[str, Any] = checkKwargs(**kwargs)
        self.loading_process = None
        super().__init__(daemon=True)

    def run(self) -> None:
        states['loading_states'].loading = True
        delMask()
        delImage()
        disableAllCanvas()
        self.event = Event()
        self.animation = LoadingCircles(event=self.event)
        self.animation.start()
        self.loading_process = ImageVolumeLoader(path=self.params["file"])
        self.loading_process.start()
        self.loading_process.join()
        self.event.set()
        self.animation.join()
        states['loading_states'].image_is_loaded = True
        states['options_states'].image_is_square = self.params["resized"]
        enableAllCanvas()
        states['loading_states'].loading =  False

class LoadNewMask(Thread):
    def __init__(self, **kwargs: Dict[str, Any]) -> None:
        self.params: Dict[str, Any] = checkKwargs(**kwargs)
        super().__init__(daemon=True)

    def run(self) -> None:
        states['loading_states'].loading = True
        delMask()
        disableAllCanvas()
        self.event = Event()
        self.animation = LoadingCircles(event=self.event)
        self.animation.start()
        self.loading_process = MaskVolumeLoader(path=self.params["mask"])
        self.loading_process.start()
        self.loading_process.join()
        self.event.set()
        self.animation.join()
        states['loading_states'].mask_is_loaded = True
        states['options_states'].mask_is_set = True
        enableAllCanvas()
        states['loading_states'].loading =  False

def delImage() -> None:
    states['loading_states'].image_is_loaded = False
    del data['changed_volume_data'].changed_image_volume
    del data['original_volume_data'].image_volume
    del data['original_volume_data'].num_of_channels

def delMask() -> None:
    states['loading_states'].mask_is_loaded = False
    states['options_states'].mask_is_set = False
    del data['changed_volume_data'].changed_mask_volume
    del data['original_volume_data'].mask_volume