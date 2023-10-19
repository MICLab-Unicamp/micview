from windows.side_windows.Parent import Parent
from services.sidewindows.input_file_handler import onClosing
from services.image.loader import loadNewMask

class OpenSegmentation(Parent):
    def __init__(self, master, windowtitle="Open Segmentation", TypeOfFile="Segmentation"):
        super().__init__(master, windowtitle, TypeOfFile)
        self.DefineClassOptions()

    def DefineClassOptions(self):
        self.openbutton.configure(command=self.SubmitInfos)

    def SubmitInfos(self):
        loadNewMask(mask=self.finalpath)
        onClosing()