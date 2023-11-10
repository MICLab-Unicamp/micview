from micview.models.data.cursor_data import *
from micview.models.data.toolframe_data import *
from micview.models.data.files_data import *
from micview.models.data.original_volume_data import *
from micview.models.data.changed_volume_data import *
from micview.models.refs.objects_ref import *
from micview.models.states.image_canvas_states import *
from micview.models.states.loading_states import *
from micview.models.states.toolframe_states import *
from micview.models.states.options_states import *

data = dict()
views = dict()
states = dict()

def init_models(master):
    global data, views, states
    data['cursor_data'] = cursor_data_class()
    data['toolframe_data'] = toolframe_data_class()
    data['files_data'] = files_data_class()
    data['original_volume_data'] = original_volume_data_class()
    data['changed_volume_data'] = changed_volume_data_class()
    views['objects_ref'] = objects_ref_class()
    states['image_canvas_states'] = image_canvas_states_class(master)
    states['loading_states'] = loading_states_class(master)
    states['options_states'] = options_states_class(master)
    states['toolframe_states'] = toolframe_states_class(master)
    master.states = states
    master.views = views
    master.data = data