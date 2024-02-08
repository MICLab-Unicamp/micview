##
# @brief This file contains the CursorTool class, which is a component of the ToolFrame class.
#

# Imports
import tkinter as tk
from tkinter import ttk
import importlib
from types import ModuleType
models: ModuleType = importlib.import_module(name='micview.models.getters')
from micview.controllers.services.tools.cursor_tool import handleSelectedItem, updateTransparency

# Classes
class CursorTool:
    """!
    @brief This class represents the cursor tool in the toolframe.
    """
    def __init__(self, master: tk.Tk) -> None:
        """!
        @brief The constructor of the class.
        @param master: tk.Tk - The master window of the application.
        @return None
        """
        super().__init__()  # Call the __init__ method of the parent class
        self.master: tk.Tk = master
        self.createVars()
        self.createWidgets()

    def createVars(self) -> None:
        """!
        @brief This method creates the variables of the class.
        @return None
        """
        self.cursorX = tk.IntVar(master=self.master, value=0, name="cursorX")
        self.cursorY = tk.IntVar(master=self.master, value=0, name="cursorY")
        self.cursorZ = tk.IntVar(master=self.master, value=0, name="cursorZ")
        initial_label = "No Label"
        if(models.data['cursor_data'].label_under_cursor != 0):
            initial_label = f"Label {models.data['cursor_data'].label_under_cursor}"
        self.label_under_cursor = tk.StringVar(master=self.master, value=initial_label, name="label_under_cursor")

    def createWidgets(self) -> None:
        """!
        @brief This method creates the widgets of the class.
        @return None
        """
        self.title = tk.Label(master=self.master, text="Cursor Inspector", font=('Cambria', 13, 'bold'), bg="#f1f2f6")
        self.title.place(x=5, y=10)
        self.cursorpositiontitle = tk.Label(master=self.master, text="Cursor position (x,y,z):", font=('Cambria', 10), bg="#f1f2f6")
        self.cursorpositiontitle.place(x=5, y=40)
        self.posx = tk.Label(master=self.master, textvariable=self.cursorX, font=('Cambria', 8), bg="#ffffff")
        self.posx.place(x=5, y=60, width=30, height=30)
        self.posy = tk.Label(master=self.master, textvariable=self.cursorY, font=('Cambria', 8), bg="#ffffff")
        self.posy.place(x=40, y=60, width=30, height=30)
        self.posz = tk.Label(master=self.master, textvariable=self.cursorZ, font=('Cambria', 8), bg="#ffffff")
        self.posz.place(x=75, y=60, width=30, height=30)
        self.labelUnderCursorTitle = tk.Label(master=self.master, text="Label under cursor:", font=('Cambria', 10), bg="#f1f2f6")
        self.labelUnderCursorTitle.place(x=5, y=110)
        self.labelUnderCursor = tk.Label(master=self.master, textvariable=self.label_under_cursor, font=('Cambria', 8), bg="#ffffff")
        self.labelUnderCursor.place(x=5, y=130, width=90, height=30)
        self.transparencyTitle = tk.Label(master=self.master, text="Label transparency:", font=('Cambria', 10), bg="#f1f2f6")
        self.transparencyTitle.place(x=5, y=170)
        self.transparencyScale = tk.Scale(master=self.master, from_=0, to=100, resolution=1, orient=tk.HORIZONTAL, length=100, bg="#f1f2f6", troughcolor="#ffffff", sliderlength=20, sliderrelief=tk.FLAT, command=updateTransparency)
        self.transparencyScale.place(x=5, y=190)
        self.transparencyScale.set(int(models.states['toolframe_states'].transparency_level*100))
        self.instensitytitle = tk.Label(master=self.master, text="Intensity under cursor:", font=('Cambria', 10), bg="#f1f2f6")
        self.instensitytitle.place(x=5, y=230)
        self.CreateTreeView()

    def CreateTreeView(self) -> None:
        """!
        @brief This method creates the treeview widget.
        @return None
        """
        mode = "none"
        numofchannels: int = models.data['original_volume_data'].num_of_channels
        if(numofchannels > 1): mode = "browse" 
        self.treeview = ttk.Treeview(master=self.master, height=5, columns=("col0", "col1"), show="headings", selectmode=mode)
        self.treeview.column(column="col0", anchor="center", stretch=False, width=85)
        self.treeview.column(column="col1", anchor="center", stretch=False, width=99)
        self.treeview.heading(column="col0", text="Channel")
        self.treeview.heading(column="col1", text="Intensity")
        self.treeview.place(x=0, y=260, relheight=0.4, relwidth=1)
        self.addTreeviewItens(numofchannels=numofchannels)
        self.treeview.bind(sequence='<<TreeviewSelect>>', func=handleSelectedItem)

    def addTreeviewItens(self, numofchannels: int) -> None:
        """!
        @brief This method adds the itens to the treeview.
        @param numofchannels: int - The number of channels.
        @return None
        """
        for i in range(numofchannels):
            self.treeview.insert(parent='', index=tk.END, values=(f"{i+1}", "0"))