import tkinter as tk
from tkinter import ttk
from src.micview.views.windows.toplevels.Parent import Parent
from src.micview.controllers.services.toplevels.input_file_handler import resizedImageHandler, onClosing
from src.micview.controllers.services.loading.loader import loadNewImage

class OpenImage(Parent):
    def __init__(self, master, windowtitle="Open Image", TypeOfFile="Image"):
        self.master = master
        super().__init__(master, windowtitle=windowtitle, TypeOfFile=TypeOfFile)
        self.DefineClassOptions()
        self.OptionsComboboxes()

    def DefineClassOptions(self):
        self.zoomorder = tk.IntVar(self, value=0, name="zoom_order")
        self.resized_image = tk.BooleanVar(self, value=False, name="resized_image")
        self.openbutton.configure(command=self.SubmitInfos)

    def OptionsComboboxes(self):
        imageformat_text = tk.Label(self, text="Image Format", font=('Helvetica', 10), anchor="w", justify="left")
        imageformat_text.place(rely=0.55, relx=0.02, relheight=0.1, relwidth=0.6)
        self.image_format= ttk.Combobox(self, values=["Normal", "Resized"], state="readonly", justify="center")
        self.image_format.option_add('*TCombobox*Listbox.Justify', 'center')
        self.image_format.set(value="Normal")
        self.image_format.bind(sequence='<<ComboboxSelected>>', func=lambda event: resizedImageHandler(event))
        self.image_format.place(rely= 0.55, relx=0.68, relheight=0.1, relwidth=0.20)

    def SubmitInfos(self):
        file=self.currentdirectory.get()+'/'+self.filepath.get()
        resized=self.resized_image.get()
        self.loading_process = loadNewImage(file=file, resized=resized)
        self.loading_process.start()
        onClosing()