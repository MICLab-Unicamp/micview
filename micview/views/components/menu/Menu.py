##
# @brief: This file contains the Menu class, which is a subclass of the tk Menu class.
#

# Imports
import tkinter as tk
from micview.models.getters import views, states
from micview.controllers.services.menu.callbacks_onclick import fileWindow, segmentationWindow, setImageMetadata, setToolCursor, setToolZoom, setToolEdit, setToolContrast, setImageInfo

# Classes
class Menu(tk.Menu):
    """!
    @brief: This class is a subclass of the tk Menu class.
    """
    def __init__(self, master: tk.Tk) -> None:
        """!
        @brief: The constructor of the class.
        @param: master: tk.Tk - The master window of the application.
        """
        self.master = master
        super().__init__(master=self.master, tearoff=False, background='#4b7bec', foreground='white', activebackground='white', activeforeground='black')
        views['objects_ref'].Menu = self
        self.initSessions()
        self.master.config(menu=self)

    def initSessions(self) -> None:
        """!
        @brief: This method initializes the sessions of the menu.
        @return: None
        """
        self.fileInit()
        self.viewInit()
        self.segmentationInit()
        self.toolsView()
        self.infoView()

    def fileInit(self) -> None:
        """!
        @brief: This method initializes the file session of the menu.
        @return: None
        """
        self.file_options = tk.Menu(master=self, tearoff=False, background='#4b7bec', foreground='white')
        self.file_options.add_command(label="Open Main Image", command=fileWindow)  
        self.file_options.add_separator()  
        self.file_options.add_command(label="Exit", command=self.master.quit)  
        self.add_cascade(label="File", menu=self.file_options)

    def viewInit(self) -> None:
        """!
        @brief: This method initializes the view session of the menu.
        @return: None
        """
        self.radioboolvar = tk.BooleanVar(master=self.master, value = states['options_states'].image_is_square)
        self.view_options = tk.Menu(master=self, tearoff=False, background='#4b7bec', foreground='white')
        self.view_options.add_radiobutton(label="Original Size", variable=self.radioboolvar, value=False, command=self.callbackRadiobool, state="disabled")
        self.view_options.add_radiobutton(label="Zoom To Fit", variable=self.radioboolvar, value=True, command=self.callbackRadiobool, state="disabled")
        self.add_cascade(label="View", menu=self.view_options)
    
    def segmentationInit(self) -> None:
        """!
        @brief: This method initializes the segmentation session of the menu.
        @return: None
        """
        self.segmentation_options = tk.Menu(master=self, tearoff=False, background='#4b7bec', foreground='white')
        self.segmentation_options.add_command(label="Open Segmentation", command=segmentationWindow)
        self.add_cascade(label="Segmentation", menu=self.segmentation_options)

    def toolsView(self) -> None:
        """!
        @brief: This method initializes the tools session of the menu.
        @return: None
        """
        self.tools_options = tk.Menu(master=self, tearoff=False, background='#4b7bec', foreground='white')
        self.tools_options.add_command(label="Cursor Inspector", command=setToolCursor)
        self.tools_options.add_command(label="Zoom Inspector", command=setToolZoom)
        self.tools_options.add_command(label="Image Contrast", command=setToolContrast)
        self.tools_options.add_command(label="Edit Tool", command=setToolEdit)
        self.add_cascade(label="Tools", menu=self.tools_options)

    def infoView(self) -> None:
        """!
        @brief: This method initializes the info session of the menu.
        @return: None
        """
        self.info_options = tk.Menu(master=self.tools_options, tearoff=False, background='#4b7bec', foreground='white')
        self.info_options.add_command(label="Main Image", command=setImageInfo)
        self.info_options.add_command(label="Image Metadata", command=setImageMetadata)
        self.add_cascade(label="Info", menu=self.info_options)

    def callbackRadiobool(self) -> None:
        """!
        @brief: This method is the callback of the radioboolvar variable.
        @return: None
        """
        states['options_states'].image_is_square = self.radioboolvar.get()