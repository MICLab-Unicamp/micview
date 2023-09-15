import tkinter as tk
from PIL import ImageTk
from screeninfo import get_monitors
import Components.Image_Controller as Imctrl
import Components.Images_Initializer as Iminit

def get_screensize():
    for monitor in get_monitors():
        if(monitor.is_primary):
            return {"width": monitor.width, "height": monitor.height}


class RootFrame():
    def __init__(self, image, window_name):
        self.root = tk.Tk()
        self.window_name = window_name
        self.image = image
        self.screensize = get_screensize()
        self.CreateImages()
        self.ScreenConfig()
        self.Frames()
        self.ImageFrame()
        self.root.mainloop()

    def CreateImages(self):
        Labeled_image = Imctrl.update_POV(self.image)
        Imgs = [ImageTk.PhotoImage(Labeled_image[0]), ImageTk.PhotoImage(Labeled_image[1]), ImageTk.PhotoImage(Labeled_image[2])]
        self.Labeled_images = Imgs

    def ScreenConfig(self):
        self.root.title(self.window_name)
        self.root.configure(background= '#1e3743')
        self.root.geometry(f"{self.screensize['width']}x{self.screensize['height']}")
        self.root.resizable(True, True)
        self.root.minsize(width=400, height=400)
    
    def Frames(self):
        self.frame_bottom = tk.Frame(self.root, bd=4, bg='#dfe3ee', highlightbackground= '#759fe6', highlightthickness=2)
        self.frame_bottom.place(relx=0.19, rely=0.82, relwidth=0.8, relheight=0.17)
        self.frame_left = tk.Frame(self.root, bd=4, bg= '#dfe3ee', highlightbackground= '#759fe6', highlightthickness=2)
        self.frame_left.place(relx=0.01, rely=0.01, relwidth=0.17, relheight=0.98)
    
    def ImageFrame(self):
        self.frame_top = tk.Frame(self.root, bd=4, bg= '#dfe3ee', highlightbackground= '#759fe6', highlightthickness=2)
        self.frame_top.place(relx=0.19, rely=0.01, relwidth=0.8, relheight=0.8)

        self.canvasaxis0 = self.AxisLabel(relheight=0.47, rely=0.02, relwidth=0.47, relx=0.02,fig=self.Labeled_images[0])

        self.canvasaxis0['Label'].bind("<1>", lambda event: self.UpdateImages(True))

        self.canvasaxis1 = self.AxisLabel(relheight=0.47, rely=0.02, relwidth=0.47, relx=0.52, fig=self.Labeled_images[1])
        self.canvasaxis2 = self.AxisLabel(relheight=0.47, rely=0.52, relwidth=0.47, relx=0.52, fig=self.Labeled_images[2])
        self.imageorientation = self.AxisLabel(relheight=0.47, rely=0.52, relwidth=0.47, relx=0.02)

    def AxisLabel(self, relheight, rely, relwidth, relx, fig=None):
        canvasaxis = tk.Canvas(self.frame_top, background="red")
        canvasaxis.place(relheight=relheight, rely=rely, relwidth=relwidth, relx=relx)
        labelaxis = tk.Label(canvasaxis, image=fig, background="lightblue")
        labelaxis.pack(expand=True, fill=tk.BOTH)
        return {"Canvas": canvasaxis, "Label": labelaxis}
    
    def UpdateImages(self, Adjust_to_window=False):
        if(Adjust_to_window):
            self.image = Imctrl.ImageResizing(self.image, 200)

        Labeled_image = Imctrl.update_POV(self.image)
        Imgs = [ImageTk.PhotoImage(Labeled_image[0]), ImageTk.PhotoImage(Labeled_image[1]), ImageTk.PhotoImage(Labeled_image[2])]
        self.Labeled_images = Imgs
        self.canvasaxis0['Label'].configure(image=Imgs[0])
        self.canvasaxis0['Label'].image = Imgs[0]
        self.canvasaxis1['Label'].configure(image=Imgs[1])
        self.canvasaxis1['Label'].image = Imgs[1]
        self.canvasaxis2['Label'].configure(image=Imgs[2])
        self.canvasaxis2['Label'].image = Imgs[2]