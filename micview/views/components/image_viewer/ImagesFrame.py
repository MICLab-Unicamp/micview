##
# @brief: This file contains the ImagesFrame class, which is a tkinter Frame that contains the ImageCanvasView objects
#

# Imports
import tkinter as tk
from micview.views.components.image_viewer.ImageCanvasView import ImageCanvasView
from micview.models.getters import views, data
from matplotlib.patches import Rectangle
import mpl_toolkits.mplot3d.art3d as art3d
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# Classes
class ImagesFrame(tk.Frame):    
    """!
    @brief: This class is a tkinter Frame that contains the ImageCanvasView objects.
    """
    def __init__(self, master: tk.Tk) -> None:
        """!
        @brief: The constructor of the class.
        @param: master: tk.Tk - The master window of the application.
        """
        self.master = master
        super().__init__(master=self.master, bd=4, bg= '#d1d8e0', highlightbackground='#759fe6', highlightthickness=2)
        self.place(x=205, rely=0, relwidth=1, relheight=1, width=-205)
        self.fig = None
        self.configFrame()
        self.createWidgets()

    def configFrame(self) -> None:
        """!
        @brief: This method configures the frame.
        @return: None
        """
        views['objects_ref'].ImagesFrame = self
        for i in range(2):
            self.rowconfigure(index=i, weight=1, minsize=150, uniform='fred')
            self.columnconfigure(index=i, weight=1, minsize=150, uniform='fred')

    def createWidgets(self) -> None:
        """!
        @brief: This method creates the widgets of the frame.
        @return: None
        """
        self.axial = ImageCanvasView(master=self, id=0)
        self.axial.grid(row=0, column=0, padx=5, pady=5, sticky='news')
        self.coronal = ImageCanvasView(master=self, id=1)
        self.coronal.grid(row=0, column=1, padx=5, pady=5, sticky='news')
        self.sagital = ImageCanvasView(master=self, id=2)
        self.sagital.grid(row=1, column=1, padx=5, pady=5, sticky='news')
        self.imageorientation = tk.Label(master=self, background='#f1f2f6')
        self.imageorientation.grid(row=1, column=0, padx=5, pady=5, sticky='news')

    def showsurface(self) -> None:
        """!
        @brief: This method renders the 3D surface to represent the image orientation.
        @return: None
        """
        self.fig = plt.figure()
        self.ax = self.fig.add_subplot(projection='3d')
        self.actual_point = data['cursor_data'].current_point
        image_shape = data['changed_volume_data'].changed_image_volume.shape[-3:]
        self.axis_x, self.axis_y, self.axis_z = image_shape
        self.ax.set_xlim(0, self.axis_x)
        self.ax.set_ylim(0, self.axis_y)
        self.ax.set_zlim(0, self.axis_z)
        self.rectangle_x = Rectangle((0, 0), self.axis_y, self.axis_z, fill=False, color="Red")
        self.rectangle_y = Rectangle((0, 0), self.axis_x, self.axis_z, fill=False, color="Blue")
        self.rectangle_z = Rectangle((0, 0), self.axis_x, self.axis_y, fill=False, color="Green")
        self.ax.add_patch(self.rectangle_x)
        self.ax.add_patch(self.rectangle_y)
        self.ax.add_patch(self.rectangle_z)
        self.get_points()
        art3d.pathpatch_2d_to_3d(self.rectangle_x, z=self.points[0], zdir="x")
        art3d.pathpatch_2d_to_3d(self.rectangle_y, z=self.points[1], zdir="y")
        art3d.pathpatch_2d_to_3d(self.rectangle_z, z=self.points[2], zdir="z")
        self.canvas = FigureCanvasTkAgg(self.fig, master=self.imageorientation)
        self.canvas.draw()
        self.canvas.get_tk_widget().pack()

    def refreshSurface(self) -> None:
        """!
        @brief: This method refreshes the 3D surface to represent the image orientation.
        @return: None
        """
        self.rectangle_x.remove()
        self.rectangle_y.remove()
        self.rectangle_z.remove()
        self.actual_point = data['cursor_data'].current_point
        self.rectangle_x = Rectangle((0, 0), self.axis_y, self.axis_z, fill=False, color="Red")
        self.rectangle_y = Rectangle((0, 0), self.axis_x, self.axis_z, fill=False, color="Blue")
        self.rectangle_z = Rectangle((0, 0), self.axis_x, self.axis_y, fill=False, color="Green")
        self.ax.add_patch(self.rectangle_x)
        self.ax.add_patch(self.rectangle_y)
        self.ax.add_patch(self.rectangle_z)
        self.get_points()
        art3d.pathpatch_2d_to_3d(self.rectangle_x, z=self.points[0], zdir="x")
        art3d.pathpatch_2d_to_3d(self.rectangle_y, z=self.points[1], zdir="y")
        art3d.pathpatch_2d_to_3d(self.rectangle_z, z=self.points[2], zdir="z")
        self.canvas.draw()

    def resetSurface(self) -> None:
        """!
        @brief: This method resets the 3D surface.
        @return: None
        """
        if(self.fig is None):
            self.showsurface()
        self.rectangle_x.remove()
        self.rectangle_y.remove()
        self.rectangle_z.remove()
        self.ax.clear()
        self.ax = None
        self.canvas.get_tk_widget().destroy()
        self.canvas = None
        self.fig = None
        self.showsurface()

    def get_points(self) -> None:
        self.points = [self.actual_point[0], self.actual_point[1], self.actual_point[2]]
        flipped: Tuple[bool] = data['files_data'].flipped_axes
        if(flipped[2]):
            self.points[0] = self.axis_x - self.points[0]
        if(flipped[1]):
            self.points[1] = self.axis_y - self.points[1]
        if(flipped[0]):
            self.points[2] = self.axis_z - self.points[2]