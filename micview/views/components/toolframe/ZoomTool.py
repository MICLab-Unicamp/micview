import tkinter as tk
import importlib
from types import ModuleType
from typing import Any

from micview.controllers.services.tools.zoom_tool import changeZoom
models: ModuleType = importlib.import_module(name='micview.models.getters')

class ZoomTool:
    def __init__(self, master: tk.Tk):
        super().__init__()
        self.master: tk.Tk = master
        self.createVars()
        self.createWidgets()

    def createVars(self) -> None:
        initial_value = models.states['toolframe_states'].zoom
        self.zoom = tk.DoubleVar(master=self.master, value=initial_value, name="zoom_local")
        self.zoom.trace_add(mode="write", callback=self.updateZoom)

    def createWidgets(self) -> None:
        self.title = tk.Label(master=self.master, text="Zoom Tool", font=('Cambria', 13, 'bold'), bg="#f1f2f6")
        self.title.place(x=5, y=10)
        self.zoomTitle = tk.Label(master=self.master, text="Zoom", font=('Cambria', 11, 'bold'), bg="#f1f2f6")
        self.zoomTitle.place(x=5, y=60)
        self.box = tk.Spinbox(master=self.master, from_=0.1, to=10, increment=0.1, width=10, bg="#f1f2f6", textvariable=self.zoom, state="readonly", font=('Cambria', 14))
        self.box.place(x=5, y=85)
        self.zoomButton1 = tk.Button(master=self.master, text="1x", font=('Cambria', 10, 'bold'), bg="#f1f2f6", command=self.set1)
        self.zoomButton1.place(x=5, y=125)
        self.zoomButton5 = tk.Button(master=self.master, text="5x", font=('Cambria', 10, 'bold'), bg="#f1f2f6", command=self.set5)
        self.zoomButton5.place(x=55, y=125)
        self.zoomButton10 = tk.Button(master=self.master, text="10x", font=('Cambria', 10, 'bold'), bg="#f1f2f6", command=self.set10)
        self.zoomButton10.place(x=105, y=125)

    def updateZoom(self, *args: Any) -> None:
        value = self.zoom.get()
        changeZoom(zoom=value)

    def set1(self) -> None:
        self.zoom.set(value=float(1))
        changeZoom(float(1))

    def set5(self) -> None:
        self.zoom.set(value=float(5))
        changeZoom(float(5))
    
    def set10(self) -> None:
        self.zoom.set(value=float(10))
        changeZoom(float(10))
