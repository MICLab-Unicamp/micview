##
# @brief: This file initializes the models used in the application.
#

# Imports
import tkinter as tk
from micview.models.data.cursor_data import CursorDataClass
from micview.models.data.toolframe_data import ToolframeDataClass
from micview.models.data.files_data import FilesDataClass
from micview.models.data.original_volume_data import OriginalVolumeDataClass
from micview.models.data.changed_volume_data import ChangedVolumeDataClass
from micview.models.refs.objects_ref import ObjectsRefClass
from micview.models.states.image_canvas_states import ImageCanvasStatesClass
from micview.models.states.loading_states import LoadingStatesClass
from micview.models.states.toolframe_states import ToolframeStatesClass
from micview.models.states.options_states import OptionsStatesClass

data: "dict[str,str]" = dict()
views: "dict[str,str]" = dict()
states: "dict[str,str]" = dict()

# Functions
def initModels(master: tk.Tk) -> None:
    """!
    @brief: This function initializes the models used in the application.
    @param: master: tk.Tk - The master window of the application.
    @return: None
    """
    global data, views, states
    data['cursor_data'] = CursorDataClass()
    data['toolframe_data'] = ToolframeDataClass()
    data['files_data'] = FilesDataClass()
    data['original_volume_data'] = OriginalVolumeDataClass()
    data['changed_volume_data'] = ChangedVolumeDataClass()
    views['objects_ref'] = ObjectsRefClass()
    states['image_canvas_states'] = ImageCanvasStatesClass(master=master)
    states['loading_states'] = LoadingStatesClass(master=master)
    states['options_states'] = OptionsStatesClass(master=master)
    states['toolframe_states'] = ToolframeStatesClass(master=master)
    master.states = states
    master.views = views
    master.data = data