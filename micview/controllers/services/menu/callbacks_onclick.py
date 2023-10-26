from micview.models.models import get_loading_states, get_objects_ref, get_options_states
from micview.views.windows.toplevels.OpenImage import OpenImage
from micview.views.windows.toplevels.OpenSegmentation import OpenSegmentation

def handle_onLoading(loading):
    menu = get_objects_ref().Menu
    if(loading):
        menu.entryconfig("File", state="disabled")
        menu.entryconfig("View", state="disabled")
        menu.entryconfig("Segmentation", state="disabled")
        menu.entryconfig("Edit", state="disabled")
        menu.entryconfig("Tools", state="disabled")
    else:
        menu.entryconfig("File", state="normal")
        menu.entryconfig("View", state="normal")
        menu.entryconfig("Segmentation", state="normal")
        menu.entryconfig("Edit", state="normal")
        menu.entryconfig("Tools", state="normal")
        
def change_buttons_state(*args):
    image_is_loaded = get_loading_states().image_is_loaded
    menu = get_objects_ref().Menu
    state = "normal" if image_is_loaded else "disabled"
    menu.view_options.entryconfig("Original Size", state=state)        
    menu.view_options.entryconfig("Zoom To Fit", state=state)
    menu.file_options.entryconfig("Open Main Image", state=state)

def update_radiobool():
    menu = get_objects_ref().Menu
    state = get_options_states().image_is_square
    menu.radioboolvar.set(state)

def FileWindow():
    menu = get_objects_ref().Menu
    get_objects_ref().SideWindow = OpenImage(master=menu.master)
    
def SegmentationWindow():
    menu = get_objects_ref().Menu
    get_objects_ref().SideWindow = OpenSegmentation(master=menu.master)

def DelSideWindow():
    del get_objects_ref().SideWindow
