import importlib
from types import ModuleType
from typing import Any
models: ModuleType = importlib.import_module(name='micview.models.getters')

def loading_hook(* args: Any) -> None:
    from micview.controllers.services.menu.callbacks_onclick import change_buttons_state, handle_onLoading, update_radiobool
    if(models.states['loading_states'].loading):
        if(models.states['toolframe_states'].tool_is_set):
            models.states['toolframe_states'].tool_is_set = False
        handle_onLoading(loading=True)

    else:
        if(models.states['loading_states'].image_is_loaded):
            models.states['toolframe_states'].tool_is_set = True
            models.states['image_canvas_states'].update_all_childs = True
        handle_onLoading(loading=False)
        change_buttons_state()
        update_radiobool()

