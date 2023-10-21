import tkinter as tk
from tkinter import ttk
from src.views.windows.toplevels.Parent import Parent
from src.controllers.services.toplevels.input_file_handler import zoomOrderHandler, resizedImageHandler, onClosing
from src.controllers.services.image_viewer.loader import loadNewImage

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
        self.image_format.set("Normal")
        self.image_format.bind('<<ComboboxSelected>>', resizedImageHandler)
        self.image_format.place(rely= 0.55, relx=0.68, relheight=0.1, relwidth=0.20)
        zoom_combobox_text = tk.Label(self, text="Zoom Interpolation Order", font=('Helvetica', 10), anchor="w", justify="left")
        zoom_combobox_text.place(rely=0.7, relx=0.02, relheight=0.1, relwidth=0.6)
        self.zoom_interpolation_order = ttk.Combobox(self, values=[ str(x) for x in range(6)], state="readonly", justify="center")
        self.zoom_interpolation_order.option_add('*TCombobox*Listbox.Justify', 'center')
        self.zoom_interpolation_order.set("0")
        self.zoom_interpolation_order.bind('<<ComboboxSelected>>', zoomOrderHandler)
        self.zoom_interpolation_order.place(rely= 0.7, relx=0.68, relheight=0.1, relwidth=0.10)
        print("end")

    def SubmitInfos(self):
        loadNewImage(file=self.finalpath.get(), order=self.zoomorder.get(), resized = self.resized_image.get())
        onClosing()