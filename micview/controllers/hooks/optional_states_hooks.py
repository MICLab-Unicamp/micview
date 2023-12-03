import importlib
from types import ModuleType
models: ModuleType = importlib.import_module(name='micview.models.getters')

def imageIsSquareHook(* args: None) -> None:
        if(models.states['loading_states'].image_is_loaded and not models.states['loading_states'].loading):
                models.states['image_canvas_states'].update_all_childs = True

def maskIsSetHook(* args: None) -> None:
        if(models.states['loading_states'].mask_is_loaded and not models.states['loading_states'].loading):
                models.states['image_canvas_states'].update_all_childs = True
