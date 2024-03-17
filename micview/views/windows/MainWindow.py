##
# @brief: This file contains the main window of the application.
#

# Imports
import os
import site
import tkinter as tk
from PIL import Image, ImageTk
from micview.models.getters import initModels
from micview.controllers.services.screen_size.screensize import getScreensize
from micview.controllers.services.loading.loader import LoadImageFromShell
from micview.views.components.image_viewer.ImagesFrame import ImagesFrame
from micview.views.components.menu.Menu import Menu
from micview.views.components.toolframe.ToolFrame import ToolFrame

# Classes
class MainWindow(tk.Tk):
    """!
    @brief: This class represents the main window of the application.
    """
    def __init__(self, **kwargs: "dict[str, str]") -> None:
        """!
        @brief: The constructor of the class.
        @param: kwargs: dict[str, dict[str, str]] - The keyword arguments.
        @return: None
        """
        self.kwargs: dict[str, dict[str, str]] = kwargs
        super().__init__()
        self.create()
        tk.Tk.report_callback_exception = self.show_error

    def show_error(self, *args):
        tk.messagebox.showerror(title="Error", message="Unexpected error")

    def create(self) -> None:
        """!
        @brief: This method creates the main window.
        @return: None
        """
        self.configWindow()
        self.screenConfig()
        self.frames()
        self.initInput()

    def configWindow(self) -> None:
        """!
        @brief: This method configures the main window.
        @return: None
        """
        self.window_name = "MICView"
        try:
            LOGO: str = os.path.join(site.getsitepackages()[0], "micview", "assets/miclab_logo.jpg")
            self.image_icon = ImageTk.PhotoImage(image=Image.open(fp=LOGO)) 
            self.iconphoto(default=False, __image1=self.image_icon)
        except:
            pass
        initModels(master=self)

    def screenConfig(self) -> None:
        """!
        @brief: This method configures the screen.
        @return: None
        """
        self.screensize: dict[str, int] = getScreensize()
        self.title(string=self.window_name)
        self.configure(background= '#2d98da')
        self.geometry(newGeometry=f"{self.screensize['width']}x{self.screensize['height']}")
        self.resizable(width=True, height=True)
        self.minsize(width=700, height=500)

    def frames(self) -> None:
        """!
        @brief: This method creates the frames of the main window.
        @return: None
        """
        self.Left_Frame = tk.Frame(master=self, bd=4, bg= '#d1d8e0', highlightbackground= '#759fe6', highlightthickness=2)
        self.Left_Frame.place(x=0, rely=0, width=200, relheight=1)
        self.ToolFrame = ToolFrame(master=self.Left_Frame)
        self.ImagesFrame = ImagesFrame(master=self)
        self.protocol("WM_DELETE_WINDOW", self.onClose)
        self.Menu = Menu(master=self)

    def initInput(self) -> None:
        """!
        @brief: This method initializes the input.
        @return: None
        """
        if(self.kwargs):
            self.loading_process = LoadImageFromShell(**self.kwargs)
            self.loading_process.start()

    def onClose(self) -> None:
        """!
        @brief: This method is called when the window is closed.
        @return: None
        """
        self.destroy()
        exit(0)