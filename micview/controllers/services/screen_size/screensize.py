from typing import List
from screeninfo import get_monitors

def getScreensize() -> "dict[str, int]":
    arr: List[object] = get_monitors()
    for monitor in arr:
        if(monitor.is_primary):
            return {"width": monitor.width, "height": monitor.height}
    return {"width": arr[0].width, "height": arr[0].height}
