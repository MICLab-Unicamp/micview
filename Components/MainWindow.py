import tkinter as tk
from PIL import ImageTk
from screeninfo import get_monitors

def get_screensize():
    for monitor in get_monitors():
        if(monitor.is_primary):
            return {"width": monitor.width, "height": monitor.height}


class RootFrame():
    def __init__(self, image, window_name, metadata):
        self.root = tk.Tk()
        Img = ImageTk.PhotoImage(image)
        self.image = Img
        self.window_name = window_name
        self.metadata = metadata
        self.screensize = get_screensize()
        self.ScreenConfig()
        self.Frames()
        self.root.mainloop()
    def ScreenConfig(self):
        self.root.title(self.window_name)
        self.root.configure(background= '#1e3743')
        self.root.geometry(f"{self.screensize['width']}x{self.screensize['height']}")
        self.root.resizable(True, True)
        self.root.minsize(width=400, height=400)
    def Frames(self):
        self.frame_top = tk.Frame(self.root, bd=4, bg= '#dfe3ee', highlightbackground= '#759fe6', highlightthickness=2)
        self.frame_top.place(relx=0.19, rely=0.01, relwidth=0.8, relheight=0.8)
        self.frame_bottom = tk.Frame(self.root, bd=4, bg='#dfe3ee', highlightbackground= '#759fe6', highlightthickness=2)
        self.frame_bottom.place(relx=0.19, rely=0.82, relwidth=0.8, relheight=0.17)
        self.frame_left = tk.Frame(self.root, bd=4, bg= '#dfe3ee', highlightbackground= '#759fe6', highlightthickness=2)
        self.frame_left.place(relx=0.01, rely=0.01, relwidth=0.17, relheight=0.98)
        label = tk.Label(self.frame_top, image=self.image)
        label.pack(expand=True, fill=tk.BOTH)
        label.bind("<1>", lambda event: print(event))
        label.bind("<B1-Motion>", lambda event: print(event))
        print(self.metadata.GetMetaDataKeys())
        meta = tk.Label(self.frame_bottom, text=self.metadata.GetMetaDataKeys())
        meta.place(relheight=1, relwidth=1)
