import tkinter as tk
import math
from screeninfo import get_monitors
from Components.ImageFrame import *
import Components.ImageFrame_Update as Imupdate
import Components.Volume_Controller as Volctrl

def get_screensize():
    arr = get_monitors()
    for monitor in arr:
        if(monitor.is_primary):
            return {"width": monitor.width, "height": monitor.height}
    return {"width": arr[0].width, "height": arr[0].height}

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
        self.ImageFrame = ImageFrame(self.frame_rigth)
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
        self.frame_bottom.place(relx=0.19, rely=0.85, relwidth=0.8, relheight=0.14)
        self.frame_left = tk.Frame(self.root, bd=4, bg= '#dfe3ee', highlightbackground= '#759fe6', highlightthickness=2)
        self.frame_left.place(relx=0.005, rely=0, relwidth=0.18, relheight=0.99)
        self.frame_rigth = tk.Frame(self.root, bd=4, bg= '#dfe3ee', highlightbackground= '#759fe6', highlightthickness=2)
        self.frame_rigth.place(relx=0.19, rely=0, relwidth=0.8, relheight=0.84)
        self.menu = tk.Menu(self.root, background='#ff8000', foreground='black', activebackground='white', activeforeground='black')  
        self.Create_Notebook()

    def Create_Notebook(self):
        file = tk.Menu(self.menu, tearoff=1, background='#ffcc99', foreground='black')
        file.add_command(label="New")  
        file.add_command(label="Open")  
        file.add_command(label="Save")  
        file.add_command(label="Save as")    
        file.add_separator()  
        file.add_command(label="Exit", command=self.root.quit)  
        self.menu.add_cascade(label="File", menu=file)  
        self.root.config(menu=self.menu)
        '''

edit = Menu(menubar, tearoff=0)  
edit.add_command(label="Undo")  
edit.add_separator()     
edit.add_command(label="Cut")  
edit.add_command(label="Copy")  
edit.add_command(label="Paste")  
menubar.add_cascade(label="Edit", menu=edit)  

minimap = BooleanVar()
minimap.set(True)
darkmode = BooleanVar()
darkmode.set(False)

view = Menu(menubar, tearoff=0)
view.add_checkbutton(label="show minimap", onvalue=1, offvalue=0, variable=minimap)
view.add_checkbutton(label='Darkmode', onvalue=1, offvalue=0, variable=darkmode, command=darkMode)
menubar.add_cascade(label='View', menu=view)

help = Menu(menubar, tearoff=0)  
help.add_command(label="About", command=about)  
menubar.add_cascade(label="Help", menu=help)  
    
ws.config(menu=menubar)
        '''

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

    def SquareImageButtonHandler(self): ###Tratar erro futuramente
        Square_Image_True()
        Volctrl.reset_current_point()
        Imupdate.UpdateImages(self.ImageFrame.Controller, True)

    def NormalImageButtonHandler(self):
        Square_Image_False()
        Volctrl.reset_current_point()
        Imupdate.UpdateImages(self.ImageFrame.Controller, False)