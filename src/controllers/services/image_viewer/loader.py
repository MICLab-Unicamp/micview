from src.controllers.validations.validate_kwargs import checkKwargs
from src.models.models import get_loading_states, get_options_states, get_changed_volume_data, get_original_volume_data
from src.controllers.services.files.file_reader import readImageFile, readMaskFile
from src.controllers.services.volume.loader import image_volume_loader, mask_volume_loader

def loadImageFromShell(**kwargs):
    get_loading_states().loading = True
    params = checkKwargs(**kwargs)
    ArrayFromImage = readImageFile(path=params["file"])
    image_volume_loader(ArrayFromImage)
    get_loading_states().image_is_loaded = True
    get_options_states().image_is_square = params["resized"]
    
    if(len(params["mask"]) > 1):
        ArrayFromMask = readMaskFile(path=params["mask"])
        mask_volume_loader(ArrayFromMask)
        get_loading_states().mask_is_loaded = True
        get_options_states().mask_is_set = True
    
    get_loading_states().loading = False

def loadNewImage(**kwargs):
    get_loading_states().loading = True
    delMask()
    delImage()
    params = checkKwargs(**kwargs)
    ArrayFromImage = readImageFile(path=params["file"])
    image_volume_loader(ArrayFromImage)
    get_loading_states().image_is_loaded = True
    get_options_states().image_is_square = params["resized"]
    get_loading_states().loading = False

def loadNewMask(**kwargs):
    get_loading_states().loading = True
    delMask()
    params = checkKwargs(**kwargs)
    ArrayFromMask = readMaskFile(path=params["mask"])
    mask_volume_loader(ArrayFromMask)
    get_loading_states().mask_is_loaded = True
    get_options_states().mask_is_set = True
    get_loading_states().loading = False

def delImage():
    get_loading_states().image_is_loaded = False
    del get_changed_volume_data().changed_image_volume
    del get_changed_volume_data().zoom_factors
    del get_original_volume_data().image_volume
    del get_original_volume_data().num_of_channels

def delMask():
    del get_changed_volume_data().changed_mask_volume
    del get_original_volume_data().mask_volume