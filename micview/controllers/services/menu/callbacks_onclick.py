##
# @brief: This file contains the callback functions for the menu options.
#

# Imports
from typing import Any, Literal
from tkinter import messagebox
from micview.models.getters import states, views, data
from micview.views.windows.toplevels.Metadata import Metadata
from micview.views.windows.toplevels.OpenImage import OpenImage
from micview.views.windows.toplevels.OpenSegmentation import OpenSegmentation
from micview.views.windows.toplevels.Info import Info

# Functions
def handleOnLoading(loading: bool) -> None:
    """!
    @brief: This function is responsible for handling the menu options when the application is loading.
    @param: loading: bool - The loading state of the application.
    @return: None
    """
    menu: object = views['objects_ref'].Menu
    if(loading):
        menu.entryconfig("File", state="disabled")
        menu.entryconfig("View", state="disabled")
        menu.entryconfig("Segmentation", state="disabled")
        menu.entryconfig("Tools", state="disabled")
        menu.entryconfig("Info", state="disabled")
    else:
        menu.entryconfig("File", state="normal")
        menu.entryconfig("View", state="normal")
        menu.entryconfig("Segmentation", state="normal")
        menu.entryconfig("Tools", state="normal")
        if(data["files_data"].image_metadatas is not None):
            menu.entryconfig("Info", state="normal")
        
def changeButtonsState(*args: Any) -> None:
    """!
    @brief: This function is responsible for changing the state of the buttons in the menu.
    @param: *args: Any - The arguments of the function.
    @return: None
    """
    image_is_loaded: bool = states['loading_states'].image_is_loaded
    menu: object = views['objects_ref'].Menu
    state: Literal['normal', 'disabled'] = "normal" if image_is_loaded else "disabled"
    menu.view_options.entryconfig("Original Size", state=state)        
    menu.view_options.entryconfig("Zoom To Fit", state=state)
    menu.file_options.entryconfig("Open Main Image", state=state)

def updateRadiobool() -> None:
    """!
    @brief: This function is responsible for updating the radiobool state of the menu.
    @return: None
    """
    menu: object = views['objects_ref'].Menu
    state: bool = states['options_states'].image_is_square
    menu.radioboolvar.set(state)

def fileWindow() -> None:
    """!
    @brief: This function is responsible for opening the file window.
    @return: None
    """
    menu: object = views['objects_ref'].Menu
    views['objects_ref'].SideWindow = OpenImage(master=menu.master)
    
def segmentationWindow() -> None:
    """!
    @brief: This function is responsible for opening the segmentation window.
    @return: None
    """
    menu: object = views['objects_ref'].Menu
    views['objects_ref'].SideWindow = OpenSegmentation(master=menu.master)

def delSideWindow() -> None:
    """!
    @brief: This function is responsible for deleting the side window.
    @return: None
    """
    del views['objects_ref'].SideWindow

def setToolCursor() -> None:
    """!
    @brief: This function is responsible for setting the tool to cursor.
    @return: None
    """
    states['toolframe_states'].selected_tool = "cursor"

def setToolZoom() -> None:
    """!
    @brief: This function is responsible for setting the tool to zoom.
    @return: None
    """
    states['toolframe_states'].selected_tool = "zoom"

def setToolContrast() -> None:
    """!
    @brief: This function is responsible for setting the tool to contrast.
    @return: None
    """
    states['toolframe_states'].selected_tool = "contrast"

def setToolEdit() -> None:
    """!
    @brief: This function is responsible for setting the tool to edit.
    @return: None
    """
    if(states['loading_states'].mask_is_loaded is False):
        messagebox.showwarning("Warning", "Load a mask first!")
    else:
        states['toolframe_states'].selected_tool = "edit"

def setImageInfo() -> None:
    """!
    @brief: This function is responsible for setting the image info.
    @return: None
    """
    menu: object = views['objects_ref'].Menu
    views['objects_ref'].SideWindow = Info(master=menu.master, windowtitle="Main Image Info")

def setImageMetadata() -> None:
    """!
    @brief: This function is responsible for setting the image metadata.
    @return: None
    """
    menu: object = views['objects_ref'].Menu
    views['objects_ref'].SideWindow = Metadata(master=menu.master)