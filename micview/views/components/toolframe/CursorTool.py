import tkinter as tk
from tkinter import ttk
import importlib
from types import ModuleType
models: ModuleType = importlib.import_module(name='micview.models.getters')
from micview.controllers.services.tools.cursor_tool import handle_selected_item

class CursorTool:
    def __init__(self, master: tk.Tk) -> None:
        super().__init__()  # Call the __init__ method of the parent class
        self.master: tk.Tk = master
        self.initial_point: tuple[int] = models.data['cursor_data'].current_point
        self.CreateVars()
        self.CreateWidgets()

    def CreateVars(self) -> None:
        self.cursorX = tk.IntVar(master=self.master, value=self.initial_point[2]+1, name="cursorX")
        self.cursorY = tk.IntVar(master=self.master, value=self.initial_point[1]+1, name="cursorY")
        self.cursorZ = tk.IntVar(master=self.master, value=self.initial_point[0]+1, name="cursorZ")

    def CreateWidgets(self) -> None:
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
        self.instensitytitle = tk.Label(master=self.master, text="Intensity under cursor:", font=('Cambria', 10), bg="#f1f2f6")
        self.instensitytitle.place(x=5, y=110)
        self.CreateTreeView()

    def CreateTreeView(self) -> None:
        mode = "none"
        numofchannels: int = models.data['original_volume_data'].num_of_channels
        if(numofchannels > 1): mode = "browse" 
        self.treeview = ttk.Treeview(master=self.master, height=5, columns=("col0", "col1"), show="headings", selectmode=mode)
        self.treeview.column(column="col0", anchor="center", stretch=False, width=85)
        self.treeview.column(column="col1", anchor="center", stretch=False, width=99)
        self.treeview.heading(column="col0", text="Channel")
        self.treeview.heading(column="col1", text="Intensity")
        self.treeview.place(x=0, y=150, relheight=0.4, relwidth=1)
        self.AddTreeviewItens(numofchannels=numofchannels)
        self.treeview.bind(sequence='<<TreeviewSelect>>', func=handle_selected_item)

    def AddTreeviewItens(self, numofchannels: int) -> None:
        for i in range(numofchannels):
            self.treeview.insert(parent='', index=tk.END, values=(f"{i+1}", "0"))