from PIL import Image, ImageTk
from threading import Event
from src.models.models import get_options_states, get_image_canvas_states, get_loading_states
from src.controllers.services.volume.controller import *
from src.controllers.services.image_viewer.services import *
from src.controllers.services.image_viewer.HandleLoadingBar import *

class ImageCanvasController:
    def __init__(self, master: tk.Canvas):
        self.master = master
        self.id = self.master.id
        self.canvas_image_size = False
        self.proportion_factor = False
        self.enabled = False
        self.image_data = None
        self.mask_data = None

    @property
    def canvas_shape(self):
        return (self.master.winfo_width(), self.master.winfo_height())

    def event_handler(self): #when other child suffer click
        if(get_loading_states().loading):
            self.disable_canvas()
            self.event = Event()
            self.loading_bar = HandleLoadingBar(self.master, self.event)
            self.loading_bar.start()
        elif(not get_loading_states().loading and not self.enabled):
            self.event.set()
            self.enable_canvas()
            self.master.update()
            image_shape = get_image_slices(self.id).shape
            self.canvas_image_size = calc_canvas_image_size(canvas_shape=self.canvas_shape, image_shape=image_shape)
            self.refresh()
        elif(get_image_canvas_states().action_on_child == 3):
            self.resize()
        else:
            self.refresh()

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

    def disable_canvas(self):#disable canvas when loading
        #self.master.config(state='disabled')
        self.enabled = False
        self.master.delete("all")
        self.master.unbind('<Configure>')
        self.master.unbind('<Button-1>')
        self.master.unbind('<B1-Motion>')

    def enable_canvas(self):#enables canvas after loading
        #self.master.config(state='normal')
        self.enabled = True
        self.master.delete("all")
        self.master.bind('<Configure>', self.resize)
        self.master.bind('<Button-1>', self.click)
        self.master.bind('<B1-Motion>', self.click)