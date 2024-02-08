##
# @brief: This file contains the Info class, which is a Toplevel window that displays the metadata of the image.
#

# Imports
import tkinter as tk
import importlib
from types import ModuleType
models: ModuleType = importlib.import_module(name='micview.models.getters')

# Classes
class Info(tk.Toplevel):
    """!
    @brief: This class creates the Info window.
    """
    def __init__(self, master: tk.Tk, windowtitle: str) -> None:
        """!
        @brief: The constructor of the class.
        @param: master: tk.Tk - The master window of the application.
        @param: windowtitle: str - The title of the window.
        @return: None
        """
        super().__init__(master=master)
        self.master = master
        self.title = windowtitle
        self.configWindow()
        self.getInfos()
        self.createWidgets()

    def configWindow(self) -> None:
        """!
        @brief: This method configures the window.
        @return: None
        """
        self.configure(background='#f1f2f6')
        self.geometry(newGeometry="400x300")
        self.resizable(width=False, height=False)
        self.transient(master=self.master)
        self.protocol(name="WM_DELETE_WINDOW", func=self.onClosing)
        self.focus_force()
        self.grab_set()

    def getInfos(self) -> None:
        """!
        @brief: This method gets the image metadata.
        @return: None
        """
        self.metadatas = models.data['files_data'].image_metadatas
        self.dimensions: tuple[str, str, str] = (self.metadatas['dim[1]'], self.metadatas['dim[2]'], self.metadatas['dim[3]'])
        self.spacing: tuple[str, str, str] = (self.metadatas['pixdim[1]'], self.metadatas['pixdim[2]'], self.metadatas['pixdim[3]'])
        self.origin: list[int, int, int] = [-1*int(self.metadatas['qoffset_x']),-1*int(self.metadatas['qoffset_y']),-1*int(self.metadatas['qoffset_z'])]
        self.intensity_range: tuple[str, str] = models.data["original_volume_data"].min_and_max_values

    def createWidgets(self) -> None:
        """!
        @brief: This method creates the widgets of the class.
        @return: None
        """
        title = tk.Label(master=self, text=f"{self.title}", font=('Helvetica', 15, 'bold'), bg="#f1f2f6",  justify="left", anchor="w")
        title.place(rely=0.02, relx=0.02, relwidth=0.9,relheight=0.1)
        dimensions = tk.Label(master=self, text=f"Dimensions: x:{self.dimensions[0]}, y:{self.dimensions[1]}, z:{self.dimensions[2]}", font=('Helvetica', 11, 'bold'), bg="#f1f2f6", justify="left", anchor="w")
        dimensions.place(rely=0.14, relx=0.02, relwidth=0.9,relheight=0.08)
        spacing = tk.Label(master=self, text=f"Spacing: x:{self.spacing[0]}, y:{self.spacing[1]}, z:{self.spacing[2]}", font=('Helvetica', 11, 'bold'), bg="#f1f2f6", justify="left", anchor="w")
        spacing.place(rely=0.26, relx=0.02, relwidth=0.9,relheight=0.08)
        origin = tk.Label(master=self, text=f"Origin: x:{self.origin[0]}, y:{self.origin[1]}, z:{self.origin[2]}", font=('Helvetica', 11, 'bold'), bg="#f1f2f6", justify="left", anchor="w")
        origin.place(rely=0.38, relx=0.02, relwidth=0.9,relheight=0.08)
        orientation = tk.Label(master=self, text=f"Orientation: LPI", font=('Helvetica', 11, 'bold'), bg="#f1f2f6", justify="left", anchor="w")
        orientation.place(rely=0.50, relx=0.02, relwidth=0.9,relheight=0.08)
        intensity_range = tk.Label(master=self, text=f"Intensity Range: min:{self.intensity_range[0]}, max:{self.intensity_range[1]}", font=('Helvetica', 11), bg="#f1f2f6", justify="left", anchor="w")
        intensity_range.place(rely=0.62, relx=0.02, relwidth=0.9,relheight=0.08)

    def onClosing(self) -> None:
        """!
        @brief: This method closes the window.
        @return: None
        """
        from micview.controllers.services.menu.callbacks_onclick import delSideWindow
        window: object = models.views['objects_ref'].SideWindow
        window.destroy()
        window.update()
        delSideWindow()