import tkinter as tk
from PIL import ImageTk
from screeninfo import get_monitors

def get_screensize():
    for monitor in get_monitors():
        if(monitor.is_primary):
            return {"width": monitor.width, "height": monitor.height}


class RootFrame():
    def __init__(self, images, window_name):
        self.root = tk.Tk()
        self.images = images
        self.window_name = window_name
        self.screensize = get_screensize()
        self.ScreenConfig()
        self.Frames()
        self.ImageLabel()
        self.root.mainloop()
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
    
    def ImageLabel(self):
        self.frame_top = tk.Frame(self.root, bd=4, bg= '#dfe3ee', highlightbackground= '#759fe6', highlightthickness=2)
        self.frame_top.place(relx=0.19, rely=0.01, relwidth=0.8, relheight=0.8)
        ImgAxis = [ImageTk.PhotoImage(self.images[0]), ImageTk.PhotoImage(self.images[1]), ImageTk.PhotoImage(self.images[2])]
        labelaxis0 = tk.Label(self.frame_top, image=ImageTk.PhotoImage(self.images[0]),background="red")
        labelaxis0.pack(expand=True, fill=tk.BOTH)
        '''
        self.frame_top.columnconfigure(0, weight=1)
        self.frame_top.rowconfigure(0, weight=1)
        self.frame_top.columnconfigure(1, weight=1)
        self.frame_top.rowconfigure(1, weight=1)

        canvasaxis0 = tk.Canvas(self.frame_top, background="blue")
        canvasaxis0.grid(column=0, row=0, sticky=('NW'),padx=10,pady=10)
        labelaxis0 = tk.Label(canvasaxis0, image=ImgAxis[0])
        labelaxis0.pack(expand=True, fill=tk.BOTH)

        canvasaxis1 = tk.Canvas(self.frame_top, background="red")
        canvasaxis1.grid(column=1, row=0, sticky=('NE'), padx=10, pady=10)
        
        canvasaxis2 = tk.Canvas(self.frame_top, background="orange")
        canvasaxis2.grid(column=0, row=1, sticky=('SW'), padx=10, pady=10)
        
        canvasaxis3 = tk.Canvas(self.frame_top, background="pink")
        canvasaxis3.grid(column=1, row=1, sticky=('SE'), padx=10, pady=10)
        #label.pack(expand=True, fill=tk.BOTH)
        #label.bind("<1>", lambda event: print(event))
        #label.bind("<B1-Motion>", lambda event: print(event))
        '''