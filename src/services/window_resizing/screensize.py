import math
from screeninfo import get_monitors

def get_screensize():
    arr = get_monitors()
    for monitor in arr:
        if(monitor.is_primary):
            return {"width": monitor.width, "height": monitor.height}
    return {"width": arr[0].width, "height": arr[0].height}

def set_minsize(screen_w,screen_h):
    if(screen_h < screen_w):
        return math.ceil(screen_h*2/3),math.ceil(screen_h*2/3)
    return math.ceil(screen_w*2/3),math.ceil(screen_w*2/3)
