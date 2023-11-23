from typing import Any, Literal
from micview.models.getters import states, views
from micview.views.windows.toplevels.OpenImage import OpenImage
from micview.views.windows.toplevels.OpenSegmentation import OpenSegmentation

def handle_onLoading(loading: bool) -> None:
    menu: object = views['objects_ref'].Menu
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
        
def change_buttons_state(*args: Any) -> None:
    image_is_loaded: bool = states['loading_states'].image_is_loaded
    menu: object = views['objects_ref'].Menu
    state: Literal['normal', 'disabled'] = "normal" if image_is_loaded else "disabled"
    menu.view_options.entryconfig("Original Size", state=state)        
    menu.view_options.entryconfig("Zoom To Fit", state=state)
    menu.file_options.entryconfig("Open Main Image", state=state)

def update_radiobool() -> None:
    menu: object = views['objects_ref'].Menu
    state: bool = states['options_states'].image_is_square
    menu.radioboolvar.set(state)

def FileWindow() -> None:
    menu: object = views['objects_ref'].Menu
    views['objects_ref'].SideWindow = OpenImage(master=menu.master)
    
def SegmentationWindow() -> None:
    menu: object = views['objects_ref'].Menu
    views['objects_ref'].SideWindow = OpenSegmentation(master=menu.master)

def DelSideWindow() -> None:
    del views['objects_ref'].SideWindow
