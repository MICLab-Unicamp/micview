import tkinter as tk
from micview.models.getters import views, states
from micview.controllers.services.menu.callbacks_onclick import FileWindow, SegmentationWindow

class Menu(tk.Menu):
    def __init__(self, master):
        self.master = master
        super().__init__(self.master, tearoff=False, background='#4b7bec', foreground='white', activebackground='white', activeforeground='black')
        views['objects_ref'].Menu = self
        self.init_sessions()
        self.master.config(menu=self)

    def init_sessions(self):
        self.file_init()
        self.view_init()
        self.segmentation_init()
        self.edit_view()
        self.tools_view()

    def file_init(self):
        self.file_options = tk.Menu(self, tearoff=False, background='#4b7bec', foreground='white')
        self.file_options.add_command(label="Open Main Image", command=FileWindow)  
        self.file_options.add_separator()  
        self.file_options.add_command(label="Exit", command=self.master.quit)  
        self.add_cascade(label="File", menu=self.file_options)

    def view_init(self):
        self.radioboolvar = tk.BooleanVar(self.master, states['options_states'].image_is_square)
        self.view_options = tk.Menu(self, tearoff=False, background='#4b7bec', foreground='white')
        self.view_options.add_radiobutton(label="Original Size", variable=self.radioboolvar, value=False, command=self.callback_radiobool, state="disabled")
        self.view_options.add_radiobutton(label="Zoom To Fit", variable=self.radioboolvar, value=True, command=self.callback_radiobool, state="disabled")
        self.add_cascade(label="View", menu=self.view_options)
    
    def segmentation_init(self):
        self.segmentation_options = tk.Menu(self, tearoff=False, background='#4b7bec', foreground='white')
        self.segmentation_options.add_command(label="Open Segmentation", command=SegmentationWindow)
        self.segmentation_options.add_command(label="Save Segmentation")
        self.add_cascade(label="Segmentation", menu=self.segmentation_options)

    def edit_view(self):
        self.edit_options = tk.Menu(self, tearoff=False, background='#4b7bec', foreground='white')
        self.edit_options.add_command(label="Polygon Mode")
        self.edit_options.add_command(label="Paintbrush Mode")
        self.add_cascade(label="Edit", menu=self.edit_options)

    def tools_view(self):
        self.tools_options = tk.Menu(self, tearoff=False, background='#4b7bec', foreground='white')
        self.tools_options.add_command(label="Cursor Inspector")
        self.tools_options.add_command(label="Zoom Inspector")
        self.tools_options.add_command(label="Image Contrast")
        self.tools_options.add_command(label="Segmentation Opacity")

        self.info_options = tk.Menu(self.tools_options, tearoff=False, background='#4b7bec', foreground='white')
        self.info_options.add_command(label="Main Image")
        self.info_options.add_command(label="Segmentation")
        self.tools_options.add_cascade(label="Info", menu=self.info_options)

        self.tools_options.add_command(label="Image Metadata")
        self.add_cascade(label="Tools", menu=self.tools_options)

    def callback_radiobool(self):
        states['options_states'].image_is_square = self.radioboolvar.get()
