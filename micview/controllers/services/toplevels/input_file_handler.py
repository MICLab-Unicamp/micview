##
# @brief: This file contains the functions that handle the input file window
#

# Imports
import tkinter.filedialog as fd
import os
from typing import List
from micview.models.getters import views, data

# Functions
def browseFileHandler() -> None:
    """!
    @brief: This function is responsible for handling the browse file button.
    @return: None
    """
    window: object = views['objects_ref'].SideWindow
    window.withdraw()
    actualdir = data['toolframe_data'].dirpath
    name: str = fd.askopenfilename(initialdir= actualdir if(len(actualdir)>0) else "./", title="Select File", filetypes= (("NiFTI files","*.nii.gz"),("DICOM files","*.dcm") ,("all files","*.*")))
    if(type(name) != str):
        window.deiconify()
        return
    aux: List[str] = name.split('/')
    filepath: str = aux[-1]
    currentdirectory: str = "/".join(aux[:-1])
    if(len(filepath) > 0 and len(currentdirectory) > 0):
        window.currentdirectory.set(currentdirectory)
        data['toolframe_data'].dirpath = currentdirectory
        window.filepath.set(filepath)
    window.deiconify()

def browseDirHandler() -> None:
    """!
    @brief: This function is responsible for handling the browse directory button.
    @return: None
    """
    window: object = views['objects_ref'].SideWindow
    window.withdraw()
    actualdir = data['toolframe_data'].dirpath
    name: str = fd.askdirectory(initialdir= actualdir if(len(actualdir)>0) else "./", title="Select Directory")
    if(type(name) != str):
        window.deiconify()
        return
    aux: List[str] = name.split('/')
    filepath: str = aux[-1]
    currentdirectory: str = "/".join(aux[:-1])
    if(len(filepath) > 0 and len(currentdirectory) > 0):
        window.currentdirectory.set(currentdirectory)
        data['toolframe_data'].dirpath = currentdirectory
        window.filepath.set(filepath)
    window.deiconify()

def callbackCurrentDir(*args: None) -> None:
    """!
    @brief: This function is responsible for handling the current directory callback.
    @return: None
    """
    window: object = views['objects_ref'].SideWindow
    window.pathtextvariable.set(f"Path: {window.currentdirectory.get()}")

def callbackFilePath(*args: None) -> None:
    """!
    @brief: This function is responsible for handling the file path callback.
    @return: None
    """
    window: object = views['objects_ref'].SideWindow
    path: str = window.filepath.get()
    if(path == ""):
        window.warning.set("")
        window.openbutton['state'] = "disabled"
    else:
        path_split: List[str] = path.split('.')
        if((len(path_split) > 2 and path_split[-1] == "gz" and path_split[-2] == "nii") or (len(path_split) > 1 and path_split[-1] == "dcm")):
            finalpath: str = window.currentdirectory.get()+"/"+path
            if(os.path.exists(path=finalpath)):
                window.finalpath = finalpath
                window.warning.set("")
                window.openbutton['state'] = "normal"
            else:
                window.warning.set("File not found")
                window.openbutton['state'] = "disabled"
        else:
            finalpath: str = window.currentdirectory.get()+"/"+path
            if(os.path.exists(path=finalpath) and os.path.isdir(finalpath)):
                window.finalpath = finalpath
                window.warning.set("")
                window.openbutton['state'] = "normal"
            else:
                window.warning.set("File format not suported")
                window.openbutton['state'] = "disabled"

def resizedImageHandler(*args: None) -> None:
    """!
    @brief: This function is responsible for handling the resized image checkbox.
    @return: None
    """
    window: object = views['objects_ref'].SideWindow
    value: str = window.image_format.get()
    if(value == "Normal"):
        window.resized_image.set(False)
    else:
        window.resized_image.set(True)
    
def onClosing() -> None:
    """!
    @brief: This function is responsible for handling the closing of the window.
    @return: None
    """
    from micview.controllers.services.menu.callbacks_onclick import delSideWindow
    window: object = views['objects_ref'].SideWindow
    window.filepath.trace_remove("write", window.traceid1)
    window.currentdirectory.trace_remove("write", window.traceid2)
    window.destroy()
    window.update()
    delSideWindow()