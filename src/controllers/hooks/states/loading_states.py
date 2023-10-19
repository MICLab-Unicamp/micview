from globals.globals import loading_states, toolframe_states

def loading_hook(* args):
    pass
#self.menuframe.change_buttons_state()

def image_is_loaded_hook(* args):
    if(loading_states.get_image_is_loaded()):
        toolframe_states.set_tool_is_set(False)

def mask_is_loaded_hook(* args):
    pass