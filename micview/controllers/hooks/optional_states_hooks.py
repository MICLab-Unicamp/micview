import importlib
models = importlib.import_module('micview.models.models')

def image_is_square_hook(* args):
        if(models.get_loading_states().image_is_loaded and not models.get_loading_states().loading):
                models.get_image_canvas_states().update_all_childs = True

def mask_is_set_hook(* args):
        if(models.get_loading_states().mask_is_loaded and not models.get_loading_states().loading):
                models.get_image_canvas_states().update_all_childs = True
