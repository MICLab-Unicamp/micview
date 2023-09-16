import tkinter as tk
import math
import numpy as np
from PIL import Image, ImageTk
from screeninfo import get_monitors
import Components.Image_Controller as Imctrl
import Components.Images_Initializer as Iminit

square_image = False

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
        self.image_h = None
        self.image_w = None
        self.screensize = get_screensize()
        self.ScreenConfig()
        self.Frames()
        self.ImageFrame()
        self.Create_Buttons()
        self.root.mainloop()

    def CreateImages(self):
        print("CreatingImages")
        self.load_image_buttom['state'] = "disabled"
        size=math.floor(self.canvasaxis0['Label'].winfo_height())
        self.squared_image = Iminit.ImagesContainer(self.image_sitk,square=True, cube_side=size)
        self.image = Iminit.ImagesContainer(self.image_sitk, cube_side=size)
        print(self.image.volume_shape)
        image_data = Imctrl.update_POV(self.image)
        Labeled_image = [Image.fromarray(image_data[0],mode='F'),Image.fromarray(image_data[1],mode='F'),Image.fromarray(image_data[2],mode='F')]
        Imgs = [ImageTk.PhotoImage(Labeled_image[0]), ImageTk.PhotoImage(Labeled_image[1]), ImageTk.PhotoImage(Labeled_image[2])]
        self.Labeled_images = Imgs

        square_image_data = Imctrl.update_POV(self.squared_image)
        Labeled_squared_image = [Image.fromarray(square_image_data[0],mode='F'),Image.fromarray(square_image_data[1],mode='F'),Image.fromarray(square_image_data[2],mode='F')]
        Squared_Imgs = [ImageTk.PhotoImage(Labeled_squared_image[0]), ImageTk.PhotoImage(Labeled_squared_image[1]), ImageTk.PhotoImage(Labeled_squared_image[2])]
        self.Labeled_squared_images = Squared_Imgs
        print("finish")
        self.Resize_Images()
        self.canvasaxis0['Label'].bind("<Configure>", lambda e: self.Resize_Images())

    def ScreenConfig(self):
        self.root.title(self.window_name)
        self.root.configure(background= '#1e3743')
        self.root.geometry(f"{self.screensize['width']}x{self.screensize['height']}")
        self.root.resizable(True, True)
        min_w,min_h = set_minsize(screen_w=self.screensize['width'], screen_h=self.screensize['height'])
        self.root.minsize(width=min_w, height=min_h)
        self.previous_geometry = (self.root.winfo_width(), self.root.winfo_height())
        self.actual_geometry = (self.root.winfo_width(), self.root.winfo_height())

    def Frames(self):
        self.frame_bottom = tk.Frame(self.root, bd=4, bg='#dfe3ee', highlightbackground= '#759fe6', highlightthickness=2)
        self.frame_bottom.place(relx=0.19, rely=0.82, relwidth=0.8, relheight=0.17)
        self.frame_left = tk.Frame(self.root, bd=4, bg= '#dfe3ee', highlightbackground= '#759fe6', highlightthickness=2)
        self.frame_left.place(relx=0.01, rely=0.01, relwidth=0.17, relheight=0.98)
    def Create_Buttons(self):
        self.load_image_buttom = tk.Button(self.frame_left, text="Load Image", command=self.CreateImages)
        self.load_image_buttom.pack()
        self.square_image_buttom = tk.Button(self.frame_left, text="Square Image", command=self.UpdateSquareImage)
        self.square_image_buttom.pack()
        self.normal_image_buttom = tk.Button(self.frame_left, text="Normal Image", command=self.UpdateNormalImage)
        self.normal_image_buttom.pack()
    
    def UpdateSquareImage(self):
        global square_image
        square_image = True
        print(square_image)
        self.UpdateImages()
    
    def UpdateNormalImage(self):
        global square_image
        square_image = False
        print(square_image)
        self.UpdateImages()

    def ImageFrame(self):
        self.frame_top = tk.Frame(self.root, bd=4, bg= '#dfe3ee', highlightbackground= '#759fe6', highlightthickness=2)
        self.frame_top.place(relx=0.19, rely=0.01, relwidth=0.8, relheight=0.8)

        self.canvasaxis0 = self.AxisLabel(relheight=0.47, rely=0.02, relwidth=0.47, relx=0.02,fig=None)
        self.canvasaxis1 = self.AxisLabel(relheight=0.47, rely=0.02, relwidth=0.47, relx=0.52, fig=None)
        self.canvasaxis2 = self.AxisLabel(relheight=0.47, rely=0.52, relwidth=0.47, relx=0.52, fig=None)
        self.imageorientation = self.AxisLabel(relheight=0.47, rely=0.52, relwidth=0.47, relx=0.02)

    def AxisLabel(self, relheight, rely, relwidth, relx, fig=None):
        canvasaxis = tk.Canvas(self.frame_top, background="red")
        canvasaxis.place(relheight=relheight, rely=rely, relwidth=relwidth, relx=relx)
        labelaxis = tk.Label(canvasaxis, image=fig, background="lightblue")
        labelaxis.pack(expand=True, fill=tk.BOTH)
        return {"Canvas": canvasaxis, "Label": labelaxis}
    
    def UpdateImages(self, resized_window=False):
        print(self.image_h)
        if(self.image_h == None or self.image_h <= 1): # Screen Not Open Yet
            return
        global square_image
        if(not resized_window):
            self.image_w = self.canvasaxis0['Label'].winfo_width()
            self.image_h = self.canvasaxis0['Label'].winfo_height()
        if(square_image):
            new_sizes = Imctrl.ImageResizing(self.squared_image, self.image_h)
            print(self.image_h)
            print(self.image_w)
            print(new_sizes)
        else:
            new_sizes = Imctrl.ImageResizing(self.image, self.image_h)
            print(self.image_h)
            print(self.image_w)
            print(new_sizes)

        image_data = Imctrl.update_POV(self.image)
        Labeled_image = [Image.fromarray(image_data[0],mode='F'),Image.fromarray(image_data[1],mode='F'),Image.fromarray(image_data[2],mode='F')]
        Imgs = [ImageTk.PhotoImage(Labeled_image[0].resize((new_sizes["axis0_x"],new_sizes["axis0_y"]))),
                ImageTk.PhotoImage(Labeled_image[1].resize((new_sizes["axis1_x"],new_sizes["axis1_y"]))), 
                ImageTk.PhotoImage(Labeled_image[2].resize((new_sizes["axis2_x"],new_sizes["axis2_y"])))]
        self.Labeled_images = Imgs
        self.canvasaxis0['Label'].configure(image=Imgs[0])
        self.canvasaxis0['Label'].image = Imgs[0]
        self.canvasaxis1['Label'].configure(image=Imgs[1])
        self.canvasaxis1['Label'].image = Imgs[1]
        self.canvasaxis2['Label'].configure(image=Imgs[2])
        self.canvasaxis2['Label'].image = Imgs[2]
    
    def Resize_Images(self,e=None):
        self.actual_geometry = (self.root.winfo_width(), self.root.winfo_height())
        if(self.actual_geometry != self.previous_geometry):
            self.previous_geometry = (self.root.winfo_width(), self.root.winfo_height())
            self.image_w = self.canvasaxis0['Label'].winfo_width()
            self.image_h = self.canvasaxis0['Label'].winfo_height()
            self.UpdateImages(resized_window=True)