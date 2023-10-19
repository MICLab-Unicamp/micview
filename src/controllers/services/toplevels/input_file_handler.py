import tkinter.filedialog as fd
import os
from services.menu.callbacks_onclick import DelSideWindow
from globals.globals import objects_ref

def browseFileHandler():
        window = objects_ref.get_SideWindow()
        window.withdraw()
        name = fd.askopenfilename(initialdir="./", title="Select File", filetypes= (("NiFTI files","*.nii.gz"),("all files","*.*")))
        if(type(name) != str):
            window.deiconify()
            return
        aux = name.split('/')
        filepath = aux[-1]
        currentdirectory = "/".join(aux[:-1])
        window.currentdirectory.set(currentdirectory)
        window.filepath.set(filepath)
        window.deiconify()

def callbackCurrentDir(*args):
    window = objects_ref.get_SideWindow()
    window.pathtextvariable.set(f"Path: {window.currentdirectory.get()}")

def callbackFilePath(*args):
    window = objects_ref.get_SideWindow()
    path = window.filepath.get()
    if(path == ""):
        window.warning.set("")
        window.openbutton['state'] = "disabled"
    else:
        path_split = path.split('.')
        if(len(path_split) > 2 and path_split[-1] == "gz" and path_split[-2] == "nii"):
            finalpath = window.currentdirectory.get()+"/"+path
            if(os.path.exists(finalpath)):
                window.finalpath = finalpath
                window.warning.set("")
                window.openbutton['state'] = "normal"
            else:
                window.warning.set("File not found")
                window.openbutton['state'] = "disabled"
        else:
            window.warning.set("File format not suported")
            window.openbutton['state'] = "disabled"

def zoomOrderHandler(*args):
    window = objects_ref.get_SideWindow()
    value = window.zoom_interpolation_order.get()
    window.zoomorder.set(int(value))

def resizedImageHandler(*args):
    window = objects_ref.get_SideWindow()
    value = window.image_format.get()
    if(value == "Normal"):
        window.resized_image.set(False)
    else:
        window.resized_image.set(True)
    
def onClosing():
    window = objects_ref.get_SideWindow()
    window.filepath.trace_remove("write", window.traceid1)
    window.currentdirectory.trace_remove("write", window.traceid2)
    window.destroy()
    window.update()
    DelSideWindow()