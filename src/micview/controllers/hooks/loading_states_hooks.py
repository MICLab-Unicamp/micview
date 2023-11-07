import importlib
models = importlib.import_module('src.micview.models.getters')

def loading_hook(* args):
    from src.micview.controllers.services.menu.callbacks_onclick import change_buttons_state, handle_onLoading, update_radiobool
    if(models.states['loading_states'].loading):
        if(models.states['toolframe_states'].tool_is_set):
            models.states['toolframe_states'].tool_is_set = False
        handle_onLoading(True)

    else:
        if(models.states['loading_states'].image_is_loaded):
            models.states['toolframe_states'].tool_is_set = True
        handle_onLoading(False)
        change_buttons_state()
        update_radiobool()
