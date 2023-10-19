from globals.globals import loading_states, objects_ref 
from windows.side_windows.OpenImage import OpenImage
from windows.side_windows.OpenSegmentation import OpenSegmentation

def change_buttons_state(*args):
    image_is_loaded = loading_states.get_image_is_loaded()
    menu = objects_ref.get_Menu()
    state = "normal" if image_is_loaded else "disabled"
    menu.view_options.entryconfig("Original Size", state=state)        
    menu.view_options.entryconfig("Zoom To Fit", state=state)
    menu.file_options.entryconfig("Open Main Image", state=state)

def FileWindow():
    menu = objects_ref.get_Menu()
    objects_ref.set_SideWindow(OpenImage(master=menu))
    
def SegmentationWindow():
    menu = objects_ref.get_Menu()
    objects_ref.set_SideWindow(OpenSegmentation(master=menu))

def DelSideWindow():
    objects_ref.del_SideWindow()