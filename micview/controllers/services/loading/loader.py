from threading import Event, Thread
from micview.controllers.validations.validate_kwargs import checkKwargs
from micview.models.models import get_loading_states, get_options_states, get_changed_volume_data, get_original_volume_data, get_image_canvas_states
from micview.controllers.services.volume.loader import image_volume_loader, mask_volume_loader, image_and_mask_sync_loader
from micview.controllers.services.image_viewer.ImageFrameController import LoadingCircles, enable_all_canvas, disable_all_canvas

class loadImageFromShell(Thread):
    def __init__(self, **kwargs):
        self.params = checkKwargs(**kwargs)
        super().__init__(daemon=True)

    def run(self):
        get_loading_states().loading = True
        disable_all_canvas()
        self.event = Event()
        self.animation = LoadingCircles(self.event)
        self.animation.start()
        self.loading_process = image_and_mask_sync_loader(file=self.params["file"], order=self.params["order"], mask_file=self.params["mask"])
        self.loading_process.start()
        self.loading_process.join()
        self.event.set()
        self.animation.join()
        get_loading_states().image_is_loaded = True
        if(self.params["mask"] is not None):
            get_loading_states().mask_is_loaded = True
        get_options_states().image_is_square = self.params["resized"]
        get_options_states().mask_is_set = True
        enable_all_canvas()
        get_image_canvas_states().update_all_childs = True
        get_loading_states().loading =  False

class loadNewImage(Thread):
    def __init__(self, **kwargs):
        self.params = checkKwargs(**kwargs)
        super().__init__(daemon=True)

    def run(self):
        get_loading_states().loading = True
        delMask()
        delImage()
        disable_all_canvas()
        self.event = Event()
        self.animation = LoadingCircles(self.event)
        self.animation.start()
        self.loading_process = image_volume_loader(path=self.params["file"], order=self.params["order"])
        self.loading_process.start()
        self.loading_process.join()
        self.event.set()
        self.animation.join()
        get_loading_states().image_is_loaded = True
        get_options_states().image_is_square = self.params["resized"]
        enable_all_canvas()
        get_image_canvas_states().update_all_childs = True
        get_loading_states().loading =  False

class loadNewMask(Thread):
    def __init__(self, **kwargs):
        self.params = checkKwargs(**kwargs)
        super().__init__(daemon=True)

    def run(self):
        get_loading_states().loading = True
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
        get_loading_states().mask_is_loaded = True
        get_options_states().mask_is_set = True
        enable_all_canvas()
        get_image_canvas_states().update_all_childs = True
        get_loading_states().loading =  False

def delImage():
    get_loading_states().image_is_loaded = False
    del get_changed_volume_data().changed_image_volume
    del get_changed_volume_data().zoom_factors
    del get_original_volume_data().image_volume
    del get_original_volume_data().num_of_channels

def delMask():
    get_loading_states().mask_is_loaded = False
    get_options_states().mask_is_set = False
    del get_changed_volume_data().changed_mask_volume
    del get_original_volume_data().mask_volume