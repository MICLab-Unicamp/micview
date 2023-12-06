from ast import Dict
from PIL import Image, ImageTk
import tkinter as tk
from typing import Any, Tuple, List
from micview.models.getters import states, data
from micview.controllers.services.volume.controller import changeCurrentPoint, getImageSlices, getMaskSlices
from micview.controllers.services.image_viewer.services import calcCanvasImageSize, calcProportionFactor, get3DCoordinate, getEquivalentPoint
from micview.controllers.validations.validate_point import getNearestValidPoint

class ImageCanvasController:
    def __init__(self, master: tk.Canvas) -> None:
        super().__init__()
        self.master: tk.Canvas = master
        self.id: int = self.master.id
        self.canvas_image_size = False
        self.proportion_factor = False
        self.image_data = None
        self.mask_data = None

    @property
    def canvas_shape(self) -> Tuple[int, int]:
        return (self.master.winfo_width(), self.master.winfo_height())

    def eventHandler(self, type: str) -> None: #when other child suffer click
        if(type == "action_on_child"):
            self.refresh()
        elif(type == "update_all_childs"):
            self.resize()

    def resize(self, e: Any = None) -> None:#Resizes the canvas widget
        image_shape: Tuple[int] = getImageSlices(axis=self.id).shape
        self.canvas_image_size: Tuple[int, int] = calcCanvasImageSize(canvas_shape=self.canvas_shape, image_shape=image_shape)
        self.refresh()

    def click(self, e: Any) -> None:#Handles clicks on canvas
        self.proportion_factor: Tuple[float, float] = calcProportionFactor(id=self.id, canvas_image_size=self.canvas_image_size)
        new_point_x, new_point_y = getEquivalentPoint(canvas_shape=self.canvas_shape, canvas_image_size=self.canvas_image_size, proportion_factor=self.proportion_factor, e=e)
        if(new_point_x == -1 and new_point_y == -1):
            return
        valid_points: List[int] = get3DCoordinate(id=self.id, x=new_point_x, y=new_point_y)
        valid_points = getNearestValidPoint(x=valid_points[0], y=valid_points[1], z=valid_points[2])
        valid_points[self.id] = -1
        changeCurrentPoint(axis0=valid_points[0] ,axis1=valid_points[1], axis2=valid_points[2])
        self.master.delete('cross')
        self.drawCross()
        states['image_canvas_states'].action_on_child = self.id

    def refresh(self) -> None:# Refreshs the canvas objects
        self.image_data = ImageTk.PhotoImage(image=Image.fromarray(obj=getImageSlices(axis=self.id), mode='L').resize(size=self.canvas_image_size, resample=Image.NEAREST))
        self.proportion_factor: Tuple[float, float] = calcProportionFactor(id=self.id, canvas_image_size=self.canvas_image_size)
        self.drawImage()
        self.master.delete('orient_text')
        self.drawOrientText()
        self.master.delete('cross')
        self.drawCross()
        if states['options_states'].mask_is_set:
            self.mask_data = ImageTk.PhotoImage(image=Image.fromarray(obj=getMaskSlices(axis=self.id), mode='RGBA').resize(size=self.canvas_image_size, resample=Image.NEAREST))
            self.drawMask()

    def drawImage(self) -> None:
        self.drawn_image: int = self.master.create_image((self.master.centerX, self.master.centerY), image=self.image_data, anchor="center", tags=("image",))

    def drawMask(self) -> None:
        self.drawn_mask: int = self.master.create_image((self.master.centerX, self.master.centerY), image=self.mask_data, anchor="center", tags=("mask",))
    
    def drawOrientText(self) -> None:
        self.orient_text: Dict[str, Any] = data['files_data'].orient_text[self.id]
        self.drawn_orient_text: int = self.master.create_text((10,self.master.centerY), text=f"{self.orient_text[0]}", font=('Cambria',15,'bold'), fill="#EA2027", anchor="w", tags=("orient_text",))
        self.drawn_orient_text: int = self.master.create_text((self.master.centerX,3), text=f"{self.orient_text[1]}", font=('Cambria',13,'bold'), fill="#EA2027", anchor="n", tags=("orient_text",))
        self.drawn_orient_text: int = self.master.create_text((self.canvas_shape[0] -10,self.master.centerY), text=f"{self.orient_text[2]}", fill="#EA2027", font=('Cambria',15,'bold'), anchor="e", tags=("orient_text",))
        self.drawn_orient_text: int = self.master.create_text((self.master.centerX,self.canvas_shape[1] -3), text=f"{self.orient_text[3]}", fill="#EA2027", font=('Cambria',13,'bold'), anchor="s", tags=("orient_text",))

    def drawCross(self) -> None:
        points = data["cursor_data"].current_point
        pointX, pointY = 0, 0
        if(self.id == 0):
            pointX, pointY = points[2], points[1]
        elif(self.id == 1):
            pointX, pointY = points[2], points[0]
        elif(self.id == 2):
            pointX, pointY = points[1], points[0]
        
        imgTop = self.canvas_shape[1]/2 - self.canvas_image_size[1]/2
        imgBottom = self.canvas_shape[1]/2 + self.canvas_image_size[1]/2
        imgLeft = self.canvas_shape[0]/2 - self.canvas_image_size[0]/2
        imgRight = self.canvas_shape[0]/2 + self.canvas_image_size[0]/2
        self.master.create_line((pointX/self.proportion_factor[0]+imgLeft, imgTop, pointX/self.proportion_factor[0]+imgLeft, imgBottom), fill="#759fe6", dash=(3,2), tags=("cross",))
        self.master.create_line((imgLeft, pointY/self.proportion_factor[1]+imgTop, imgRight, pointY/self.proportion_factor[1]+imgTop), fill="#759fe6", dash=(3,2), tags=("cross",))