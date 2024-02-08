##
# @brief: This file contains the OpenImage class, which is a child class of the Parent class.
#

# Imports
import tkinter as tk
from tkinter import ttk
from micview.views.windows.toplevels.Parent import Parent
from micview.controllers.services.toplevels.input_file_handler import resizedImageHandler, onClosing
from micview.controllers.services.loading.loader import LoadNewImage

# Classes
class OpenImage(Parent):
    """!
    @brief: This class represents the OpenImage class, which is a child class of the Parent class.
    """
    def __init__(self, master: tk.Tk, windowtitle: str ="Open Image", type_of_file: str ="Image") -> None:
        """!
        @brief: The constructor of the class.
        @param master: tk.Tk - The master window of the application.
        @param windowtitle: str - The title of the window.
        @param type_of_file: str - The type of file that the window will handle.
        @return: None
        """
        self.master = master
        super().__init__(master=master, windowtitle=windowtitle, type_of_file=type_of_file)
        self.defineClassOptions()
        self.optionsComboboxes()

    def defineClassOptions(self) -> None:
        """!
        @brief: This method defines the class options.
        @return: None
        """
        self.zoomorder = tk.IntVar(master=self, value=0, name="zoom_order")
        self.resized_image = tk.BooleanVar(master=self, value=False, name="resized_image")
        self.openbutton.configure(command=self.submitInfos)


    def optionsComboboxes(self) -> None:
        """!
        @brief: This method creates the options comboboxes.
        @return: None
        """
        imageformat_text = tk.Label(master=self, text="Image Format", font=('Helvetica', 12, 'bold'), bg="#70a1ff", anchor="w", justify="left")
        imageformat_text.place(rely=0.55, relx=0.02, relheight=0.1, relwidth=0.6)
        self.image_format= ttk.Combobox(master=self, values=["Normal", "Resized"], state="readonly", justify="center")
        self.image_format.option_add(pattern= '*TCombobox*Listbox.Justify', value='center')
        self.image_format.set(value="Normal")
        self.image_format.bind(sequence='<<ComboboxSelected>>', func=lambda event: resizedImageHandler(event))
        self.image_format.place(rely= 0.55, relx=0.68, relheight=0.1, relwidth=0.20)


    def submitInfos(self) -> None:
        """!
        @brief: This method submits the information to the application.
        @return: None
        """
        file: str=self.currentdirectory.get()+'/'+self.filepath.get()
        resized: bool=self.resized_image.get()
        self.loading_process = LoadNewImage(file=file, resized=resized)
        self.loading_process.start()
        onClosing()
