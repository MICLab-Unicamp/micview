from threading import Thread
import Components.Images.ImageFrame_Update as Imupdate
import Components.Images.ImageFrame_Loader as Loader
from Components.Images.ImageFrame import *

class ImagesContainer(Thread):
    def __init__(self,root,frame):
        self.root = root
        self.frame = frame
        super().__init__()
        self.run()

    def run(self):
        self.axis0 = ImageFrame(self.frame)
        self.axis0.place(relheight=0.47, rely=0.02, relwidth=0.47, relx=0.02)
        self.axis1 = ImageFrame(self.frame)
        self.axis1.place(relheight=0.47, rely=0.02, relwidth=0.47, relx=0.52)
        self.axis2 = ImageFrame(self.frame)
        self.axis2.place(relheight=0.47, rely=0.52, relwidth=0.47, relx=0.52)
        self.imageorientation = ImageFrame(self.frame)
        self.imageorientation.place(relheight=0.47, rely=0.52, relwidth=0.47, relx=0.02)
        self.Loader = Loader.ImageFrame_Loader(self)

    def clean_screen(self):
        self.axis0.clean_screen()
        self.axis1.clean_screen()
        self.axis2.clean_screen()