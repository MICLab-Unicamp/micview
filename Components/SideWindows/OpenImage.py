import tkinter as tk
import tkinter.filedialog as fd
import os
import SimpleITK as sitk

class OpenImageWindow:
    def __init__(self, parentwindow):
        self.parentwindow = parentwindow
        self.root = tk.Toplevel()
        self.root.title("Open Image")
        self.root.configure(background='gray75')
        self.root.geometry("400x300")
        self.root.resizable(False, False)
        self.root.transient(self.parentwindow)
        self.root.focus_force()
        self.root.grab_set()
        self.Create_widgets()
    
    def Create_widgets(self):
        self.warning = tk.StringVar(self.root, value="", name="warning")
        self.filepath = tk.StringVar(self.root, value="", name="filepath")
        self.filepath.trace('w', self.WatchFilePath)
        self.currentdirectory = tk.StringVar(self.root, value=os.getcwd(), name="currentdirectory")
        self.currentdirectory.trace('w', self.WatchCurrentDir)
        self.pathtextvariable = tk.StringVar(self.root, value=f"Path: {os.getcwd()}", name="pathtextvariable")

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

        self.cancel = tk.Button(self.root, text="Cancel", command=self.root.destroy)
        self.browse = tk.Button(self.root, text="Browse", command=self.GetFileName)
        self.openbutton = tk.Button(self.root, text="Open File", state="disabled")
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
                try:
                    image = sitk.ReadImage(finalpath)
                    self.warning.set("")
                    self.openbutton['state'] = "normal"
                except:
                    self.warning.set("File not found")
                    self.openbutton['state'] = "disabled"
            else:
                self.warning.set("File format not suported")
                self.openbutton['state'] = "disabled"