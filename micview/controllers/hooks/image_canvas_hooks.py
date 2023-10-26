import importlib
models = importlib.import_module('micview.models.models')
from micview.controllers.services.tools.cursor_tool import update_channels_intensity

def action_on_child(* args):
    if(models.get_toolframe_states().selected_tool == "cursor"):
        update_channels_intensity()
    parent = models.get_objects_ref().ImagesFrame
    child = models.get_image_canvas_states().action_on_child
    if(child == 0):#click in axial
            parent.coronal.controller.event_handler("action_on_child")
            parent.sagital.controller.event_handler("action_on_child")
    elif(child == 1): #click in coronal
            parent.axial.controller.event_handler("action_on_child")
            parent.sagital.controller.event_handler("action_on_child")    
    elif(child == 2): #click in sagital
            parent.coronal.controller.event_handler("action_on_child")
            parent.axial.controller.event_handler("action_on_child")
    else:
            raise Exception ###################
        
def update_all_childs(* args):
    if(models.get_toolframe_states().selected_tool == "cursor"):
        update_channels_intensity()
    parent = models.get_objects_ref().ImagesFrame
    parent.coronal.controller.event_handler("update_all_childs")
    parent.axial.controller.event_handler("update_all_childs")
    parent.sagital.controller.event_handler("update_all_childs")