##
# @brief: This file contains the class that creates the metadata window.
#

# Imports
import tkinter as tk
from tkinter import ttk
import importlib
from types import ModuleType
models: ModuleType = importlib.import_module(name='micview.models.getters')

# Classes
class Metadata(tk.Toplevel):
    """!
    @brief: This class creates the metadata window.
    """
    def __init__(self, master: tk.Tk) -> None:
        """!
        @brief: The constructor of the class.
        @param: master: tk.Tk - The master window of the application.
        @return: None
        """
        super().__init__(master=master)
        self.master = master
        self.configWindow()
        self.metadatas = dict(models.data['files_data'].image_metadatas)
        self.createWidgets()

    def configWindow(self) -> None:
        """!
        @brief: This method configures the window.
        @return: None
        """
        self.configure(background='#f1f2f6')
        self.geometry(newGeometry="500x400")
        self.resizable(width=False, height=False)
        self.transient(master=self.master)
        self.protocol(name="WM_DELETE_WINDOW", func=self.onClosing)
        self.focus_force()
        self.grab_set()

    def createWidgets(self) -> None:
        """!
        @brief: This method creates the widgets of the class.
        @return: None
        """
        title = tk.Label(master=self, text="Image Metadata", font=('Helvetica', 15, 'bold'), bg="#f1f2f6",  justify="left", anchor="w")
        title.place(y=10, x=30, width=250, height=20)
        self.treeview = ttk.Treeview(master=self, height=10, columns=("col1", "col2"), show="headings", selectmode="none")
        self.treeview.column(column="col1", anchor="center", stretch=False, width=220)
        self.treeview.column(column="col2", anchor="center", stretch=False, width=220)
        self.treeview.heading(column="col1", text="Key")
        self.treeview.heading(column="col2", text="Value")
        self.treeview.place(x=30, y=45, height=340, width=440)
        self.scrool = tk.Scrollbar(self, orient='vertical')
        self.treeview.configure(yscroll=self.scrool.set)
        self.scrool.place(x=470, y=45, width=10, height=340)
        self.addTreeviewItens()

    def addTreeviewItens(self) -> None:
        """!
        @brief: This method adds the items to the treeview widget.
        @return: None
        """
        for x, y in self.metadatas.items():
            self.treeview.insert(parent='', index=tk.END, values=(f"{x}", f"{y}"))


    def onClosing(self) -> None:
        """!
        @brief: This method is called when the window is closed.
        @return: None
        """
        from micview.controllers.services.menu.callbacks_onclick import delSideWindow
        window: object = models.views['objects_ref'].SideWindow
        window.destroy()
        window.update()
        delSideWindow()