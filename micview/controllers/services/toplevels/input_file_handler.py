import tkinter.filedialog as fd
import os
from typing import List
from micview.models.getters import views

def browseFileHandler() -> None:
        window: object = views['objects_ref'].SideWindow
        window.withdraw()
        name: str = fd.askopenfilename(initialdir="./", title="Select File", filetypes= (("NiFTI files","*.nii.gz"),("all files","*.*")))
        if(type(name) != str):
            window.deiconify()
            return
        aux: List[str] = name.split('/')
        filepath: str = aux[-1]
        currentdirectory: str = "/".join(aux[:-1])
        window.currentdirectory.set(currentdirectory)
        window.filepath.set(filepath)
        window.deiconify()

def callbackCurrentDir(*args: None) -> None:
    window: object = views['objects_ref'].SideWindow
    window.pathtextvariable.set(f"Path: {window.currentdirectory.get()}")

def callbackFilePath(*args: None) -> None:
    window: object = views['objects_ref'].SideWindow
    path: str = window.filepath.get()
    if(path == ""):
        window.warning.set("")
        window.openbutton['state'] = "disabled"
    else:
        path_split: List[str] = path.split('.')
        if(len(path_split) > 2 and path_split[-1] == "gz" and path_split[-2] == "nii"):
            finalpath: str = window.currentdirectory.get()+"/"+path
            if(os.path.exists(path=finalpath)):
                window.finalpath = finalpath
                window.warning.set("")
                window.openbutton['state'] = "normal"
            else:
                window.warning.set("File not found")
                window.openbutton['state'] = "disabled"
        else:
            window.warning.set("File format not suported")
            window.openbutton['state'] = "disabled"

def resizedImageHandler(*args: None) -> None:
    window: object = views['objects_ref'].SideWindow
    value: str = window.image_format.get()
    if(value == "Normal"):
        window.resized_image.set(False)
    else:
        window.resized_image.set(True)
    
def onClosing() -> None:
    from micview.controllers.services.menu.callbacks_onclick import delSideWindow
    window: object = views['objects_ref'].SideWindow
    window.filepath.trace_remove("write", window.traceid1)
    window.currentdirectory.trace_remove("write", window.traceid2)
    window.destroy()
    window.update()
    delSideWindow()