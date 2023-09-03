import tkinter as tk
from PIL import ImageTk

class MainFrame():
    def __init__(self, image, window_name):
        self.root = tk.Tk()
        Img = ImageTk.PhotoImage(image)
        self.image = Img
        self.window_name = window_name
        self.ScreenConfig()
        self.Frames()
        self.root.mainloop()
    def ScreenConfig(self):
        self.root.title(self.window_name)
        self.root.configure(background= '#1e3743')
        self.root.geometry("700x600")
        self.root.resizable(True, True)
        self.root.maxsize(width=1500, height=1500)
        self.root.minsize(width=500, height=300)
    def Frames(self):
        self.frame_1 = tk.Frame(self.root, bd=4, bg= '#dfe3ee', highlightbackground= '#759fe6', highlightthickness=2)
        self.frame_1.place(relx=0.02, rely=0.02, relwidth=0.96, relheight=0.46)
        self.frame_2 = tk.Frame(self.root, bd=4, bg='#dfe3ee', highlightbackground= '#759fe6', highlightthickness=2)
        self.frame_2.place(relx=0.02, rely=0.5, relwidth=0.96, relheight=0.46)
        label = tk.Label(self.frame_1, image=self.image)
        label.pack(expand=True, fill=tk.BOTH)
