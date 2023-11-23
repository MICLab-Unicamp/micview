import tkinter as tk
import os
from micview.controllers.services.toplevels.input_file_handler import browseFileHandler, callbackCurrentDir, callbackFilePath, onClosing

class Parent(tk.Toplevel):
    def __init__(self, master: tk.Tk, windowtitle: str, TypeOfFile: str) -> None:
        super().__init__(master=master)
        self.master = master
        self.title(string=windowtitle)
        self.TypeOfFile: str = TypeOfFile
        self.Config_window()
        self.CreateVars()
        self.Create_widgets()
        self.ActionButtons()

    def Config_window(self) -> None:
        self.configure(background='#70a1ff')
        self.geometry(newGeometry="400x300")
        self.resizable(width=False, height=False)
        self.transient(master=self.master)
        self.protocol(name="WM_DELETE_WINDOW", func=onClosing)
        self.focus_force()
        self.grab_set()

    def CreateVars(self) -> None:
        self.warning = tk.StringVar(master=self, value="", name="warning")
        self.filepath = tk.StringVar(master=self, value="", name="filepath")
        self.currentdirectory = tk.StringVar(master=self, value=os.getcwd(), name="currentdirectory")
        self.traceid1: str = self.filepath.trace_add(mode="write", callback=callbackFilePath)
        self.traceid2: str = self.currentdirectory.trace_add(mode="write", callback=callbackCurrentDir)
        self.pathtextvariable = tk.StringVar(master=self, value=f"Path: {os.getcwd()}", name="pathtextvariable")

    def Create_widgets(self) -> None:
        title = tk.Label(master=self, text=f"Select {self.TypeOfFile}", font=('Helvetica', 15, 'bold'), bg="#70a1ff",  justify="left", anchor="w")
        title.place(rely=0.02, relx=0.02, relwidth=0.9,relheight=0.1)
        filenametext = tk.Label(master=self, text=f"{self.TypeOfFile} Filename:", font=('Helvetica', 11), bg="#70a1ff", justify="left", anchor="w")
        filenametext.place(rely=0.14, relx=0.02, relwidth=0.9,relheight=0.08)
        warningtext = tk.Label(master=self, textvariable=self.warning, fg="red", font=('Helvetica', 8), bg="#70a1ff")
        warningtext.place(rely=0.14, relx=0.68, relwidth=0.3,relheight=0.08)
        self.input_text = tk.Entry(master=self, textvariable=self.filepath, font=('Helvetica', 10))
        self.input_text.place(rely=0.26, relx=0.02, relwidth=0.96, relheight=0.08)
        pathtext = tk.Label(master=self, textvariable=self.pathtextvariable, fg="#4cd137", font=('Helvetica', 8), bg="#f1f2f3", anchor="w", justify="left")
        pathtext.place(rely=0.36, relx=0.02, relwidth=0.96,relheight=0.08)

    def ActionButtons(self) -> None:
        self.cancel = tk.Button(master=self, text="Cancel")
        self.browse = tk.Button(master=self, text="Browse", command=browseFileHandler)
        self.openbutton = tk.Button(master=self, text="Open File", state="disabled")
        self.cancel.place(rely=0.88, relx=0.43, relheight=0.1, relwidth=0.18)
        self.cancel.configure(command=onClosing)
        self.browse.place(rely=0.88, relx=0.62, relheight=0.1, relwidth=0.18)
        self.openbutton.place(rely=0.88, relx=0.81, relheight=0.1, relwidth=0.18)