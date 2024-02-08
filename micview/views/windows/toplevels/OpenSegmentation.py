##
# @brief This file contains the OpenSegmentation class, which is a child of the Parent class.
#

# Imports
from tkinter import Tk
from micview.views.windows.toplevels.Parent import Parent
from micview.controllers.services.toplevels.input_file_handler import onClosing
from micview.controllers.services.loading.loader import LoadNewMask

# Classes
class OpenSegmentation(Parent):
    """!
    @brief This class represents the OpenSegmentation class, which is a child of the Parent class.
    """
    def __init__(self, master: Tk, windowtitle: str ="Open Segmentation", type_of_file: str ="Segmentation") -> None:
        """!
        @brief The constructor of the class.
        @param master: Tk - The master window of the application.
        @param windowtitle: str - The title of the window.
        @param type_of_file: str - The type of file that the window will handle.
        @return None
        """
        super().__init__(master=master, windowtitle=windowtitle, type_of_file=type_of_file)
        self.defineClassOptions()

    def defineClassOptions(self) -> None:
        """!
        @brief This method defines the class options.
        @return None
        """
        self.openbutton.configure(command=self.submitInfos)

    def submitInfos(self) -> None:
        """!
        @brief This method submits the information to the application.
        @return None
        """
        mask: str = self.currentdirectory.get()+'/'+self.filepath.get()
        self.loading_process = LoadNewMask(mask=mask)
        self.loading_process.start()
        onClosing()