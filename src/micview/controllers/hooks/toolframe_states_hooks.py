import importlib
models = importlib.import_module('src.micview.models.getters')
from src.micview.controllers.services.tools.toolframe import Set_Tool

def channel_select_hook(* args):
    if(models.states['loading_states'].image_is_loaded and not models.states['loading_states'].loading):
        models.states['image_canvas_states'].update_all_childs = True

def selected_tool_hook(* args):
    tool = models.states['toolframe_states'].selected_tool
    master = models.views['objects_ref'].ToolFrame
    Set_Tool(tool, master)

def tool_is_set_hook(* args):
    if(models.states['toolframe_states'].tool_is_set):
        models.states['toolframe_states'].selected_tool = "cursor"
    else:
        del models.views['objects_ref'].ToolFrame
        models.states['toolframe_states'].selected_tool = "none"