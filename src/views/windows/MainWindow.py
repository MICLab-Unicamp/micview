import tkinter as tk
from threading import Thread
from src.models.models import init_models
from src.controllers.services.screen_size.screensize import get_screensize
from src.controllers.services.image_viewer.loader import loadImageFromShell
from src.views.components.image_viewer.ImagesFrame import ImagesFrame
from src.views.components.menu.Menu import Menu
from src.views.components.toolframe.ToolFrame import ToolFrame

class MainWindow(Thread):
    def __init__(self, **kwargs):
        self.kwargs = kwargs
        super().__init__()
        self.start()
        self.Create()

    def Create(self):
        self.window_name = "MICView"
        self.root = tk.Tk()
        init_models(self.root)
        self.ScreenConfig()
        self.Frames()
        self.root.after(500, self.init_input)
        self.root.mainloop()

    def ScreenConfig(self):
        self.screensize = get_screensize()
        self.root.title(self.window_name)
        self.root.configure(background= '#1e3743')
        self.root.geometry(f"{self.screensize['width']}x{self.screensize['height']}")
        self.root.resizable(True, True)
        self.root.minsize(width=700, height=500)

    def Frames(self):
        self.Left_Frame = tk.Frame(self.root, bd=4, bg= '#dfe3ee', highlightbackground= '#759fe6', highlightthickness=2)
        self.Left_Frame.place(x=0, rely=0, width=200, relheight=1)
        self.ToolFrame = ToolFrame(self.Left_Frame)
        self.ImagesFrame = ImagesFrame(self.root)
        self.Menu = Menu(self.root)

    def init_input(self):
        if(self.kwargs):
            loadImageFromShell(**self.kwargs)