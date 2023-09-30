import tkinter as tk
from tkinter import ttk
import tkinter.filedialog as fd
import os

class OpenFileInputWindow:
    def __init__(self, parent, rootframe):
        self.parent = parent
        self.rootframe = rootframe
        self.root = tk.Toplevel()
        self.root.protocol("WM_DELETE_WINDOW", self.OnClosing)
        self.root.title("Open Image")
        self.root.configure(background='gray75')
        self.root.geometry("400x300")
        self.root.resizable(False, False)
        self.root.transient(self.rootframe)
        self.root.focus_force()
        self.root.grab_set()
        self.CreateVars()
        self.Create_widgets()
        self.OptionsComboboxes()
        self.ActionButtons()

    def CreateVars(self):
        self.warning = tk.StringVar(self.root, value="", name="warning")
        self.filepath = tk.StringVar(self.root, value="", name="filepath")
        self.currentdirectory = tk.StringVar(self.root, value=os.getcwd(), name="currentdirectory")
        self.traceid1 = self.filepath.trace_add("write", callback=self.WatchFilePath)
        self.traceid2 = self.currentdirectory.trace_add("write", callback=self.WatchCurrentDir)
        self.pathtextvariable = tk.StringVar(self.root, value=f"Path: {os.getcwd()}", name="pathtextvariable")
        self.zoomorder = tk.IntVar(self.root, value=0, name="zoom_order")
        self.resized_image = tk.BooleanVar(self.root, value=False, name="resized_image")

    def Create_widgets(self):
        title = tk.Label(self.root, text="Select Main Image", font=('Helvetica', 15, 'bold'))
        title.place(rely=0.02, relx=0.02, relwidth=0.45,relheight=0.1)
        filenametext = tk.Label(self.root, text="Image Filename:", font=('Helvetica', 11))
        filenametext.place(rely=0.14, relx=0.02, relwidth=0.3,relheight=0.08)
        warningtext = tk.Label(self.root, textvariable=self.warning, fg="red", font=('Helvetica', 8))
        warningtext.place(rely=0.14, relx=0.68, relwidth=0.3,relheight=0.08)
        self.input_text = tk.Entry(self.root, textvariable=self.filepath, font=('Helvetica', 10))
        self.input_text.place(rely=0.26, relx=0.02, relwidth=0.96, relheight=0.08)
        pathtext = tk.Label(self.root, textvariable=self.pathtextvariable, fg="blue", font=('Helvetica', 8), anchor="w", justify="left")
        pathtext.place(rely=0.36, relx=0.02, relwidth=0.96,relheight=0.08)

    def OptionsComboboxes(self):
        imageformat_text = tk.Label(self.root, text="Image Format", font=('Helvetica', 10), anchor="w", justify="left")
        imageformat_text.place(rely=0.55, relx=0.02, relheight=0.1, relwidth=0.6)
        self.image_format= ttk.Combobox(self.root, values=["Normal", "Resized"], state="readonly", justify="center")
        self.image_format.option_add('*TCombobox*Listbox.Justify', 'center')
        self.image_format.set("Normal")
        self.image_format.bind('<<ComboboxSelected>>', self.WatchResizedImage)
        self.image_format.place(rely= 0.55, relx=0.68, relheight=0.1, relwidth=0.20)
        
        zoom_combobox_text = tk.Label(self.root, text="Zoom Interpolation Order", font=('Helvetica', 10), anchor="w", justify="left")
        zoom_combobox_text.place(rely=0.7, relx=0.02, relheight=0.1, relwidth=0.6)
        self.zoom_interpolation_order = ttk.Combobox(self.root, values=[ str(x) for x in range(6)], state="readonly", justify="center")
        self.zoom_interpolation_order.option_add('*TCombobox*Listbox.Justify', 'center')
        self.zoom_interpolation_order.set("0")
        self.zoom_interpolation_order.bind('<<ComboboxSelected>>', self.WatchZoomOrder)
        self.zoom_interpolation_order.place(rely= 0.7, relx=0.68, relheight=0.1, relwidth=0.10)

    def ActionButtons(self):
        self.cancel = tk.Button(self.root, text="Cancel", command=self.OnClosing)
        self.browse = tk.Button(self.root, text="Browse", command=self.GetFileName)
        self.openbutton = tk.Button(self.root, text="Open File", state="disabled", command=self.LoadNewImage)
        self.cancel.place(rely=0.88, relx=0.43, relheight=0.1, relwidth=0.18)
        self.browse.place(rely=0.88, relx=0.62, relheight=0.1, relwidth=0.18)
        self.openbutton.place(rely=0.88, relx=0.81, relheight=0.1, relwidth=0.18)

    def GetFileName(self):
        name = fd.askopenfilename(initialdir="./", title="Select File", filetypes= (("NiFTI files","*.nii.gz"),("all files","*.*")))
        aux = name.split('/')
        filepath = aux[-1]
        currentdirectory = "/".join(aux[:-1])
        self.currentdirectory.set(currentdirectory)
        self.filepath.set(filepath)

    def LoadNewImage(self):
        if(self.parent.root.getvar(name="image_is_set")):
            self.parent.ImageFrame.Destroy_image()
        self.OnClosing(loadimage=True)

    def WatchCurrentDir(self, *args):
        self.pathtextvariable.set(f"Path: {self.currentdirectory.get()}")

    def WatchFilePath(self, *args):
        path = self.filepath.get()
        if(path == ""):
            self.warning.set("")
            self.openbutton['state'] = "disabled"
        else:
            path_split = path.split('.')
            if(len(path_split) > 2 and path_split[-1] == "gz" and path_split[-2] == "nii"):
                finalpath = self.currentdirectory.get()+"/"+path
                if(os.path.exists(finalpath)):
                    self.finalpath = finalpath
                    self.warning.set("")
                    self.openbutton['state'] = "normal"
                else:
                    self.warning.set("File not found")
                    self.openbutton['state'] = "disabled"
            else:
                self.warning.set("File format not suported")
                self.openbutton['state'] = "disabled"

    def WatchZoomOrder(self,*args):
        value = self.zoom_interpolation_order.get()
        self.zoomorder.set(int(value))

    def WatchResizedImage(self, *args):
        value = self.image_format.get()
        if(value == "Normal"):
            self.resized_image.set(False)
        else:
            self.resized_image.set(True)

    def OnClosing(self, loadimage=False):
        self.filepath.trace_remove("write", self.traceid1)
        self.currentdirectory.trace_remove("write", self.traceid2)
        self.root.destroy()
        self.root.update()
        if(loadimage):
            self.parent.ImageFrame.Load_Images(file=self.finalpath, order=self.zoomorder.get(), resized = self.resized_image.get())
        self.parent.menuframe.DelFileInputWindow()