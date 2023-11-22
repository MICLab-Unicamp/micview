from PIL import Image, ImageTk
import tkinter as tk
from micview.models.getters import states
from micview.controllers.services.volume.controller import *
from micview.controllers.services.image_viewer.services import *

class ImageCanvasController:
    def __init__(self, master: tk.Canvas):
        self.master = master
        self.id = self.master.id
        self.canvas_image_size = False
        self.proportion_factor = False
        self.image_data = None
        self.mask_data = None

    @property
    def canvas_shape(self):
        return (self.master.winfo_width(), self.master.winfo_height())

    def event_handler(self, type: str): #when other child suffer click
        if(type == "action_on_child"):
            self.refresh()
        elif(type == "update_all_childs"):
            self.resize()

    def resize(self, e=None):#Resizes the canvas widget
        image_shape = get_image_slices(self.id).shape
        self.canvas_image_size = calc_canvas_image_size(canvas_shape=self.canvas_shape, image_shape=image_shape)
        self.refresh()

    def click(self, e):#Handles clicks on canvas
        self.proportion_factor = calc_proportion_factor(self.id, self.canvas_image_size)
        new_point_x, new_point_y = get_equivalent_point(self.canvas_shape, self.canvas_image_size, self.proportion_factor, e)
        if(new_point_x == -1 and new_point_y == -1):
            return
        valid_points = get_3D_coordinate(self.id, new_point_x, new_point_y)
        valid_points = get_nearest_valid_point(valid_points[0], valid_points[1], valid_points[2])
        valid_points[self.id] = -1
        change_current_point(valid_points[0] ,valid_points[1], valid_points[2])
        states['image_canvas_states'].action_on_child = self.id

    def refresh(self):# Refreshs the canvas objects
        self.image_data = ImageTk.PhotoImage(Image.fromarray(get_image_slices(self.id), mode='L').resize(size=self.canvas_image_size, resample=Image.NEAREST))
        self.draw_image()
        self.master.delete('orient_text')
        self.draw_orient_text()
        if states['options_states'].mask_is_set:
            self.mask_data = ImageTk.PhotoImage(Image.fromarray(get_mask_slices(self.id), mode='RGBA').resize(size=self.canvas_image_size, resample=Image.NEAREST))
            self.draw_mask()

    def draw_image(self):
        self.drawn_image = self.master.create_image((self.master.center_x, self.master.center_y), image=self.image_data, anchor="center", tags=("image",))

    def draw_mask(self):
        self.drawn_mask = self.master.create_image((self.master.center_x, self.master.center_y), image=self.mask_data, anchor="center", tags=("mask",))
    
    def draw_orient_text(self):
        self.orient_text = data['files_data'].orient_text[self.id]
        self.drawn_orient_text = self.master.create_text((10,self.master.center_y), text=f"{self.orient_text[0]}", font=('Cambria',15,'bold'), fill="#EA2027", anchor="w", tags=("orient_text",))
        self.drawn_orient_text = self.master.create_text((self.master.center_x,3), text=f"{self.orient_text[1]}", font=('Cambria',13,'bold'), fill="#EA2027", anchor="n", tags=("orient_text",))
        self.drawn_orient_text = self.master.create_text((self.master.winfo_width()-10,self.master.center_y), text=f"{self.orient_text[2]}", fill="#EA2027", font=('Cambria',15,'bold'), anchor="e", tags=("orient_text",))
        self.drawn_orient_text = self.master.create_text((self.master.center_x,self.master.winfo_height()-3), text=f"{self.orient_text[3]}", fill="#EA2027", font=('Cambria',13,'bold'), anchor="s", tags=("orient_text",))