from tkinter import Tk
from micview.views.windows.toplevels.Parent import Parent
from micview.controllers.services.toplevels.input_file_handler import onClosing
from micview.controllers.services.loading.loader import loadNewMask

class OpenSegmentation(Parent):
    def __init__(self, master: Tk, windowtitle: str ="Open Segmentation", type_of_file: str ="Segmentation") -> None:
        super().__init__(master=master, windowtitle=windowtitle, type_of_file=type_of_file)
        self.defineClassOptions()

    def defineClassOptions(self) -> None:
        self.openbutton.configure(command=self.submitInfos)

    def submitInfos(self) -> None:
        mask: str = self.currentdirectory.get()+'/'+self.filepath.get()
        self.loading_process = loadNewMask(mask=mask)
        self.loading_process.start()
        onClosing()