import tkinter as tk
from threading import Thread

from services.window_resizing.screensize import get_screensize,set_minsize
from components.image_viewer.ImagesFrame import ImagesFrame
from components.menu.Menu import Menu
from components.toolframe.ToolFrame import ToolFrame

class MainWindow(Thread):
    def __init__(self, **kwargs):
        self.window_name = "MICview"
        self.kwargs = kwargs
        self.root = tk.Tk()
        self.CreateGlobalVars()
        self.ScreenConfig()
        self.Frames()
        self.root.after(200, self.checkimageload)
        self.root.mainloop()

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
        self.ImagesContainer = ImagesContainer(self.root, self.frame_rigth)
        self.Loader = self.ImagesContainer.Loader
        self.menuframe = Menu.Menu(self)

    def checkimageload(self):
        if(self.kwargs):
            self.Loader.ImageSet(**self.kwargs)
    
    def CreateProgressBars(self):
        self.loadingbars = [CircularProgressbar(self.ImagesContainer.axis0),CircularProgressbar(self.ImagesContainer.axis1),CircularProgressbar(self.ImagesContainer.axis2)]
        for item in self.loadingbars:
            item.place(relx=0.5, rely=0.5, anchor="center")

    def DeleteProgressBars(self):
        for item in self.loadingbars:
            item.close()
        self.loadthread.join()

'''
 def WatchVars(self, *args):
        if(args[0] == "image_is_set"):
            if(self.image_is_set.get() == False):
                self.toolframe.WatchToolsVar("image_unset")
            self.menuframe.Update_radioboolvar()
        if(args[0] == "seg_is_set"):
            print("setting segmentation")
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
'''