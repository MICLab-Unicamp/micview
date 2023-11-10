import tkinter as tk
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
        self.window_name = "MICView"
        init_models(self)
        self.ScreenConfig()
        self.Frames()
        self.init_input()

    def ScreenConfig(self):
        self.screensize = get_screensize()
        self.title(self.window_name)
        self.configure(background= '#1e3743')
        self.geometry(f"{self.screensize['width']}x{self.screensize['height']}")
        self.resizable(True, True)
        self.minsize(width=700, height=500)

    def Frames(self):
        self.Left_Frame = tk.Frame(self, bd=4, bg= '#dfe3ee', highlightbackground= '#759fe6', highlightthickness=2)
        self.Left_Frame.place(x=0, rely=0, width=200, relheight=1)
        self.ToolFrame = ToolFrame(self.Left_Frame)
        self.ImagesFrame = ImagesFrame(self)
        self.Menu = Menu(self)

    def init_input(self):
        if(self.kwargs):
            self.loading_process = loadImageFromShell(**self.kwargs)
            self.loading_process.start()