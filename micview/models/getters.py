import tkinter as tk
from micview.models.data.cursor_data import cursor_data_class
from micview.models.data.toolframe_data import toolframe_data_class
from micview.models.data.files_data import files_data_class
from micview.models.data.original_volume_data import original_volume_data_class
from micview.models.data.changed_volume_data import changed_volume_data_class
from micview.models.refs.objects_ref import objects_ref_class
from micview.models.states.image_canvas_states import image_canvas_states_class
from micview.models.states.loading_states import loading_states_class
from micview.models.states.toolframe_states import toolframe_states_class
from micview.models.states.options_states import options_states_class

data: "dict[str,str]" = dict()
views: "dict[str,str]" = dict()
states: "dict[str,str]" = dict()

def init_models(master: tk.Tk) -> None:
    """
    Initializes the models used in the application.

    Args:
        master (tk.Tk): The root Tkinter window.

    Returns:
        None
    """
    global data, views, states
    data['cursor_data'] = cursor_data_class()
    data['toolframe_data'] = toolframe_data_class()
    data['files_data'] = files_data_class()
    data['original_volume_data'] = original_volume_data_class()
    data['changed_volume_data'] = changed_volume_data_class()
    views['objects_ref'] = objects_ref_class()
    states['image_canvas_states'] = image_canvas_states_class(master=master)
    states['loading_states'] = loading_states_class(master=master)
    states['options_states'] = options_states_class(master=master)
    states['toolframe_states'] = toolframe_states_class(master=master)
    master.states = states
    master.views = views
    master.data = data