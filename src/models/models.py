from data.cursor_data import *
from data.toolframe_data import *
from data.files_data import *
from data.original_volume_data import *
from data.changed_volume_data import *
from refs.objects_ref import *
from states.image_canvas_states import *
from states.loading_states import *
from states.toolframe_states import *
from states.options_states import *

cursor_data = None
toolframe_data = None
files_data = None
original_volume_data = None
changed_volume_data = None
objects_ref = None
image_canvas_states = None
loading_states = None
options_states = None
toolframe_states = None

def init_models(master):
    global cursor_data, toolframe_data, files_data, original_volume_data, changed_volume_data
    global objects_ref
    global image_canvas_states, loading_states, options_states, toolframe_states
    cursor_data = cursor_data_class()
    toolframe_data = toolframe_data_class(master)
    files_data = files_data_class()
    original_volume_data = original_volume_data_class(master)
    changed_volume_data = changed_volume_data_class()
    objects_ref = objects_ref_class()
    image_canvas_states = image_canvas_states_class(master)
    loading_states = loading_states_class(master)
    options_states = options_states_class(master)
    toolframe_states = toolframe_states_class(master)