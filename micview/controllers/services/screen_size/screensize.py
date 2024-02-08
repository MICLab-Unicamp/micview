##
# @brief: This file is used to get the screen size of the monitor
#

# Imports
from typing import List
from screeninfo import get_monitors

# Functions
def getScreensize() -> "dict[str, int]":
    """!
    @brief: This function is responsible for getting the screen size of the monitor.
    @return: dict[str, int]
    """
    arr: List[object] = get_monitors()
    for monitor in arr:
        if(monitor.is_primary):
            return {"width": monitor.width, "height": monitor.height}
    return {"width": arr[0].width, "height": arr[0].height}
