##
# @brief: This file contains the ImageCanvasView class, which is a subclass of the tk.Canvas class.
#

# Imports
import tkinter as tk
from micview.controllers.services.image_viewer.ImageCanvasController import ImageCanvasController

# Classes
class ImageCanvasView(tk.Canvas):
    """!
    @brief: This class is a subclass of the tk.Canvas class.
    """
    def __init__(self, master: tk.Frame, id: int) -> None:
        """!
        @brief: The constructor of the class.
        @param: master: tk.Frame - The master window of the application.
        @param: id: int - The id of the canvas.
        """
        self.master = master
        self.id: int = id
        self.controller = None
        super().__init__(master=master, background="#f1f2f6")
        self.config()

    def config(self) -> None:
        """!
        @brief: This method configures the canvas.
        @return: None
        """
        self.controller = ImageCanvasController(master=self)

    @property
    def centerX(self) -> int:
        """!
        @brief: The getter method of the centerX property.
        @return: int
        """
        return self.winfo_width() // 2
    
    @property
    def centerY(self) -> int:
        """!
        @brief: The getter method of the centerY property.
        @return: int
        """
        return self.winfo_height() // 2