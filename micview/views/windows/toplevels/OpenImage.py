import tkinter as tk
from tkinter import ttk
from micview.views.windows.toplevels.Parent import Parent
from micview.controllers.services.toplevels.input_file_handler import resizedImageHandler, onClosing
from micview.controllers.services.loading.loader import LoadNewImage

class OpenImage(Parent):
    def __init__(self, master: tk.Tk, windowtitle: str ="Open Image", type_of_file: str ="Image") -> None:
        self.master = master
        super().__init__(master=master, windowtitle=windowtitle, type_of_file=type_of_file)
        self.defineClassOptions()
        self.optionsComboboxes()

    def defineClassOptions(self) -> None:
        self.zoomorder = tk.IntVar(master=self, value=0, name="zoom_order")
        self.resized_image = tk.BooleanVar(master=self, value=False, name="resized_image")
        self.openbutton.configure(command=self.submitInfos)

    def optionsComboboxes(self) -> None:
        imageformat_text = tk.Label(master=self, text="Image Format", font=('Helvetica', 12, 'bold'), bg="#70a1ff", anchor="w", justify="left")
        imageformat_text.place(rely=0.55, relx=0.02, relheight=0.1, relwidth=0.6)
        self.image_format= ttk.Combobox(master=self, values=["Normal", "Resized"], state="readonly", justify="center")
        self.image_format.option_add(pattern= '*TCombobox*Listbox.Justify', value='center')
        self.image_format.set(value="Normal")
        self.image_format.bind(sequence='<<ComboboxSelected>>', func=lambda event: resizedImageHandler(event))
        self.image_format.place(rely= 0.55, relx=0.68, relheight=0.1, relwidth=0.20)

    def submitInfos(self) -> None:
        file: str=self.currentdirectory.get()+'/'+self.filepath.get()
        resized: bool=self.resized_image.get()
        self.loading_process = LoadNewImage(file=file, resized=resized)
        self.loading_process.start()
        onClosing()
