import tkinter as tk
from controllers.services.image_viewer.ImageCanvasController import *

class ImageCanvasView(tk.Canvas):
    def __init__(self, master, id):
        self.master = master
        self.id = id
        super().__init__(master, background="lightblue")
        self.Config()

    def Config(self):
        self.drawn_image = None
        self.drawn_mask = None
        self.controller = ImageCanvasController(self)
        self.bind('<Configure>', self.controller.resize)
        self.bind('<Button-1>', self.controller.click)
        self.bind('<B1-Motion>', self.controller.click)
    
    def draw_image(self):
        self.drawn_image = self.create_image((self.winfo_width/2, self.winfo_height/2), image=self.controller.image_data, anchor="center")

    def draw_mask(self):
        self.drawn_mask = self.create_image((self.winfo_width/2, self.winfo_height/2), image=self.controller.mask_data, anchor="center")

    def clean_screen(self):################# not used
        self.delete(self.drawn_image)
        self.delete(self.drawn_mask)
        self.drawn_image = None
        self.drawn_mask = None