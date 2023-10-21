from src.models.data.cursor_data import *
from src.models.data.toolframe_data import *
from src.models.data.files_data import *
from src.models.data.original_volume_data import *
from src.models.data.changed_volume_data import *
from src.models.refs.objects_ref import *
from src.models.states.image_canvas_states import *
from src.models.states.loading_states import *
from src.models.states.toolframe_states import *
from src.models.states.options_states import *

cursor_data = False
toolframe_data = False
files_data = False
original_volume_data = False
changed_volume_data = False
objects_ref = False
image_canvas_states = False
loading_states = False
options_states = False
toolframe_states = False

get_cursor_data = lambda : cursor_data
get_toolframe_data = lambda : toolframe_data
get_files_data = lambda : files_data
get_original_volume_data = lambda : original_volume_data
get_changed_volume_data = lambda : changed_volume_data
get_objects_ref = lambda : objects_ref
get_image_canvas_states = lambda : image_canvas_states
get_loading_states = lambda : loading_states
get_options_states = lambda : options_states
get_toolframe_states = lambda : toolframe_states

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