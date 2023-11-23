import importlib
from types import ModuleType
from typing import Any
models: ModuleType = importlib.import_module(name='micview.models.getters')
from micview.controllers.services.tools.toolframe import Set_Tool

def channel_select_hook(* args: Any) -> None:
    if(models.states['loading_states'].image_is_loaded and not models.states['loading_states'].loading):
        models.states['image_canvas_states'].update_all_childs = True

def selected_tool_hook(* args: Any) -> None:
    tool: object = models.states['toolframe_states'].selected_tool
    master: object = models.views['objects_ref'].ToolFrame
    Set_Tool(tool=tool, master=master)

def tool_is_set_hook(* args: Any) -> None:
    if(models.states['toolframe_states'].tool_is_set):
        models.states['toolframe_states'].selected_tool = "cursor"
    else:
        del models.views['objects_ref'].ToolFrame
        models.states['toolframe_states'].selected_tool = "none"