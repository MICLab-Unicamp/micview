import importlib
models = importlib.import_module('src.models.models')

def loading_hook(* args):
    from src.controllers.services.menu.callbacks_onclick import change_buttons_state, handle_onLoading, update_radiobool
    if(models.get_loading_states().loading):
        if(models.get_toolframe_states().tool_is_set):
            models.get_toolframe_states().tool_is_set = False
        handle_onLoading(True)

    else:
        if(models.get_loading_states().image_is_loaded):
            models.get_toolframe_states().tool_is_set = True
        handle_onLoading(False)
        change_buttons_state()
        update_radiobool()
