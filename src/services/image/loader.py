from validations.validate_kwargs import checkKwargs
from globals.globals import loading_states
from services.metadatas.file_reader import readImageFile, readMaskFile

def loadImageFromShell(**kwargs):
    loading_states.set_loading(True)
    params = checkKwargs(**kwargs)
    ArrayFromImage = readImageFile(path=params["file"])
    ArrayFromMask = None
    if(len(params["mask"]) > 1):
        ArrayFromMask = readMaskFile(path=params["mask"])
        #Set loading states mask_is_loaded e optional states mask_is_set (na funcao)

    #vol_init        
    #set square image boolean
    #set cursor tool
    #set image is set
    #set mask is or isnt set
    #set loading false

def loadNewImage(**kwargs):
    #destruir imagem e mask antiga
    #image e mask is not loaded
    loading_states.set_loading(True)
    params = checkKwargs(**kwargs)

def loadNewMask(**kwargs):
    #destruir mask antiga
    #mask is not loaded
    loading_states.set_loading(True)
    params = checkKwargs(**kwargs)