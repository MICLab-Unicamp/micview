import tkinter as tk

class ImageFrame(tk.Canvas):
    def __init__(self,root, background="lightblue"):
        self.root = root
        self.image = None
        super().__init__(root, background=background)

    def SetImage(self, newimage):
        if(self.image is None):
            self.width = self.winfo_width()
            self.height = self.winfo_height()
            print(self.width)
            print(self.height)
            self.image = self.create_image(self.width//2,self.height//2,image=newimage)
        else:

        #self.image = self.create_image(self.width//2,self.height//2,image=newimage)        
            self.itemconfig(self.image, image=newimage)
        #self.update()