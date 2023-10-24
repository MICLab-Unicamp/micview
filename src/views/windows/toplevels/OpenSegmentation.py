from src.views.windows.toplevels.Parent import Parent
from src.controllers.services.toplevels.input_file_handler import onClosing
from src.controllers.services.loading.loader import loadNewMask

class OpenSegmentation(Parent):
    def __init__(self, master, windowtitle="Open Segmentation", TypeOfFile="Segmentation"):
        super().__init__(master, windowtitle, TypeOfFile)
        self.DefineClassOptions()

    def DefineClassOptions(self):
        self.openbutton.configure(command=self.SubmitInfos)

    def SubmitInfos(self):
        mask = self.currentdirectory.get()+'/'+self.filepath.get()
        self.loading_process = loadNewMask(mask=mask)
        self.loading_process.start()
        onClosing()