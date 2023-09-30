import tkinter as tk
import math
from screeninfo import get_monitors
from Components.ImageFrame.ImageFrame import *
import Components.ImageFrame.ImageFrame_Update as Imupdate
import Components.Volume.Volume_Controller as Volctrl
import Components.Menu as Menu

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

class RootFrame:
    def __init__(self, window_name, **kwargs):
        self.root = tk.Tk()
        self.window_name = window_name
        self.kwargs = kwargs
        self.CreateGlobalVars()
        self.ScreenConfig()
        self.Frames()
        self.root.after(200, self.checkimageload)
        self.root.mainloop()

    def CreateGlobalVars(self):
        self.image_is_set = tk.BooleanVar(self.root, False, name="image_is_set")
        self.image_is_set.trace('w',self.WatchVars)
        self.square_image_boolean = tk.BooleanVar(self.root, False, name="square_image_boolean")
        self.square_image_boolean.trace('w', self.WatchVars)
    
    def WatchVars(self, *args):
        if(args[0] == "image_is_set"):
            self.menuframe.change_buttons_state()
        if(args[0] == "square_image_boolean"):
            if(self.image_is_set.get()):
                self.ImageFrame.Controller.FormatImageButtonHandler()

    def ScreenConfig(self):
        self.screensize = get_screensize()
        self.root.title(self.window_name)
        self.root.configure(background= '#1e3743')
        self.root.geometry(f"{self.screensize['width']}x{self.screensize['height']}")
        self.root.resizable(True, True)
        min_w,min_h = set_minsize(screen_w=self.screensize['width'], screen_h=self.screensize['height'])
        self.root.minsize(width=min_w, height=min_h)

    def Frames(self):
        self.frame_left = tk.Frame(self.root, bd=4, bg= '#dfe3ee', highlightbackground= '#759fe6', highlightthickness=2)
        self.frame_left.place(relx=0.005, rely=0, relwidth=0.18, relheight=1)

        self.frame_rigth = tk.Frame(self.root, bd=4, bg= '#dfe3ee', highlightbackground= '#759fe6', highlightthickness=2)
        self.frame_rigth.place(relx=0.19, rely=0, relwidth=0.8, relheight=1)
        self.ImageFrame = ImageFrame(self.root, self.frame_rigth)
        self.menuframe = Menu.Menu(self)

    def checkimageload(self):
        if(self.kwargs):
            self.ImageFrame.Load_Images(**self.kwargs)