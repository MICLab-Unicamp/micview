import importlib
models = importlib.import_module('src.models.models')

def loading_hook(* args):
    print("loading_hook")
    if(models.get_loading_states().loading):
        models.get_loading_states().image_is_loaded = False
        models.get_loading_states().mask_is_loaded = False
        ##disable image_viewer, menu, and toolframe

def image_is_loaded_hook(* args):
    print("image_is_loaded_hook")
    if(models.get_loading_states().image_is_loaded):
        models.get_toolframe_states().tool_is_set = True
        #enable some tools
    else:
        models.get_toolframe_states().tool_is_set = False
        #disable some tools

def mask_is_loaded_hook(* args):
    print("mask_is_loaded_hook")
    if(models.get_loading_states().mask_is_loaded):
        pass
        #enable some tools
    else:
        pass
        #diable some tools