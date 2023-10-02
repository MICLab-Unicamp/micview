import tkinter as tk
from tkinter import ttk
import Components.Volume.Volume_Controller as Volctrl

class CursorTool:
    def __init__(self, parent, root):
        self.parent = parent
        self.root = root
        self.numofchannels = self.parent.root.getvar(name="num_of_channels")
        self.treeview_is_set = False
        self.CreateVars()
        self.CreateWidgets()

    def CreateVars(self):
        self.cursorX = tk.IntVar(self.root, value=0, name="cursorX")
        self.cursorY = tk.IntVar(self.root, value=0, name="cursorY")
        self.cursorZ = tk.IntVar(self.root, value=0, name="cursorZ")

    def CreateWidgets(self):
        self.title = tk.Label(self.root, text="Cursor Inspector", font=('Helvetica', 15, 'bold'))
        self.title.place(x=5, y=10)
        self.cursorpositiontitle = tk.Label(self.root, text="Cursor position (x,y,z):", font=('Helvetica', 10))
        self.cursorpositiontitle.place(x=5, y=40)
        self.posx = tk.Entry(self.root, textvariable=self.cursorX, font=('Helvetica', 8))
        self.posx.place(x=5, y=60, width=30, height=30)
        self.posy = tk.Entry(self.root, textvariable=self.cursorY, font=('Helvetica', 8))
        self.posy.place(x=40, y=60, width=30, height=30)
        self.posz = tk.Entry(self.root, textvariable=self.cursorZ, font=('Helvetica', 8))
        self.posz.place(x=75, y=60, width=30, height=30)
        self.instensitytitle = tk.Label(self.root, text="Intensity under cursor:", font=('Helvetica', 10))
        self.instensitytitle.place(x=5, y=110)
        self.Update_intensity()

    def CreateTreeView(self, itens_array):
        self.layerslist = ttk.Treeview(self.root, height=5, columns=("col0", "col1"), show="headings", selectmode="browse")
        self.layerslist.column("col0", anchor="center", stretch=False, width=85)
        self.layerslist.column("col1", anchor="center", stretch=False, width=99)
        self.layerslist.heading("col0", text="Channel")
        self.layerslist.heading("col1", text="Intensity")
        self.layerslist.place(x=0, y=150, relheight=0.4, relwidth=1)
        self.AddTreeviewItens(itens_array)
        self.layerslist.bind('<<TreeviewSelect>>', self.Selected_item)
        self.treeview_is_set = True

    def Selected_item(self,event):
        itemid = self.layerslist.focus()
        selected_channel = int(self.layerslist.item(itemid, 'values')[0]) - 1
        self.parent.root.setvar(name="channel_select", value=selected_channel)

    def AddTreeviewItens(self, itens):
        for i in range(self.numofchannels):
            self.layerslist.insert('', tk.END, values=(f"{i+1}", f"{itens[i]}"))

    def Update_intensity(self):
        intensity = self.parent.root.getvar(name="channel_intensity")
        if(self.numofchannels > 1):
            parse = ((intensity.split('[')[1]).split(']')[0]).split(', ')
            chann_intensity = [int(i) for i in parse]
        else:
            parse = (intensity.split('[')[1]).split(']')[0]
            chann_intensity = [round(float(parse),2)]
        self.Update_itens(intensity_arr=chann_intensity)

    def Update_itens(self, intensity_arr):
        if(self.treeview_is_set):
            itens = self.layerslist.get_children()
            for i in range(len(itens)):
                values = self.layerslist.item(itens[i],'values')
                self.layerslist.item(itens[i], values=(values[0], intensity_arr[i]))
        else:
            self.CreateTreeView(intensity_arr)
