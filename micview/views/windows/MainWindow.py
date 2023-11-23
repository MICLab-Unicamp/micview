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
    def __init__(self, **kwargs: "dict[str, str]") -> None:
        self.kwargs: dict[str, dict[str, str]] = kwargs
        super().__init__()
        self.Create()

    def Create(self) -> None:
        self.ConfigWindow()
        self.ScreenConfig()
        self.Frames()
        self.init_input()

    def ConfigWindow(self) -> None:
        self.window_name = "MICView"
        try:
            LOGO: str = os.path.join(site.getsitepackages()[0], "micview", "assets/miclab_logo.jpg")
            self.image_icon = ImageTk.PhotoImage(image=Image.open(fp=LOGO)) 
            self.iconphoto(default=False, __image1=self.image_icon)
        except:
            pass
        init_models(master=self)

    def ScreenConfig(self) -> None:
        self.screensize: dict[str, int] = get_screensize()
        self.title(string=self.window_name)
        self.configure(background= '#2d98da')
        self.geometry(newGeometry=f"{self.screensize['width']}x{self.screensize['height']}")
        self.resizable(width=True, height=True)
        self.minsize(width=700, height=500)

    def Frames(self) -> None:
        self.Left_Frame = tk.Frame(master=self, bd=4, bg= '#d1d8e0', highlightbackground= '#759fe6', highlightthickness=2)
        self.Left_Frame.place(x=0, rely=0, width=200, relheight=1)
        self.ToolFrame = ToolFrame(master=self.Left_Frame)
        self.ImagesFrame = ImagesFrame(master=self)
        self.Menu = Menu(master=self)

    def init_input(self) -> None:
        if(self.kwargs):
            self.loading_process = loadImageFromShell(**self.kwargs)
            self.loading_process.start()