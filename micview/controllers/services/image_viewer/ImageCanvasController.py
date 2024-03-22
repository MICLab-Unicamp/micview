##
# @brief: This class is responsible for handling the canvas widget that displays the image slices.
#

# Imports
from ast import Dict
import numpy as np
from PIL import Image, ImageTk
import tkinter as tk
import math
from typing import Any, Tuple, List
from micview.models.getters import states, data
from micview.controllers.services.volume.controller import changeCurrentPoint, getImageSlices, getMaskSlices
from micview.controllers.services.image_viewer.services import calcCanvasImageSize, get3DCoordinate, getEquivalentPoint, getInverseEquivalentPoint
from micview.controllers.validations.validate_point import getNearestValidPoint

# Class
class ImageCanvasController:
    """!
    @brief: This class is responsible for handling the canvas widget that displays the image slices.
    """
    def __init__(self, master: tk.Canvas) -> None:
        """!
        @brief: Constructor method
        @param master: tk.Canvas
        @return: None
        """
        super().__init__()
        self.master: tk.Canvas = master
        self.id: int = self.master.id
        self.shift: List[int, int] = [0, 0]
        self.last_clicked_coord: List[int, int] = [0,0]
        self.canvas_image_size = False
        self.proportion_factor = False
        self.image_data = None
        self.mask_data = None
        self.get_colors()

    @property
    def canvas_shape(self) -> Tuple[int, int]:
        """!
        @brief: Getter method
        @return: Tuple[int, int]
        """
        return (self.master.winfo_width(), self.master.winfo_height())

    def eventHandler(self, type: str) -> None:
        """!
        @brief: This method is used to handle the events
        @param type: str
        @return: None
        """
        if(type == "action_on_child"):
            self.refresh()
        elif(type == "update_all_childs"):
            self.actual_tool = states['toolframe_states'].selected_tool
            self.resize()

    def resize(self, e: Any = None) -> None:
        """!
        @brief: This method is used to resize the canvas widget
        @param e: Any
        @return: None
        """
        image_shape: Tuple[int] = getImageSlices(axis=self.id).shape
        self.canvas_image_size: Tuple[int, int] = calcCanvasImageSize(canvas_shape=self.canvas_shape, image_shape=image_shape)
        self.refresh()

    def click(self, e: Any) -> None:
        """!
        @brief: This method is used to handle the click event
        @param e: Any
        @return: None
        """
        if(self.actual_tool == "zoom"):
            if(int(e.type) == 4):
                self.last_clicked_coord = [e.x, e.y]
            elif(int(e.type) == 6):
                self.shift[0] -= int((e.x - self.last_clicked_coord[0])/2)
                self.last_clicked_coord[0] = e.x
                self.shift[1] -= int((e.y - self.last_clicked_coord[1])/2)
                self.last_clicked_coord[1] = e.y
            states['image_canvas_states'].update_all_childs = True
        else:
            new_point_x, new_point_y = getEquivalentPoint(canvas_shape=self.canvas_shape, canvas_image_size=self.canvas_image_size, zoom_area=self.zoom_area, e=e)
            if(new_point_x == -1 and new_point_y == -1):
                return
            valid_points: List[int] = get3DCoordinate(id=self.id, x=new_point_x, y=new_point_y)
            valid_points = getNearestValidPoint(x=valid_points[0], y=valid_points[1], z=valid_points[2])
            valid_points[self.id] = -1
            changeCurrentPoint(axis0=valid_points[0] ,axis1=valid_points[1], axis2=valid_points[2])
            self.master.delete('cross')
            if(states['toolframe_states'].selected_tool == "cursor"):
                self.drawCross()
            if(states['toolframe_states'].paint_mode):
                self.paintMode()
                states['image_canvas_states'].update_all_childs = True
                return
            states['image_canvas_states'].action_on_child = self.id

    def refresh(self) -> None:
        """!
        @brief: This method is used to refresh the canvas widget
        @return: None
        """
        self.zoomed_image()
        self.drawImage()
        self.master.delete('orient_text')
        self.drawOrientText()
        self.master.delete('cross')
        if states['options_states'].mask_is_set:
            mask_array = np.array(getMaskSlices(axis=self.id), dtype=np.uint8)
            data = np.array(mask_array)
            red, green, blue = data.T[0:3]
            mask_areas = (red > 0) | (blue > 0) | (green > 0)
            data[:,:,3][mask_areas.T] = int(255*states["toolframe_states"].transparency_level)
            self.mask_image = Image.fromarray(obj=data, mode='RGBA')
            self.zoomed_mask()
            self.drawMask()
        if(states['toolframe_states'].selected_tool == "cursor"):
            self.drawCross()
    
    def zoomed_image(self):
        """!
        @brief: This method is used to zoom the image
        @return: None
        """
        self.original_image = Image.fromarray(obj=getImageSlices(axis=self.id), mode='L')
        original_image_size = self.original_image.size
        w,h = original_image_size[0]//2, original_image_size[1]//2
        const_x, const_y = (w + self.shift[0], h + self.shift[1])
        zoom = states['toolframe_states'].zoom
        self.zoom_area = (const_x - w/zoom, const_y - h/zoom, const_x + w/zoom, const_y + h/zoom)
        self.zoomed_img = self.original_image.crop(box=self.zoom_area)
        self.image_data = ImageTk.PhotoImage(image=self.zoomed_img.resize(size=self.canvas_image_size, resample=Image.NEAREST))

    def zoomed_mask(self):
        """!
        @brief: This method is used to zoom the mask
        @return: None
        """
        self.zoomed_msk = self.mask_image.crop(box=self.zoom_area)
        self.mask_data = ImageTk.PhotoImage(image=self.zoomed_msk.resize(size=self.canvas_image_size, resample=Image.NEAREST))

    def drawImage(self) -> None:
        """!
        @brief: This method is used to draw the image
        @return: None
        """
        self.drawn_image: int = self.master.create_image((self.master.centerX, self.master.centerY), image=self.image_data, anchor="center", tags=("image",))

    def drawMask(self) -> None:
        """!
        @brief: This method is used to draw the mask
        @return: None
        """
        self.drawn_mask: int = self.master.create_image((self.master.centerX, self.master.centerY), image=self.mask_data, anchor="center", tags=("mask",))

    def get_colors(self) -> None:
        if(self.id == 0):
            self.text_colors: List[str] = ["Green", "Blue", "Green", "Blue"]
        elif(self.id == 1):
            self.text_colors: List[str] = ["Green", "Red", "Green", "Red"]
        elif(self.id == 2):
            self.text_colors: List[str] = ["Blue", "Red", "Blue", "Red"]

    def drawOrientText(self) -> None:
        """!
        @brief: This method is used to draw the orientation text
        @return: None
        """
        self.orient_text: Dict[str, Any] = data['files_data'].orient_text[self.id]
        if(self.orient_text):
            self.drawn_orient_text: int = self.master.create_text((10,self.master.centerY), text=f"{self.orient_text[0]}", font=('Cambria',15,'bold'), fill=self.text_colors[0], anchor="w", tags=("orient_text",))
            self.drawn_orient_text: int = self.master.create_text((self.master.centerX,3), text=f"{self.orient_text[1]}", font=('Cambria',13,'bold'), fill=self.text_colors[1], anchor="n", tags=("orient_text",))
            self.drawn_orient_text: int = self.master.create_text((self.canvas_shape[0] -10,self.master.centerY), text=f"{self.orient_text[2]}", fill=self.text_colors[2], font=('Cambria',15,'bold'), anchor="e", tags=("orient_text",))
            self.drawn_orient_text: int = self.master.create_text((self.master.centerX,self.canvas_shape[1] -3), text=f"{self.orient_text[3]}", fill=self.text_colors[3], font=('Cambria',13,'bold'), anchor="s", tags=("orient_text",))

    def drawCross(self) -> None:
        """!
        @brief: This method is used to draw the cross
        @return: None
        """
        x,y = getInverseEquivalentPoint(id=self.id, canvas_shape=self.canvas_shape, canvas_image_size=self.canvas_image_size, zoom_area=self.zoom_area)
        imgTop = self.canvas_shape[1]/2 - self.canvas_image_size[1]/2
        imgBottom = self.canvas_shape[1]/2 + self.canvas_image_size[1]/2
        imgLeft = self.canvas_shape[0]/2 - self.canvas_image_size[0]/2
        imgRight = self.canvas_shape[0]/2 + self.canvas_image_size[0]/2
        self.master.create_line((x, imgTop, x, imgBottom), fill="#759fe6", dash=(3,2), tags=("cross",))
        self.master.create_line((imgLeft, y, imgRight, y), fill="#759fe6", dash=(3,2), tags=("cross",))

    def paintMode(self) -> None:
        """!
        @brief: This method is used to handle the paint mode
        @param e: Any
        @return: None
        """
        x,y,z = data['cursor_data'].current_point
        brush_size = states['toolframe_states'].brush_size
        color_paint_mode = states['toolframe_states'].color_paint_mode
        for i in range(-math.floor(brush_size/2), math.floor(brush_size/2)+1):
            for j in range(-math.floor(brush_size/2), math.floor(brush_size/2)+1):
                for k in range(-math.floor(brush_size/2), math.floor(brush_size/2)+1):
                    if(math.sqrt(i**2 + j**2 + k**2) < brush_size/2):
                        try:
                            data['changed_volume_data'].changed_mask_volume[x+i, y+j, z+k] = color_paint_mode
                        except:
                            pass

    def reset_paint(self) -> None:
        """!
        @brief: This method is used to reset the paint
        @return: None
        """
        del data['changed_volume_data'].changed_mask_volume
        data['changed_volume_data'].changed_mask_volume = data['changed_volume_data'].pre_edit_changed_mask_volume.copy()
        self.refresh()