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
    
def getEquivalentPoint(canvas_shape: List[int], canvas_image_size: Tuple[float, float], zoom_area: Tuple[float, float, float, float], e: Any) -> Tuple[int, int]:
    '''
    Gets equivalent point of canvas on volume surface
    '''
    center: Tuple[float, float] = (canvas_shape[0]/2, canvas_shape[1]/2)
    if(e.x < center[0] - canvas_image_size[0]/2 or e.x > center[0] + canvas_image_size[0]/2 or e.y < center[1] - canvas_image_size[1]/2 or e.y > center[1] + canvas_image_size[1]/2):
        return -1, -1
    offsetx: float = (canvas_shape[0] - canvas_image_size[0])/2
    new_point_x: int = (e.x - offsetx)*(zoom_area[2] - zoom_area[0])/canvas_image_size[0] + zoom_area[0]
    offsety: float = (canvas_shape[1] - canvas_image_size[1])/2
    new_point_y: int = (e.y - offsety)*(zoom_area[3] - zoom_area[1])/canvas_image_size[1] + zoom_area[1]
    return new_point_x, new_point_y

def getInverseEquivalentPoint(id: int, canvas_shape: List[int], canvas_image_size: Tuple[float, float], zoom_area: Tuple[float, float, float, float]) -> Tuple[int, int]:
    points = data["cursor_data"].current_point
    x,y = 0,0
    if(id == 0):
        x,y = points[2], points[1]
    if(id == 1):
        x,y = points[2], points[0]
    if(id == 2):
        x,y = points[1], points[0]
    
    offsetx: float = (canvas_shape[0] - canvas_image_size[0])/2
    offsety: float = (canvas_shape[1] - canvas_image_size[1])/2
    new_point_x: int = (x - zoom_area[0])*canvas_image_size[0]/(zoom_area[2] - zoom_area[0]) + offsetx
    new_point_y: int = (y - zoom_area[1])*canvas_image_size[1]/(zoom_area[3] - zoom_area[1]) + offsety
    if(new_point_x < 0):
        new_point_x = 0
    if(new_point_y < 0):
        new_point_y = 0
    if(new_point_x > canvas_shape[0]):
        new_point_x = canvas_shape[0]
    if(new_point_y > canvas_shape[1]):
        new_point_y = canvas_shape[1]
    return new_point_x, new_point_y