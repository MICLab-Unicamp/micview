import os
import site
import tkinter as tk
from PIL import Image, ImageTk
from micview.models.getters import init_models
from micview.controllers.services.screen_size.screensize import get_screensize
from micview.controllers.services.loading.loader import loadImageFromShell
from micview.views.components.image_viewer.ImagesFrame import ImagesFrame
from micview.views.components.menu.Menu import Menu
from micview.views.components.toolframe.ToolFrame import ToolFrame

class MainWindow(tk.Tk):
    def __init__(self, **kwargs):
        self.kwargs = kwargs
        super().__init__()
        self.Create()

    def Create(self):
        self.ConfigWindow()
        self.ScreenConfig()
        self.Frames()
        self.init_input()

    def ConfigWindow(self):
        self.window_name = "MICView"
        try:
            LOGO = os.path.join(site.getsitepackages()[0], "micview", "assets/miclab_logo.jpg")
            self.image_icon = ImageTk.PhotoImage(Image.open(LOGO)) 
            self.iconphoto(False, self.image_icon)
        except:
            pass
        init_models(self)

    def ScreenConfig(self):
        self.screensize = get_screensize()
        self.title(self.window_name)
        self.configure(background= '#2d98da')
        self.geometry(f"{self.screensize['width']}x{self.screensize['height']}")
        self.resizable(True, True)
        self.minsize(width=700, height=500)

    def Frames(self):
        self.Left_Frame = tk.Frame(self, bd=4, bg= '#d1d8e0', highlightbackground= '#759fe6', highlightthickness=2)
        self.Left_Frame.place(x=0, rely=0, width=200, relheight=1)
        self.ToolFrame = ToolFrame(self.Left_Frame)
        self.ImagesFrame = ImagesFrame(self)
        self.Menu = Menu(self)

    def init_input(self):
        if(self.kwargs):
            self.loading_process = loadImageFromShell(**self.kwargs)
            self.loading_process.start()