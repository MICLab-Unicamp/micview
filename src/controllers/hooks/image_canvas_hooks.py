import importlib
models = importlib.import_module('src.models.models')
from src.controllers.services.tools.cursor_tool import update_channels_intensity

def action_on_child(* args):
    if(models.get_toolframe_states().tool_is_set):
        update_channels_intensity()
    parent = models.get_objects_ref().ImagesFrame
    child = models.get_image_canvas_states().action_on_child
    match child:
        case 0: #click in axial
            parent.coronal.controller.event_handler()
            parent.sagital.controller.event_handler()
        case 1: #click in coronal
            parent.axial.controller.event_handler()
            parent.sagital.controller.event_handler()    
        case 2: #click in sagital
            parent.coronal.controller.event_handler()
            parent.axial.controller.event_handler()
        case 3: #change in all of 3
            parent.coronal.controller.event_handler()
            parent.axial.controller.event_handler()         
            parent.sagital.controller.event_handler()
        case _:
            raise Exception ###################