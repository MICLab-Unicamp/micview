from models.models import toolframe_states, objects_ref, loading_states, image_canvas_states
from services.tools.toolframe import Set_Tool

def channel_select_hook(* args):
    if(loading_states.image_is_loaded):
        image_canvas_states.action_on_child = 3

def selected_tool_hook(* args):
    print(args)
    tool = toolframe_states.selected_tool
    master = objects_ref.ToolFrame
    Set_Tool(tool, master)

def tool_is_set_hook(* args):
    if(toolframe_states.tool_is_set):
        toolframe_states.selected_tool = "cursor"
    else:
        del objects_ref.ToolFrame
        toolframe_states.selected_tool = "none"