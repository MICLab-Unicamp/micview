from threading import Event, Thread
from micview.controllers.validations.validate_kwargs import checkKwargs
from micview.models.getters import states, data
from micview.controllers.services.volume.loader import image_volume_loader, mask_volume_loader, image_and_mask_sync_loader
from micview.controllers.services.image_viewer.ImageFrameController import LoadingCircles, enable_all_canvas, disable_all_canvas

class loadImageFromShell(Thread):
    def __init__(self, **kwargs):
        self.params = checkKwargs(**kwargs)
        super().__init__(daemon=True)

    def run(self):
        states['loading_states'].loading = True
        disable_all_canvas()
        self.event = Event()
        self.animation = LoadingCircles(self.event)
        self.animation.start()
        self.loading_process = image_and_mask_sync_loader(file=self.params["file"], mask_file=self.params["mask"])
        self.loading_process.start()
        self.loading_process.join()
        self.event.set()
        self.animation.join()
        states['loading_states'].image_is_loaded = True
        if(self.params["mask"] is not None):
            states['loading_states'].mask_is_loaded = True
            states['options_states'].mask_is_set = True
        states['options_states'].image_is_square = self.params["resized"]
        enable_all_canvas()
        states['loading_states'].loading =  False

class loadNewImage(Thread):
    def __init__(self, **kwargs):
        self.params = checkKwargs(**kwargs)
        self.loading_process = None
        super().__init__(daemon=True)

    def run(self):
        states['loading_states'].loading = True
        delMask()
        delImage()
        disable_all_canvas()
        self.event = Event()
        self.animation = LoadingCircles(self.event)
        self.animation.start()
        self.loading_process = image_volume_loader(path=self.params["file"])
        self.loading_process.start()
        self.loading_process.join()
        self.event.set()
        self.animation.join()
        states['loading_states'].image_is_loaded = True
        states['options_states'].image_is_square = self.params["resized"]
        enable_all_canvas()
        states['loading_states'].loading =  False

class loadNewMask(Thread):
    def __init__(self, **kwargs):
        self.params = checkKwargs(**kwargs)
        super().__init__(daemon=True)

    def run(self):
        states['loading_states'].loading = True
        delMask()
        disable_all_canvas()
        self.event = Event()
        self.animation = LoadingCircles(self.event)
        self.animation.start()
        self.loading_process = mask_volume_loader(path=self.params["mask"])
        self.loading_process.start()
        self.loading_process.join()
        self.event.set()
        self.animation.join()
        states['loading_states'].mask_is_loaded = True
        states['options_states'].mask_is_set = True
        enable_all_canvas()
        states['loading_states'].loading =  False

def delImage():
    states['loading_states'].image_is_loaded = False
    del data['changed_volume_data'].changed_image_volume
    del data['original_volume_data'].image_volume
    del data['original_volume_data'].num_of_channels

def delMask():
    states['loading_states'].mask_is_loaded = False
    states['options_states'].mask_is_set = False
    del data['changed_volume_data'].changed_mask_volume
    del data['original_volume_data'].mask_volume