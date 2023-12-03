import importlib
from types import ModuleType
from typing import Any
models: ModuleType = importlib.import_module(name='micview.models.getters')
from micview.controllers.services.tools.cursor_tool import updateChannelsIntensity

def actionOnChild(* args: Any) -> None:
    if(models.states['toolframe_states'].selected_tool == "cursor"):
        updateChannelsIntensity()
    parent: object = models.views['objects_ref'].ImagesFrame
    child: int = models.states['image_canvas_states'].action_on_child
    if(child == 0):#click in axial
            parent.coronal.controller.eventHandler("action_on_child")
            parent.sagital.controller.eventHandler("action_on_child")
    elif(child == 1): #click in coronal
            parent.axial.controller.eventHandler("action_on_child")
            parent.sagital.controller.eventHandler("action_on_child")    
    elif(child == 2): #click in sagital
            parent.coronal.controller.eventHandler("action_on_child")
            parent.axial.controller.eventHandler("action_on_child")
    else:
            raise IndexError
        
def updateAllChilds(* args: Any) -> None:
    if(models.states['toolframe_states'].selected_tool == "cursor"):
        updateChannelsIntensity()
    parent: object = models.views['objects_ref'].ImagesFrame
    parent.coronal.controller.eventHandler("update_all_childs")
    parent.axial.controller.eventHandler("update_all_childs")
    parent.sagital.controller.eventHandler("update_all_childs")