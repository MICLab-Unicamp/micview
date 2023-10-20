from models.models import toolframe_states, loading_states

def loading_hook(* args):
    print(args)
    if(loading_states.loading):
        loading_states.image_is_loaded = False
        loading_states.mask_is_loaded = False
        ##disable image_viewer, menu, and toolframe

def image_is_loaded_hook(* args):
    if(loading_states.image_is_loaded):
        toolframe_states.tool_is_set = True
        #enable some tools
    else:
        toolframe_states.tool_is_set = False
        #disable some tools

def mask_is_loaded_hook(* args):
    if(loading_states.mask_is_loaded):
        pass
        #enable some tools
    else:
        pass
        #diable some tools