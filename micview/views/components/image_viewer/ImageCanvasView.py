import tkinter as tk
from micview.controllers.services.image_viewer.ImageCanvasController import *

class ImageCanvasView(tk.Canvas):
    def __init__(self, master: tk.Frame, id: int) -> None:
        self.master = master
        self.id: int = id
        self.controller = None
        super().__init__(master=master, background="#f1f2f6")
        self.Config()

    def Config(self) -> None:
        self.controller = ImageCanvasController(master=self)

    @property
    def center_x(self) -> int:
        return self.winfo_width() // 2
    
    @property
    def center_y(self) -> int:
        return self.winfo_height() // 2