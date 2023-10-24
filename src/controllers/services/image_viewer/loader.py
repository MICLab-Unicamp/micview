from threading import Thread
from src.controllers.validations.validate_kwargs import checkKwargs
from src.models.models import get_loading_states, get_options_states, get_changed_volume_data, get_original_volume_data
from src.controllers.services.volume.loader import image_volume_loader, mask_volume_loader, image_and_mask_sync_loader

def loadImageFromShell(**kwargs):
    get_loading_states().loading = True
    params = checkKwargs(**kwargs)
    image_and_mask_sync_loader(file=params["file"], order=params["order"], image_is_square=params["resized"], mask_file=params["mask"]).start()

def loadNewImage(**kwargs):
    get_loading_states().loading = True
    delMask()
    delImage()
    params = checkKwargs(**kwargs)
    image_volume_loader(path=params["file"], order=params["order"], image_is_square=params["resized"]).start()

def loadNewMask(**kwargs):
    get_loading_states().loading = True
    delMask()
    params = checkKwargs(**kwargs)
    mask_volume_loader(path=params["mask"]).start()

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