from models.models import loading_states, image_canvas_states, options_states

def image_is_square_hook(* args):
        if(loading_states.image_is_loaded):
                image_canvas_states.action_on_child = 3
        #self.Loader.Controller.UpdateImageResetPoint()
        #self.toolframe.WatchToolsVar(self.toolvar.get())

def mask_is_set_hook(* args):
        print(args)
        if(loading_states.mask_is_loaded):
                image_canvas_states.action_on_child = 3