import tkinter as tk
import math
from screeninfo import get_monitors
from threading import Thread
from Components.ImageFrame.ImageFrame import *
import Components.ImageFrame.ImageFrame_Update as Imupdate
import Components.Volume.Volume_Controller as Volctrl
import Components.Menu as Menu
from Components.ToolFrame.ToolFrame import *
from Components.CircularProgressbar import *

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
        self.window_name = window_name
        self.kwargs = kwargs
        self.root = tk.Tk()
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
        self.channel_select = tk.IntVar(self.root, -1, name="channel_select")
        self.channel_select.trace('w', self.WatchVars)
        self.num_of_channels = tk.IntVar(self.root, 1, name="num_of_channels")
        self.toolvar = tk.StringVar(self.root, value="none", name="toolvar")
        self.toolvar.trace('w', self.WatchVars)
        self.channel_intensity = tk.StringVar(self.root, "", name="channel_intensity")
        self.channel_intensity.trace('w', self.WatchVars)
        self.loading = tk.BooleanVar(self.root, False, name="loading")
        self.loading.trace('w', self.WatchVars)
    
    def WatchVars(self, *args):
        if(args[0] == "image_is_set"):
            if(self.image_is_set.get() == False):
                self.toolframe.WatchToolsVar("image_unset")
            self.menuframe.Update_radioboolvar()
        if(args[0] == "square_image_boolean"):
            if(self.image_is_set.get()):
                self.Loader.Controller.UpdateImageResetPoint()
                self.toolframe.WatchToolsVar(self.toolvar.get())
        if(args[0] == "toolvar"):
            self.toolframe.WatchToolsVar(self.toolvar.get())
        if(args[0] == "channel_select" and self.image_is_set.get()):
            if(self.image_is_set.get()):
                self.Loader.Controller.UpdateImage()
        if(args[0] == "channel_intensity"):
            if(self.toolvar.get() == "cursor_tool"):
                self.toolframe.WatchToolsVar(args[0])
        if(args[0] == "loading"):
            self.menuframe.change_buttons_state()
            if(self.loading.get()):
                self.loadthread = Thread(target=self.CreateProgressBars)
                self.loadthread.start()
            else:
                self.DeleteProgressBars()

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
        self.frame_left.place(x=0, rely=0, width=200, relheight=1)
        self.toolframe = ToolFrame(self, self.frame_left)
        self.frame_rigth = tk.Frame(self.root, bd=4, bg= '#dfe3ee', highlightbackground= '#759fe6', highlightthickness=2)
        self.frame_rigth.place(x=205, rely=0, relwidth=1, relheight=1, width=-205)
        self.ImageFrame = ImageFrame(self.root, self.frame_rigth)
        self.Loader = self.ImageFrame.Loader
        self.menuframe = Menu.Menu(self)

    def checkimageload(self):
        if(self.kwargs):
            self.Loader.ImageSet(**self.kwargs)
    
    def CreateProgressBars(self):
        self.loadingbars = [CircularProgressbar(self.ImageFrame.canvasaxis0['Canvas']),CircularProgressbar(self.ImageFrame.canvasaxis1['Canvas']),CircularProgressbar(self.ImageFrame.canvasaxis2['Canvas'])]
        for item in self.loadingbars:
            item.place(relx=0.5, rely=0.5, anchor="center")

    def DeleteProgressBars(self):
        for item in self.loadingbars:
            item.close()
        self.loadthread.join()