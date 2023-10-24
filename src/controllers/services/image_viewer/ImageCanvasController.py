from PIL import Image, ImageTk
import tkinter as tk
from src.models.models import get_options_states, get_image_canvas_states
from src.controllers.services.volume.controller import *
from src.controllers.services.image_viewer.services import *

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
        get_image_canvas_states().action_on_child = self.id

    def refresh(self):# Refreshs the canvas objects
        self.image_data = ImageTk.PhotoImage(Image.fromarray(get_image_slices(self.id), mode='L').resize(self.canvas_image_size))
        self.draw_image()
        if get_options_states().mask_is_set:
            self.mask_data = ImageTk.PhotoImage(Image.fromarray(get_mask_slices(self.id), mode='RGBA').resize(self.canvas_image_size))
            self.draw_mask()

    def draw_image(self):
        self.drawn_image = self.master.create_image((self.master.center_x, self.master.center_y), image=self.image_data, anchor="center", tags=("image",))

    def draw_mask(self):
        self.drawn_mask = self.master.create_image((self.master.center_x, self.master.center_y), image=self.mask_data, anchor="center", tags=("mask",))