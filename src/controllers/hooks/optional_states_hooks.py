import importlib
models = importlib.import_module('src.models.models')

def image_is_square_hook(* args):
        print("image_is_square_hook")
        if(models.get_loading_states().image_is_loaded):
                models.get_image_canvas_states().action_on_child = 3
        #self.Loader.Controller.UpdateImageResetPoint()
        #self.toolframe.WatchToolsVar(self.toolvar.get())

def mask_is_set_hook(* args):
        print("mask_is_set_hook")
        if(models.get_loading_states().mask_is_loaded):
                models.get_image_canvas_states().action_on_child = 3