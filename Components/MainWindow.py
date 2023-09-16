import tkinter as tk
import math
from screeninfo import get_monitors
from Components.ImageFrame import *

def get_screensize():
    for monitor in get_monitors():
        if(monitor.is_primary):
            return {"width": monitor.width, "height": monitor.height}
def set_minsize(screen_w,screen_h):
    if(screen_h < screen_w):
        return math.ceil(screen_h*2/3),math.ceil(screen_h*2/3)
    return math.ceil(screen_w*2/3),math.ceil(screen_w*2/3)

class RootFrame():
    def __init__(self, image_sitk, window_name):
        self.root = tk.Tk()
        self.window_name = window_name
        self.image_sitk = image_sitk
        self.screensize = get_screensize()
        self.ScreenConfig()
        self.Frames()
        self.Create_Buttons()
        self.ImageFrame = ImageFrame(self.frame_top)
        self.root.mainloop()

    def ScreenConfig(self):
        self.root.title(self.window_name)
        self.root.configure(background= '#1e3743')
        self.root.geometry(f"{self.screensize['width']}x{self.screensize['height']}")
        self.root.resizable(True, True)
        min_w,min_h = set_minsize(screen_w=self.screensize['width'], screen_h=self.screensize['height'])
        self.root.minsize(width=min_w, height=min_h)

    def Frames(self):
        self.frame_bottom = tk.Frame(self.root, bd=4, bg='#dfe3ee', highlightbackground= '#759fe6', highlightthickness=2)
        self.frame_bottom.place(relx=0.19, rely=0.82, relwidth=0.8, relheight=0.17)
        self.frame_left = tk.Frame(self.root, bd=4, bg= '#dfe3ee', highlightbackground= '#759fe6', highlightthickness=2)
        self.frame_left.place(relx=0.01, rely=0.01, relwidth=0.17, relheight=0.98)
        self.frame_top = tk.Frame(self.root, bd=4, bg= '#dfe3ee', highlightbackground= '#759fe6', highlightthickness=2)
        self.frame_top.place(relx=0.19, rely=0.01, relwidth=0.8, relheight=0.8)

    def Create_Buttons(self):
        self.load_image_buttom = tk.Button(self.frame_left, text="Load Image", command=self.LoadImageButtonHandler)
        self.load_image_buttom.pack()
        self.square_image_buttom = tk.Button(self.frame_left, text="Adjust to Window", command=self.SquareImageButtonHandler)
        self.square_image_buttom.pack()
        self.normal_image_buttom = tk.Button(self.frame_left, text="Normal Image", command=self.NormalImageButtonHandler)
        self.normal_image_buttom.pack()

    def LoadImageButtonHandler(self):
        self.load_image_buttom['state'] = "disabled"
        self.ImageFrame.Load_Images(self.image_sitk)

    def SquareImageButtonHandler(self):
        self.ImageFrame.UpdateSquareImage()

    def NormalImageButtonHandler(self):
        self.ImageFrame.UpdateNormalImage()