##
# @brief: This function returns a color from the pallete
#

# Imports
from typing import Dict, Any, List, Tuple

pallete: List[Dict[str, Tuple[int,int,int]]] = [
    {'Number': 1, 'RGB': (255, 0, 0)},
    {'Number': 2, 'RGB': (0, 255, 0)},
    {'Number': 3, 'RGB': (0, 0, 255)},
    {'Number': 4, 'RGB': (255, 255, 0)},
    {'Number': 5, 'RGB': (0, 255, 255)},
    {'Number': 6, 'RGB': (255, 0, 255)},
    {'Number': 7, 'RGB': (255, 255, 255)}
]

# Function
def maskPallete(index: int) -> Dict[str, Any]:
    """!
    @brief: This function returns a color from the pallete
    @param index: int
    @return: Dict[str, Any]
    """
    if(index < 7):
        return dict.copy(pallete[index])
    else:
        color: Dict[str, Any] = dict.copy(self=pallete[index%7])
        color["Number"] = index + 1
        rgb: List[int] = [0,0,0]
        for i in range(3):
            ton: float = abs(color["RGB"][i] - 30*(index//7))
            if(ton>255):
                ton = 255
            rgb[i] = ton
        color["RGB"] = tuple(rgb)
        return color