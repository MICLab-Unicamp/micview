from src.models.models import get_options_states
from src.controllers.validations.validate_point import *

def calc_canvas_image_size(canvas_shape=(0,0), image_shape=(0,0)):
        '''
        Calcs the image size that will be displayed on canvas
        '''
        max_side = 0 if image_shape[0]>image_shape[1] else 1
        if get_options_states().image_is_square:
            return (int(canvas_shape[1]), int(canvas_shape[1]))
        mult_factor = canvas_shape[1]/image_shape[max_side]
        return (int(mult_factor*image_shape[1]), int(mult_factor*image_shape[0]))

def calc_proportion_factor(id ,canvas_image_size):
    '''
    Calcs the proportion factor between image in canvas and volume
    '''
    volume_shape = get_changed_volume_data().changed_image_volume.shape
    shift = 0
    if(len(volume_shape) > 3):
        shift = 1
    if(id == 0):
        return (volume_shape[2 + shift]/canvas_image_size[0], volume_shape[1 + shift]/canvas_image_size[1])
    if(id == 1):
        return (volume_shape[2 + shift]/canvas_image_size[0], volume_shape[0 + shift]/canvas_image_size[1])
    if(id == 2):
        return (volume_shape[1 + shift]/canvas_image_size[0], volume_shape[0 + shift]/canvas_image_size[1])
    
def get_3D_coordinate(id, x, y):
    '''
    Gets the 3D coordinate on volume
    '''
    if(id == 0):
        return [0, y, x]
    if(id == 1):
        return [y, 0, x]
    if(id == 2):
        return [y, x, 0]
    
def get_equivalent_point(canvas_shape, canvas_image_size, proportion_factor, e):
    '''
    Gets equivalent point of canvas on volume surface
    '''
    center = (canvas_shape[0]/2, canvas_shape[1]/2)
    if(e.x < center[0] - canvas_image_size[0]/2 or e.x > center[0] + canvas_image_size[0]/2 or e.y < center[1] - canvas_image_size[1]/2 or e.y > center[1] + canvas_image_size[1]/2):
        return -1, -1
    offsetx = (canvas_shape[0] - canvas_image_size[0])/2
    new_point_x = (e.x - offsetx)*proportion_factor[0]
    offsety = (canvas_shape[1] - canvas_image_size[1])/2
    new_point_y = (e.y - offsety)*proportion_factor[1]
    return new_point_x, new_point_y