from tkinter import Tk
from micview.views.windows.toplevels.Parent import Parent
from micview.controllers.services.toplevels.input_file_handler import onClosing
from micview.controllers.services.loading.loader import loadNewMask

class OpenSegmentation(Parent):
    def __init__(self, master: Tk, windowtitle: str ="Open Segmentation", TypeOfFile: str ="Segmentation") -> None:
        super().__init__(master=master, windowtitle=windowtitle, TypeOfFile=TypeOfFile)
        self.DefineClassOptions()

    def DefineClassOptions(self) -> None:
        self.openbutton.configure(command=self.SubmitInfos)

    def SubmitInfos(self) -> None:
        mask: str = self.currentdirectory.get()+'/'+self.filepath.get()
        self.loading_process = loadNewMask(mask=mask)
        self.loading_process.start()
        onClosing()