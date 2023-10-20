from models.models import loading_states, objects_ref
from views.windows.toplevels.OpenImage import OpenImage
from views.windows.toplevels.OpenSegmentation import OpenSegmentation

def change_buttons_state(*args):
    image_is_loaded = loading_states.image_is_loaded
    menu = objects_ref.Menu
    state = "normal" if image_is_loaded else "disabled"
    menu.view_options.entryconfig("Original Size", state=state)        
    menu.view_options.entryconfig("Zoom To Fit", state=state)
    menu.file_options.entryconfig("Open Main Image", state=state)

def FileWindow():
    menu = objects_ref.Menu
    objects_ref.SideWindow = OpenImage(master=menu)
    
def SegmentationWindow():
    menu = objects_ref.Menu
    objects_ref.SideWindow = OpenSegmentation(master=menu)

def DelSideWindow():
    del objects_ref.SideWindow
