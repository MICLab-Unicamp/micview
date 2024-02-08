##
# @brief: This file contains the ImagesFrame class, which is a tkinter Frame that contains the ImageCanvasView objects
#

# Imports
import tkinter as tk
from micview.views.components.image_viewer.ImageCanvasView import ImageCanvasView
from micview.models.getters import views

# Classes
class ImagesFrame(tk.Frame):    
    """!
    @brief: This class is a tkinter Frame that contains the ImageCanvasView objects.
    """
    def __init__(self, master: tk.Tk) -> None:
        """!
        @brief: The constructor of the class.
        @param: master: tk.Tk - The master window of the application.
        """
        self.master = master
        super().__init__(master=self.master, bd=4, bg= '#d1d8e0', highlightbackground='#759fe6', highlightthickness=2)
        self.place(x=205, rely=0, relwidth=1, relheight=1, width=-205)
        self.configFrame()
        self.createWidgets()

    def configFrame(self) -> None:
        """!
        @brief: This method configures the frame.
        @return: None
        """
        views['objects_ref'].ImagesFrame = self
        for i in range(2):
            self.rowconfigure(index=i, weight=1, minsize=150)
            self.columnconfigure(index=i, weight=1, minsize=150)

    def createWidgets(self) -> None:
        """!
        @brief: This method creates the widgets of the frame.
        @return: None
        """
        self.axial = ImageCanvasView(master=self, id=0)
        self.axial.grid(row=0, column=0, padx=5, pady=5, sticky='news')
        self.coronal = ImageCanvasView(master=self, id=1)
        self.coronal.grid(row=0, column=1, padx=5, pady=5, sticky='news')
        self.sagital = ImageCanvasView(master=self, id=2)
        self.sagital.grid(row=1, column=1, padx=5, pady=5, sticky='news')
        self.imageorientation = tk.Canvas(master=self, background='#f1f2f6')
        self.imageorientation.grid(row=1, column=0, padx=5, pady=5, sticky='news')
