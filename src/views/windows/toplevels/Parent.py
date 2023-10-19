import tkinter as tk
import os
from services.sidewindows.input_file_handler import browseFileHandler, callbackCurrentDir, callbackFilePath, onClosing

class Parent(tk.Toplevel):
    def __init__(self, master, windowtitle, TypeOfFile):
        super().__init__(master=master)
        self.transient(master=master)
        self.title(windowtitle)
        self.TypeOfFile = TypeOfFile
        self.Config_window()
        self.CreateVars()
        self.Create_widgets()
        self.ActionButtons()

    def Config_window(self):
        self.configure(background='gray75')
        self.geometry("400x300")
        self.resizable(False, False)
        self.protocol("WM_DELETE_WINDOW", onClosing)
        self.focus_force()
        self.grab_set()

    def CreateVars(self):
        self.warning = tk.StringVar(self, value="", name="warning")
        self.filepath = tk.StringVar(self, value="", name="filepath")
        self.currentdirectory = tk.StringVar(self, value=os.getcwd(), name="currentdirectory")
        self.traceid1 = self.filepath.trace_add("write", callback=callbackFilePath)
        self.traceid2 = self.currentdirectory.trace_add("write", callback=callbackCurrentDir)
        self.pathtextvariable = tk.StringVar(self, value=f"Path: {os.getcwd()}", name="pathtextvariable")

    def Create_widgets(self):
        title = tk.Label(self, text=f"Select {self.TypeOfFile}", font=('Helvetica', 15, 'bold'))
        title.place(rely=0.02, relx=0.02, relwidth=0.45,relheight=0.1)
        filenametext = tk.Label(self, text=f"{self.TypeOfFile} Filename:", font=('Helvetica', 11))
        filenametext.place(rely=0.14, relx=0.02, relwidth=0.3,relheight=0.08)
        warningtext = tk.Label(self, textvariable=self.warning, fg="red", font=('Helvetica', 8))
        warningtext.place(rely=0.14, relx=0.68, relwidth=0.3,relheight=0.08)
        self.input_text = tk.Entry(self, textvariable=self.filepath, font=('Helvetica', 10))
        self.input_text.place(rely=0.26, relx=0.02, relwidth=0.96, relheight=0.08)
        pathtext = tk.Label(self, textvariable=self.pathtextvariable, fg="blue", font=('Helvetica', 8), anchor="w", justify="left")
        pathtext.place(rely=0.36, relx=0.02, relwidth=0.96,relheight=0.08)

    def ActionButtons(self):
        self.cancel = tk.Button(self, text="Cancel")
        self.browse = tk.Button(self, text="Browse", command=browseFileHandler)
        self.openbutton = tk.Button(self, text="Open File", state="disabled")
        self.cancel.place(rely=0.88, relx=0.43, relheight=0.1, relwidth=0.18)
        self.cancel.configure(command=onClosing)
        self.browse.place(rely=0.88, relx=0.62, relheight=0.1, relwidth=0.18)
        self.openbutton.place(rely=0.88, relx=0.81, relheight=0.1, relwidth=0.18)