import tkinter as tk
from tkinter import ttk
import tkinter.filedialog as fd
import os

class SideWindow:
    def __init__(self, parent, rootframe, windowtitle, TypeOfFile):
        self.parent = parent
        self.rootframe = rootframe
        self.root = tk.Toplevel()
        self.root.title(windowtitle)
        self.TypeOfFile = TypeOfFile
        self.root.configure(background='gray75')
        self.root.geometry("400x300")
        self.root.resizable(False, False)
        self.root.transient(self.rootframe)
        self.root.focus_force()
        self.root.grab_set()
        self.root.wm_attributes('-topmost', 1)
        self.CreateVars()
        self.Create_widgets()
        self.ActionButtons()

    def CreateVars(self):
        self.warning = tk.StringVar(self.root, value="", name="warning")
        self.filepath = tk.StringVar(self.root, value="", name="filepath")
        self.currentdirectory = tk.StringVar(self.root, value=os.getcwd(), name="currentdirectory")
        self.traceid1 = self.filepath.trace_add("write", callback=self.WatchFilePath)
        self.traceid2 = self.currentdirectory.trace_add("write", callback=self.WatchCurrentDir)
        self.pathtextvariable = tk.StringVar(self.root, value=f"Path: {os.getcwd()}", name="pathtextvariable")

    def Create_widgets(self):
        title = tk.Label(self.root, text=f"Select {self.TypeOfFile}", font=('Helvetica', 15, 'bold'))
        title.place(rely=0.02, relx=0.02, relwidth=0.45,relheight=0.1)
        filenametext = tk.Label(self.root, text=f"{self.TypeOfFile} Filename:", font=('Helvetica', 11))
        filenametext.place(rely=0.14, relx=0.02, relwidth=0.3,relheight=0.08)
        warningtext = tk.Label(self.root, textvariable=self.warning, fg="red", font=('Helvetica', 8))
        warningtext.place(rely=0.14, relx=0.68, relwidth=0.3,relheight=0.08)
        self.input_text = tk.Entry(self.root, textvariable=self.filepath, font=('Helvetica', 10))
        self.input_text.place(rely=0.26, relx=0.02, relwidth=0.96, relheight=0.08)
        pathtext = tk.Label(self.root, textvariable=self.pathtextvariable, fg="blue", font=('Helvetica', 8), anchor="w", justify="left")
        pathtext.place(rely=0.36, relx=0.02, relwidth=0.96,relheight=0.08)

    def ActionButtons(self):
        self.cancel = tk.Button(self.root, text="Cancel")
        self.browse = tk.Button(self.root, text="Browse", command=self.GetFileName)
        self.openbutton = tk.Button(self.root, text="Open File", state="disabled")
        self.cancel.place(rely=0.88, relx=0.43, relheight=0.1, relwidth=0.18)
        self.browse.place(rely=0.88, relx=0.62, relheight=0.1, relwidth=0.18)
        self.openbutton.place(rely=0.88, relx=0.81, relheight=0.1, relwidth=0.18)

    def GetFileName(self):
        name = fd.askopenfilename(initialdir="./", title="Select File", filetypes= (("NiFTI files","*.nii.gz"),("all files","*.*")))
        if(type(name) != str):
            return
        aux = name.split('/')
        filepath = aux[-1]
        currentdirectory = "/".join(aux[:-1])
        self.currentdirectory.set(currentdirectory)
        self.filepath.set(filepath)

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