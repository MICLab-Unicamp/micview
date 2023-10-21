from PIL import Image, ImageTk
from src.models.models import get_options_states, get_image_canvas_states
from src.controllers.services.volume.controller import *

class ImageCanvasController:
    def __init__(self, master):
        self.master = master
        self.id = self.master.id
        self.resize_factors = (1, 1)
        self.image_data = None
        self.mask_data = None

    def event_handler(self): #when other child suffer click
        print("eventoooo")

    def resize(self, e):
        print("resizing")
        print(e)
        image_shape = get_image_slices(self.id).shape
        self.resize_factors = calc_image_resize_factors(canvas_shape=(e.width, e.height), image_shape=image_shape)
        self.refresh()

    def click(self, e):
        print(e)
        get_image_canvas_states().action_on_child = self.id
        '''
        pega o click, trata e interpola para o tamanho original da imagem
        seta o novo ponto do click
        refresh imagems
        '''
        pass

    def refresh(self):
        print("refreshing")
        self.image_data = ImageTk.PhotoImage(Image.fromarray(get_image_slices(self.id), mode='L').resize(self.resize_factors))
        self.master.draw_image()
        if get_options_states().mask_is_set:
            self.mask_data = ImageTk.PhotoImage(Image.fromarray(get_mask_slices(self.id), mode='RGBA').resize(self.resize_factors))
            self.master.draw_mask()

    def disable_canvas(self):
        self.master.config(state='disabled')
        self.master.unbind('<Configure>')
        self.master.unbind('<Button-1>')
        self.master.unbind('<B1-Motion>')

    def enable_canvas(self):
        self.master.config(state='normal')
        self.master.bind('<Configure>', self.resize)
        self.master.bind('<Button-1>', self.click)
        self.master.bind('<B1-Motion>', self.click)

    '''def UpdatePointAxis2(self, event):
        click = event.__dict__
        x = click['x']; y = click['y']
        new_point_x, new_point_y = self.UpdatePoint(self.images_sizes[2][0], self.images_sizes[2][1], x, y)
        if(new_point_x != None and new_point_y != None):
            square_image_boolean = self.root.getvar(name="square_image_boolean")
            Volctrl.change_current_point(new_point_y,new_point_x,-1, self.square_image) if square_image_boolean else Volctrl.change_current_point(new_point_y,new_point_x,-1, self.image)
            self.ChangeChannelsIntensity()
            Imupdate.UpdateImages(self,square_image_boolean)

    def UpdatePoint(self, image_size_x, image_size_y, x, y):
        center = (self.label_w/2, self.label_h/2)
        if(x < center[0] - image_size_x/2 or x > center[0] + image_size_x/2 or y < center[1] - image_size_y/2 or y > center[1] + image_size_y/2):
            return None, None #Clicked outside the image
        offsetx = math.floor((self.label_w - image_size_x)/2)
        new_point_x = int(x - offsetx) -1
        offsety = math.floor((self.label_h - image_size_y)/2)
        new_point_y = int(y - offsety) -1
        return new_point_x,new_point_y
    '''
        
def calc_image_resize_factors(canvas_shape=(0,0), image_shape=(0,0)):
        max_side = np.array(image_shape).max()
        resize_factors = (canvas_shape[0]/max_side, canvas_shape[0]/max_side)
        if get_options_states().image_is_square:
            square_factor = (max_side/image_shape[0], max_side/image_shape[1])
            return square_factor * resize_factors
        return resize_factors