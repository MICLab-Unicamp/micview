import tkinter as tk
from tkinter import ttk
import importlib
models = importlib.import_module('micview.models.getters')
from micview.controllers.services.tools.cursor_tool import *

class CursorTool:
    def __init__(self, master):
        self.master = master
        self.initial_point = models.data['cursor_data'].current_point
        self.CreateVars()
        self.CreateWidgets()

    def CreateVars(self):
        self.cursorX = tk.IntVar(self.master, value=self.initial_point[2]+1, name="cursorX")
        self.cursorY = tk.IntVar(self.master, value=self.initial_point[1]+1, name="cursorY")
        self.cursorZ = tk.IntVar(self.master, value=self.initial_point[0]+1, name="cursorZ")

    def CreateWidgets(self):
        self.title = tk.Label(self.master, text="Cursor Inspector", font=('Cambria', 13, 'bold'), bg="#f1f2f6")
        self.title.place(x=5, y=10)
        self.cursorpositiontitle = tk.Label(self.master, text="Cursor position (x,y,z):", font=('Cambria', 10), bg="#f1f2f6")
        self.cursorpositiontitle.place(x=5, y=40)
        self.posx = tk.Label(self.master, textvariable=self.cursorX, font=('Cambria', 8), bg="#ffffff")
        self.posx.place(x=5, y=60, width=30, height=30)
        self.posy = tk.Label(self.master, textvariable=self.cursorY, font=('Cambria', 8), bg="#ffffff")
        self.posy.place(x=40, y=60, width=30, height=30)
        self.posz = tk.Label(self.master, textvariable=self.cursorZ, font=('Cambria', 8), bg="#ffffff")
        self.posz.place(x=75, y=60, width=30, height=30)
        self.instensitytitle = tk.Label(self.master, text="Intensity under cursor:", font=('Cambria', 10), bg="#f1f2f6")
        self.instensitytitle.place(x=5, y=110)
        self.CreateTreeView()

    def CreateTreeView(self):
        mode = "none"
        numofchannels = models.data['original_volume_data'].num_of_channels
        if(numofchannels > 1): mode = "browse" 
        self.treeview = ttk.Treeview(self.master, height=5, columns=("col0", "col1"), show="headings", selectmode=mode)
        self.treeview.column("col0", anchor="center", stretch=False, width=85)
        self.treeview.column("col1", anchor="center", stretch=False, width=99)
        self.treeview.heading("col0", text="Channel")
        self.treeview.heading("col1", text="Intensity")
        self.treeview.place(x=0, y=150, relheight=0.4, relwidth=1)
        self.AddTreeviewItens(numofchannels)
        self.treeview.bind('<<TreeviewSelect>>', handle_selected_item)

    def AddTreeviewItens(self, numofchannels):
        for i in range(numofchannels):
            self.treeview.insert('', tk.END, values=(f"{i+1}", "0"))