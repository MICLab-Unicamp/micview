from src.models.models import get_loading_states, get_objects_ref
from src.views.windows.toplevels.OpenImage import OpenImage
from src.views.windows.toplevels.OpenSegmentation import OpenSegmentation

def change_buttons_state(*args):
    image_is_loaded = get_loading_states().image_is_loaded
    menu = get_objects_ref().Menu
    state = "normal" if image_is_loaded else "disabled"
    menu.view_options.entryconfig("Original Size", state=state)        
    menu.view_options.entryconfig("Zoom To Fit", state=state)
    menu.file_options.entryconfig("Open Main Image", state=state)

def FileWindow():
    menu = get_objects_ref().Menu
    print(f"menu: {menu}")
    get_objects_ref().SideWindow = OpenImage(master=menu)
    print(get_objects_ref().Menu)
    
def SegmentationWindow():
    menu = get_objects_ref().Menu
    get_objects_ref().SideWindow = OpenSegmentation(master=menu)

def DelSideWindow():
    del get_objects_ref().SideWindow
