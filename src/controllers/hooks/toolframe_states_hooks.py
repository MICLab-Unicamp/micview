import importlib
models = importlib.import_module('src.models.models')
from src.controllers.services.tools.toolframe import Set_Tool

def channel_select_hook(* args):
    print("channel_select_hook")
    if(models.get_loading_states().image_is_loaded):
        models.get_image_canvas_states().action_on_child = 3

def selected_tool_hook(* args):
    print("selected_tool_hook")
    tool = models.get_toolframe_states().selected_tool
    master = models.get_objects_ref().ToolFrame
    Set_Tool(tool, master)

def tool_is_set_hook(* args):
    print("tool_is_set_hook")
    if(models.get_toolframe_states().tool_is_set):
        models.get_toolframe_states().selected_tool = "cursor"
    else:
        del models.get_objects_ref().ToolFrame
        models.get_toolframe_states().selected_tool = "none"