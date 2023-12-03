from typing import Any, List, Literal, Tuple
from micview.models.getters import states, data
from typing import List, Tuple

def calcCanvasImageSize(canvas_shape: Tuple[int,int]=(0,0), image_shape: Tuple[int,int]=(0,0)) -> Tuple[int, int]:
        '''
        Calcs the image size that will be displayed on canvas
        '''
        max_side: Literal[0, 1] = 0 if image_shape[0]>image_shape[1] else 1
        if states['options_states'].image_is_square:
            return (int(canvas_shape[1]), int(canvas_shape[1]))
        mult_factor: float = canvas_shape[1]/image_shape[max_side]
        return (int(mult_factor*image_shape[1]), int(mult_factor*image_shape[0]))

def calcProportionFactor(id: int ,canvas_image_size: Tuple[float, float]) -> Tuple[float, float]:
    '''
    Calcs the proportion factor between image in canvas and volume
    '''
    volume_shape: List[float] = data['changed_volume_data'].changed_image_volume.shape
    shift = 0
    if(len(volume_shape) > 3):
        shift = 1
    if(id == 0):
        return (volume_shape[2 + shift]/canvas_image_size[0], volume_shape[1 + shift]/canvas_image_size[1])
    if(id == 1):
        return (volume_shape[2 + shift]/canvas_image_size[0], volume_shape[0 + shift]/canvas_image_size[1])
    if(id == 2):
        return (volume_shape[1 + shift]/canvas_image_size[0], volume_shape[0 + shift]/canvas_image_size[1])
    
def get3DCoordinate(id:int, x:int, y:int) -> List[int]:
    '''
    Gets the 3D coordinate on volume
    '''
    if(id == 0):
        return [0, y, x]
    if(id == 1):
        return [y, 0, x]
    if(id == 2):
        return [y, x, 0]
    
def getEquivalentPoint(canvas_shape: List[int], canvas_image_size: Tuple[float, float], proportion_factor: float, e: Any) -> Tuple[int, int]:
    '''
    Gets equivalent point of canvas on volume surface
    '''
    center: Tuple[float, float] = (canvas_shape[0]/2, canvas_shape[1]/2)
    if(e.x < center[0] - canvas_image_size[0]/2 or e.x > center[0] + canvas_image_size[0]/2 or e.y < center[1] - canvas_image_size[1]/2 or e.y > center[1] + canvas_image_size[1]/2):
        return -1, -1
    offsetx: float = (canvas_shape[0] - canvas_image_size[0])/2
    new_point_x: int = (e.x - offsetx)*proportion_factor[0]
    offsety: float = (canvas_shape[1] - canvas_image_size[1])/2
    new_point_y: int = (e.y - offsety)*proportion_factor[1]
    return new_point_x, new_point_y