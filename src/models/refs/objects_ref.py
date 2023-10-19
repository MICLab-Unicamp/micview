import tkinter as tk
from components.toolframe.ToolFrame import ToolFrame
from components.image_viewer.ImagesFrame import ImagesFrame
from components.menu.Menu import Menu
from windows.side_windows.Parent import Parent

class objects_ref_class:
    def __init__(self):
        self.__ImagesFrame = None
        self.__ToolFrame = None
        self.__Menu = None
        self.__SideWindow = None

    def get_ImagesFrame(self):
        if self.__ImagesFrame is not None:
            assert type(self.__ImagesFrame) is ImagesFrame
            return self.__ImagesFrame
    
    def set_ImagesFrame(self, Object):
        assert type(Object) is ImagesFrame
        self.__ImagesFrame = Object

    def get_ToolFrame(self):
        if self.__ToolFrame is not None:
            assert type(self.__ToolFrame) is ToolFrame
            return self.__ToolFrame
    
    def set_ToolFrame(self, Object):
        assert type(Object) is ToolFrame
        self.__ToolFrame = Object

    def get_Menu(self):
        if self.__Menu is not None:
            assert type(self.__Menu) is Menu
            return self.__Menu
    
    def set_Menu(self, Object):
        assert type(Object) is Menu
        self.__Menu = Object

    def get_SideWindow(self):
        if self.__SideWindow is not None:
            assert issubclass(self.__SideWindow, Parent)
            return self.__SideWindow
        
    def set_SideWindow(self, Object):
        assert issubclass(Object, Parent)
        self.__SideWindow = Object

    def del_SideWindow(self):
        del self.__SideWindow
        self.__SideWindow = None