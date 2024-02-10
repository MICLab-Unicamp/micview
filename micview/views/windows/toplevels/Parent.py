##
# @brief This file contains the Parent class, which is a toplevel window that is used as a parent window for other toplevel windows.
#

# Imports
import tkinter as tk
import os
import importlib
from types import ModuleType
from micview.controllers.services.toplevels.input_file_handler import browseFileHandler, browseDirHandler, callbackCurrentDir, callbackFilePath, onClosing
models: ModuleType = importlib.import_module(name='micview.models.getters')

# Classes
class Parent(tk.Toplevel):
    """!
    @brief This class represents the Parent class, which is a toplevel window that is used as a parent window for other toplevel windows.
    """
    def __init__(self, master: tk.Tk, windowtitle: str, type_of_file: str) -> None:
        """!
        @brief The constructor of the class.
        @param master: tk.Tk - The master window of the application.
        @param windowtitle: str - The title of the window.
        @param type_of_file: str - The type of file that the window will handle.
        @return None
        """
        super().__init__(master=master)
        self.master = master
        self.title(string=windowtitle)
        self.type_of_file: str = type_of_file
        self.configWindow()
        self.createVars()
        self.createWidgets()
        self.actionButtons()

    def configWindow(self) -> None:
        """!
        @brief This method configures the window.
        @return None
        """
        self.configure(background='#70a1ff')
        self.geometry(newGeometry="400x300")
        self.resizable(width=False, height=False)
        self.transient(master=self.master)
        self.protocol(name="WM_DELETE_WINDOW", func=onClosing)
        self.focus_force()
        self.grab_set()

    def createVars(self) -> None:
        """!
        @brief This method creates the variables of the class.
        @return None
        """
        self.warning = tk.StringVar(master=self, value="", name="warning")
        self.filepath = tk.StringVar(master=self, value="", name="filepath")
        currentdir = models.data['toolframe_data'].dirpath
        self.currentdirectory = tk.StringVar(master=self, value= currentdir if(len(currentdir)>0) else os.getcwd(), name="currentdirectory")
        self.traceid1: str = self.filepath.trace_add(mode="write", callback=callbackFilePath)
        self.traceid2: str = self.currentdirectory.trace_add(mode="write", callback=callbackCurrentDir)
        self.pathtextvariable = tk.StringVar(master=self, value=f"Path: {currentdir if(len(currentdir)>0) else os.getcwd()}", name="pathtextvariable")

    def createWidgets(self) -> None:
        """!
        @brief This method creates the widgets of the class.
        @return None
        """
        title = tk.Label(master=self, text=f"Select {self.type_of_file}", font=('Helvetica', 15, 'bold'), bg="#70a1ff",  justify="left", anchor="w")
        title.place(rely=0.02, relx=0.02, relwidth=0.9,relheight=0.1)
        filenametext = tk.Label(master=self, text=f"{self.type_of_file} Filename:", font=('Helvetica', 11), bg="#70a1ff", justify="left", anchor="w")
        filenametext.place(rely=0.14, relx=0.02, relwidth=0.9,relheight=0.08)
        warningtext = tk.Label(master=self, textvariable=self.warning, fg="red", font=('Helvetica', 8), bg="#70a1ff")
        warningtext.place(rely=0.14, relx=0.68, relwidth=0.3,relheight=0.08)
        self.input_text = tk.Entry(master=self, textvariable=self.filepath, font=('Helvetica', 10))
        self.input_text.place(rely=0.26, relx=0.02, relwidth=0.96, relheight=0.08)
        pathtext = tk.Label(master=self, textvariable=self.pathtextvariable, fg="#4cd137", font=('Helvetica', 8), bg="#f1f2f3", anchor="w", justify="left")
        pathtext.place(rely=0.36, relx=0.02, relwidth=0.96,relheight=0.08)

    def actionButtons(self) -> None:
        """!
        @brief This method creates the action buttons of the class.
        @return None
        """
        self.cancel = tk.Button(master=self, text="Cancel")
        self.browseDir = tk.Button(master=self, text="Browse Dir", command=browseDirHandler)
        self.browse = tk.Button(master=self, text="Browse", command=browseFileHandler)
        self.openbutton = tk.Button(master=self, text="Open File", state="disabled")
        self.cancel.place(rely=0.88, relx=0.24, relheight=0.1, relwidth=0.18)
        self.cancel.configure(command=onClosing)
        self.browseDir.place(rely=0.88, relx=0.43, relheight=0.1, relwidth=0.18)
        self.browse.place(rely=0.88, relx=0.62, relheight=0.1, relwidth=0.18)
        self.openbutton.place(rely=0.88, relx=0.81, relheight=0.1, relwidth=0.18)