from globals.globals import toolframe_states, objects_ref, loading_states
from services.tools.toolframe import Set_Tool

def channel_select_hook(* args):
    if(loading_states.get_image_is_loaded()):
         #self.loader.controller.updateimage
        pass

def selected_tool_hook(* args):
    tool = toolframe_states.get_selected_tool()
    if(tool != "none"):
        master = objects_ref.get_ToolFrame()
        Set_Tool(tool, master)

def tool_is_set_hook(* args):
    if(toolframe_states.get_tool_is_set()):
        toolframe_states.set_selected_tool("cursor")
    else:
        objects_ref.get_ToolFrame().del_actual_tool()
        toolframe_states.set_selected_tool("none")