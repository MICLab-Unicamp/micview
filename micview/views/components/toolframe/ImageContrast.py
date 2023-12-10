import tkinter as tk
import importlib
from types import ModuleType
from micview.controllers.services.tools.contrast_tool import changeContrast
models: ModuleType = importlib.import_module(name='micview.models.getters')

class ImageContrast:
    def __init__(self, master: tk.Tk) -> None:
        super().__init__()
        self.master: tk.Tk = master
        self.createVars()
        self.createWidgets()

    def createVars(self) -> None:
        self.min, self.max = models.data["changed_volume_data"].min_and_max_values
        self.original_min, self.original_max = models.data["original_volume_data"].min_and_max_values

    def createWidgets(self) -> None:
        self.title = tk.Label(master=self.master, text="Contrast Adjustment", font=('Cambria', 13, 'bold'), bg="#f1f2f6")
        self.title.place(x=5, y=10)
        self.minimumTitle = tk.Label(master=self.master, text="Minimum", font=('Cambria', 10, 'bold'), bg="#f1f2f6")
        self.minimumTitle.place(x=5, y=40)
        self.minimumScale = tk.Scale(master=self.master, from_=self.original_min, to=self.original_max-1, resolution=1, orient=tk.HORIZONTAL, length=100, bg="#f1f2f6", troughcolor="#ffffff", sliderlength=20, sliderrelief=tk.FLAT, command=self.updateMinimum)
        self.minimumScale.place(x=5, y=60)
        self.minimumScale.set(self.min)
        self.maximumTitle = tk.Label(master=self.master, text="Maximum", font=('Cambria', 10, 'bold'), bg="#f1f2f6")
        self.maximumTitle.place(x=5, y=105)
        self.maximumScale = tk.Scale(master=self.master, from_=self.original_min+1, to=self.original_max, resolution=1, orient=tk.HORIZONTAL, length=100, bg="#f1f2f6", troughcolor="#ffffff", sliderlength=20, sliderrelief=tk.FLAT, command=self.updateMaximum)
        self.maximumScale.place(x=5, y=125)
        self.maximumScale.set(self.max)
        self.changeButton = tk.Button(master=self.master, text="Set", font=('Cambria', 10, 'bold'), bg="#f1f2f6", command=self.setContrast)
        self.changeButton.place(x=5, y=165)

    def updateMinimum(self, value: int) -> None:
        self.min = int(value)
        if(self.min > self.max):
            self.min = self.max - 1
            self.minimumScale.set(self.min)
    
    def updateMaximum(self, value: int) -> None:
        self.max = int(value)
        if(self.max < self.min):
            self.max = self.min + 1
            self.maximumScale.set(self.max)

    def setContrast(self) -> None:
        changeContrast(min=self.min, max=self.max)