import tkinter as tk
from micview.controllers.services.image_viewer.ImageCanvasController import ImageCanvasController

class ImageCanvasView(tk.Canvas):
    def __init__(self, master: tk.Frame, id: int) -> None:
        self.master = master
        self.id: int = id
        self.controller = None
        super().__init__(master=master, background="#f1f2f6")
        self.config()

    def config(self) -> None:
        self.controller = ImageCanvasController(master=self)

    @property
    def centerX(self) -> int:
        return self.winfo_width() // 2
    
    @property
    def centerY(self) -> int:
        return self.winfo_height() // 2