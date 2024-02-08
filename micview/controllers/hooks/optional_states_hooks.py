##
# @brief: This file contains the hooks for the optional states.
#

# Imports
import importlib
from types import ModuleType
models: ModuleType = importlib.import_module(name='micview.models.getters')

# Functions
def imageIsSquareHook(* args: None) -> None:
        """!
        @brief: This function is called when the image is square
        @param args: None
        @return: None
        """
        if(models.states['loading_states'].image_is_loaded and not models.states['loading_states'].loading):
                models.states['image_canvas_states'].update_all_childs = True

def maskIsSetHook(* args: None) -> None:
        """!
        @brief: This function is called when the mask is set
        @param args: None
        @return: None
        """
        if(models.states['loading_states'].mask_is_loaded and not models.states['loading_states'].loading):
                models.states['image_canvas_states'].update_all_childs = True
