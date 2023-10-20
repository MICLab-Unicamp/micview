from validations.validate_kwargs import checkKwargs
from models.models import loading_states, options_states, changed_volume_data, original_volume_data
from controllers.services.files.file_reader import readImageFile, readMaskFile
from controllers.services.volume.loader import image_volume_loader, mask_volume_loader

def loadImageFromShell(**kwargs):
    loading_states.loading = True
    params = checkKwargs(**kwargs)
    ArrayFromImage = readImageFile(path=params["file"])
    image_volume_loader(ArrayFromImage)
    loading_states.image_is_loaded = True
    options_states.image_is_square = params["resized"]
    
    if(len(params["mask"]) > 1):
        ArrayFromMask = readMaskFile(path=params["mask"])
        mask_volume_loader(ArrayFromMask)
        loading_states.mask_is_loaded = True
        options_states.mask_is_set = True
    
    loading_states.loading = False

def loadNewImage(**kwargs):
    loading_states.loading = True
    delMask()
    delImage()
    params = checkKwargs(**kwargs)
    ArrayFromImage = readImageFile(path=params["file"])
    image_volume_loader(ArrayFromImage)
    loading_states.image_is_loaded = True
    options_states.image_is_square = params["resized"]
    loading_states.loading = False

def loadNewMask(**kwargs):
    loading_states.loading = True
    delMask()
    params = checkKwargs(**kwargs)
    ArrayFromMask = readMaskFile(path=params["mask"])
    mask_volume_loader(ArrayFromMask)
    loading_states.mask_is_loaded = True
    options_states.mask_is_set = True
    loading_states.loading = False

def delImage():
    loading_states.image_is_loaded = False
    del changed_volume_data.changed_image_volume
    del changed_volume_data.zoom_factors
    del original_volume_data.image_volume
    del original_volume_data.num_of_channels

def delMask():
    del changed_volume_data.changed_mask_volume
    del original_volume_data.mask_volume