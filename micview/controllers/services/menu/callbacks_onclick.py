from micview.models.getters import states, views
from micview.views.windows.toplevels.OpenImage import OpenImage
from micview.views.windows.toplevels.OpenSegmentation import OpenSegmentation

def handle_onLoading(loading):
    menu = views['objects_ref'].Menu
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
    image_is_loaded = states['loading_states'].image_is_loaded
    menu = views['objects_ref'].Menu
    state = "normal" if image_is_loaded else "disabled"
    menu.view_options.entryconfig("Original Size", state=state)        
    menu.view_options.entryconfig("Zoom To Fit", state=state)
    menu.file_options.entryconfig("Open Main Image", state=state)

def update_radiobool():
    menu = views['objects_ref'].Menu
    state = states['options_states'].image_is_square
    menu.radioboolvar.set(state)

def FileWindow():
    menu = views['objects_ref'].Menu
    views['objects_ref'].SideWindow = OpenImage(master=menu.master)
    
def SegmentationWindow():
    menu = views['objects_ref'].Menu
    views['objects_ref'].SideWindow = OpenSegmentation(master=menu.master)

def DelSideWindow():
    del views['objects_ref'].SideWindow
