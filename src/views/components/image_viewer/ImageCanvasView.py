import tkinter as tk
from src.controllers.services.image_viewer.ImageCanvasController import *

class ImageCanvasView(tk.Canvas):
    def __init__(self, master, id):
        self.master = master
        self.id = id
        super().__init__(master, background="lightblue")
        self.Config()

    def Config(self):
        self.controller = ImageCanvasController(self)

    @property
    def center_x(self):
        return self.winfo_width() // 2
    
    @property
    def center_y(self):
        return self.winfo_height() // 2