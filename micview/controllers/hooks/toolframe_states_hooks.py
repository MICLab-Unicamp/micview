##
#
# @brief: This file contains the hooks for the toolframe_states
#

# Imports
import importlib
from types import ModuleType
from typing import Any
models: ModuleType = importlib.import_module(name='micview.models.getters')
from micview.controllers.services.tools.toolframe import setTool

# Functions
def channelSelectHook(* args: Any) -> None:
    """!
        @brief: This function is called when the user clicks in one of the childs of the image canvas
        @param args: Any
        @return: None
    """
    if(models.states['loading_states'].image_is_loaded and not models.states['loading_states'].loading):
        models.states['image_canvas_states'].update_all_childs = True

def selectedToolHook(* args: Any) -> None:
    """!
    @brief: This function is called when the user clicks in one of the childs of the image canvas
    @param args: Any
    @return: None
    """
    tool: str = models.states['toolframe_states'].selected_tool
    models.states['toolframe_states'].paint_mode = False
    master: object = models.views['objects_ref'].ToolFrame
    setTool(tool=tool, master=master)
    models.states['image_canvas_states'].update_all_childs = True

def toolIsSetHook(* args: Any) -> None:
    """!
    @brief: This function is called when the user clicks in one of the childs of the image canvas
    @param args: Any
    @return: None
    """
    if(models.states['toolframe_states'].tool_is_set):
        models.states['toolframe_states'].selected_tool = "cursor"
    else:
        del models.views['objects_ref'].ToolFrame
        models.states['toolframe_states'].selected_tool = "none"

def transparencyLevelHook(* args: Any) -> None:
    """!
    @brief: This function is called when the user clicks in one of the childs of the image canvas
    @param args: Any
    @return: None
    """
    models.states['image_canvas_states'].update_all_childs = True

def zoomHook(* args: Any) -> None:
    """!
    @brief: This function is called when the user clicks in one of the childs of the image canvas
    @param args: Any
    @return: None
    """
    models.states['image_canvas_states'].update_all_childs = True

def paintHooks(* args: Any) -> None:
    """!
    @brief: This function is called when the user clicks in one of the childs of the image canvas
    @param args: Any
    @return: None
    """
    models.states['image_canvas_states'].update_all_childs = True
    