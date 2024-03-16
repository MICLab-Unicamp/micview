##
# @brief: This file contains the EditTool class, which is a component of the ToolFrame class.
#

# Imports
import tkinter as tk
from tkinter import ttk, colorchooser
import importlib
from types import ModuleType
models: ModuleType = importlib.import_module(name='micview.models.getters')
from micview.controllers.services.tools.cursor_tool import handleSelectedItem, updateTransparency

pallete = [
    {'Number': 1, 'RGB': (255, 0, 0, 255)},
    {'Number': 2, 'RGB': (0, 255, 0, 255)},
    {'Number': 3, 'RGB': (0, 0, 255, 255)},
    {'Number': 4, 'RGB': (255, 255, 0, 255)},
    {'Number': 5, 'RGB': (0, 255, 255, 255)},
    {'Number': 6, 'RGB': (255, 0, 255, 255)},
    {'Number': 7, 'RGB': (255, 255, 255, 255)},
    {'Number': 8, 'RGB': (0, 0, 0, 255)}
]

# Classes
class EditTool():
    """!
    @brief: This class represents the edit tool in the toolframe.
    """
    def __init__(self, master: tk.Tk):
        super().__init__()
        self.master: tk.Tk = master
        self.createVars()
        self.createWidgets()

    def createVars(self) -> None:
        """!
        @brief This method creates the variables of the class.
        @return None
        """
        self.cursorX = tk.IntVar(master=self.master, value=0, name="cursorX")
        self.cursorY = tk.IntVar(master=self.master, value=0, name="cursorY")
        self.cursorZ = tk.IntVar(master=self.master, value=0, name="cursorZ")
        initial_label = "No Label"
        if(models.data['cursor_data'].label_under_cursor != 0):
            initial_label = f"Label {models.data['cursor_data'].label_under_cursor}"
        self.label_under_cursor = tk.StringVar(master=self.master, value=initial_label, name="label_under_cursor")

    def createWidgets(self) -> None:
        """!
        @brief This method creates the widgets of the class.
        @return None
        """
        self.title = tk.Label(master=self.master, text="Cursor Inspector", font=('Cambria', 13, 'bold'), bg="#f1f2f6")
        self.title.place(x=5, y=10)
        self.cursorpositiontitle = tk.Label(master=self.master, text="Cursor position (x,y,z):", font=('Cambria', 10), bg="#f1f2f6")
        self.cursorpositiontitle.place(x=5, y=40)
        self.posx = tk.Label(master=self.master, textvariable=self.cursorX, font=('Cambria', 8), bg="#ffffff")
        self.posx.place(x=5, y=60, width=30, height=30)
        self.posy = tk.Label(master=self.master, textvariable=self.cursorY, font=('Cambria', 8), bg="#ffffff")
        self.posy.place(x=40, y=60, width=30, height=30)
        self.posz = tk.Label(master=self.master, textvariable=self.cursorZ, font=('Cambria', 8), bg="#ffffff")
        self.posz.place(x=75, y=60, width=30, height=30)
        self.labelUnderCursorTitle = tk.Label(master=self.master, text="Label under cursor:", font=('Cambria', 10), bg="#f1f2f6")
        self.labelUnderCursorTitle.place(x=5, y=110)
        self.labelUnderCursor = tk.Label(master=self.master, textvariable=self.label_under_cursor, font=('Cambria', 8), bg="#ffffff")
        self.labelUnderCursor.place(x=5, y=130, width=90, height=30)
        self.paintButtonFalse = tk.Radiobutton(master=self.master, text="Cursor", font=('Cambria', 10, 'bold'), bg="#f1f2f6", variable=models.states['toolframe_states'].paint_mode, value=False, command=self.PaintModeFalse)
        self.paintButtonFalse.place(x=5, y=180)
        self.paintButtonTrue = tk.Radiobutton(master=self.master, text="Paint", font=('Cambria', 10, 'bold'), bg="#f1f2f6", variable=models.states['toolframe_states'].paint_mode, value=True, command=self.PaintModeTrue)
        self.paintButtonTrue.place(x=5, y=210)
        self.PaintModeTrue()
        self.selectColorButton = tk.Button(master=self.master, text="Select Color", font=('Cambria', 10, 'bold'), bg="#f1f2f6", command=self.selectColor)
        self.selectColorButton.place(x=5, y=240)
        self.brushSizeScale = tk.Scale(master=self.master, from_=1, to=20, resolution=1, orient=tk.HORIZONTAL, length=100, bg="#f1f2f6", troughcolor="#ffffff", sliderlength=20, sliderrelief=tk.FLAT, command=self.updateBrushSize)
        self.brushSizeScale.place(x=5, y=270)
        self.brushSizeScale.set(1)
        self.resetButton = tk.Button(master=self.master, text="Clear", font=('Cambria', 10, 'bold'), bg="#f1f2f6", command=self.resetDrawing)
        self.resetButton.place(x=5, y=320)
        self.backButton = tk.Button(master=self.master, text="Back", font=('Cambria', 10, 'bold'), bg="#f1f2f6", command=self.back)
        self.backButton.place(x=5, y=350)

    def PaintModeTrue(self) -> None:
        models.states['toolframe_states'].paint_mode = True
    
    def PaintModeFalse(self) -> None:
        models.states['toolframe_states'].paint_mode = False

    def selectColor(self) -> None:
        colors = colorchooser.askcolor()
        selectedColor = (colors[0][0], colors[0][1], colors[0][2], 255)
        models.states['toolframe_states'].color_paint_mode = selectedColor

    def updateBrushSize(self, value: int) -> None:
        """!
        @brief: This method is used to select the pencil size.
        @param: value: int - The new minimum value.
        @return: None
        """
        models.states['toolframe_states'].brush_size = int(value)

    def resetDrawing(self) -> None:
        """!
        @brief: This method is used to reset the drawing.
        @return: None
        """
        images_frame: object = models.views['objects_ref'].ImagesFrame
        images_frame.axial.controller.reset_paint()
        images_frame.coronal.controller.reset_paint()
        images_frame.sagital.controller.reset_paint()

    def back(self) -> None:
        """!
        @brief: This method is used to go back to cursor tool.
        @return: None
        """
        from micview.controllers.services.menu.callbacks_onclick import setToolCursor
        setToolCursor()