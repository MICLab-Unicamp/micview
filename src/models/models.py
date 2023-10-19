from infos.cursor_infos import *
from infos.toolframe_infos import *
from infos.volume_infos import *
from infos.files_infos import *
from refs.objects_ref import *
from states.loading_states import *
from models.states.options_states import *
from states.toolframe_states import *

cursor_infos = None
toolframe_infos = None
volume_infos = None
files_infos = None
objects_ref = None
loading_states = None
optional_states = None
toolframe_states = None

def init_models(master):
    global cursor_infos, toolframe_infos, volume_infos, files_infos
    global objects_ref
    global loading_states, optional_states, toolframe_states
    cursor_infos = cursor_infos_class(master)
    toolframe_infos = toolframe_infos_class(master)
    volume_infos = volume_infos_class(master)
    files_infos = files_infos_class(master)
    objects_ref = objects_ref_class(master)
    loading_states = loading_states_class(master)
    optional_states = optional_states_class(master)
    toolframe_states = toolframe_states_class(master)