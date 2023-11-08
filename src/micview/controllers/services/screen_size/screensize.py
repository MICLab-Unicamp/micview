from screeninfo import get_monitors

def get_screensize() -> "dict[str, int]":
    arr: List[Monitor] = get_monitors()
    for monitor in arr:
        if(monitor.is_primary):
            return {"width": monitor.width, "height": monitor.height}
    return {"width": arr[0].width, "height": arr[0].height}
