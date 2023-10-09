import tkinter as tk
from Components.SideWindows.OpenImage import *

class Menu:
    def __init__(self, parent):
        self.parent = parent
        self.rootframe = parent.root
        self.menubar = tk.Menu(self.rootframe, tearoff=False, background='blue', foreground='white', activebackground='white', activeforeground='black')
        self.cascades()
        self.rootframe.config(menu=self.menubar)

    def cascades(self):
        self.file_init()
        self.view_init()
        self.segmentation_init()
        self.edit_view()
        self.tools_view()

    def file_init(self):
        self.file_options = tk.Menu(self.menubar, tearoff=False, background='blue', foreground='white')
        self.file_options.add_command(label="Open Main Image", command=self.OpenFileInputWindow)  
        self.file_options.add_separator()  
        self.file_options.add_command(label="Exit", command=self.rootframe.quit)  
        self.menubar.add_cascade(label="File", menu=self.file_options)

    def view_init(self):
        self.radioboolvar = tk.BooleanVar(self.rootframe, self.rootframe.getvar(name="square_image_boolean"))
        self.traceidradiobool = self.radioboolvar.trace_add("write", callback=lambda *args: self.rootframe.setvar(name="square_image_boolean", value=self.radioboolvar.get()))
        self.view_options = tk.Menu(self.menubar, tearoff=False, background='blue', foreground='white')
        self.view_options.add_radiobutton(label="Original Size", variable=self.radioboolvar, value=False, state="disabled")
        self.view_options.add_radiobutton(label="Zoom To Fit", variable=self.radioboolvar, value=True, state="disabled")
        self.menubar.add_cascade(label="View", menu=self.view_options)
    
    def Update_radioboolvar(self):
        self.radioboolvar.trace_remove("write", self.traceidradiobool)
        self.radioboolvar.set(self.rootframe.getvar(name="square_image_boolean"))
        self.traceidradiobool = self.radioboolvar.trace_add("write", callback=lambda *args: self.rootframe.setvar(name="square_image_boolean", value=self.radioboolvar.get()))

    def segmentation_init(self):
        self.segmentation_options = tk.Menu(self.menubar, tearoff=False, background='blue', foreground='white')
        self.segmentation_options.add_command(label="Open Segmentation")
        self.segmentation_options.add_command(label="Save Segmentation")
        self.menubar.add_cascade(label="Segmentation", menu=self.segmentation_options)

    def edit_view(self):
        self.edit_options = tk.Menu(self.menubar, tearoff=False, background='blue', foreground='white')
        self.edit_options.add_command(label="Polygon Mode")
        self.edit_options.add_command(label="Paintbrush Mode")
        self.menubar.add_cascade(label="Edit", menu=self.edit_options)

    def tools_view(self):
        self.tools_options = tk.Menu(self.menubar, tearoff=False, background='blue', foreground='white')
        self.tools_options.add_command(label="Cursor Inspector")
        self.tools_options.add_command(label="Zoom Inspector")
        self.tools_options.add_command(label="Image Contrast")
        self.tools_options.add_command(label="Segmentation Opacity")

        self.info_options = tk.Menu(self.tools_options, tearoff=False, background='blue', foreground='white')
        self.info_options.add_command(label="Main Image")
        self.info_options.add_command(label="Segmentation")
        self.tools_options.add_cascade(label="Info", menu=self.info_options)

        self.tools_options.add_command(label="Image Metadata")
        self.menubar.add_cascade(label="Tools", menu=self.tools_options)

    def change_buttons_state(self, *args):
        image_is_set = self.rootframe.getvar(name="image_is_set")
        state = "normal" if image_is_set else "disabled"
        self.view_options.entryconfig("Original Size", state=state)        
        self.view_options.entryconfig("Zoom To Fit", state=state)
        self.file_options.entryconfig("Open Main Image", state=state)

    def OpenFileInputWindow(self):
        self.side_window = OpenFileInputWindow(self.parent, self.rootframe)

    def DelFileInputWindow(self):
        del self.side_window