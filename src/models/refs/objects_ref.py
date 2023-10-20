from views.components.toolframe.ToolFrame import ToolFrame
from views.components.image_viewer.ImagesFrame import ImagesFrame
from views.components.menu.Menu import Menu
from views.windows.toplevels.Parent import Parent

class objects_ref_class:
    def __init__(self):
        self.__ImagesFrame = None
        self.__ToolFrame = None
        self.__Menu = None
        self.__SideWindow = None

    @property
    def ImagesFrame(self):
        if self.__ImagesFrame is not None:
            assert type(self.__ImagesFrame) is ImagesFrame
            return self.__ImagesFrame
    
    @ImagesFrame.setter
    def set_ImagesFrame(self, Object):
        assert type(Object) is ImagesFrame
        self.__ImagesFrame = Object

    @property
    def ToolFrame(self):
        if self.__ToolFrame is not None:
            assert type(self.__ToolFrame) is ToolFrame
            return self.__ToolFrame
    
    @ToolFrame.setter
    def ToolFrame(self, Object):
        assert type(Object) is ToolFrame
        self.__ToolFrame = Object

    @property
    def Menu(self):
        if self.__Menu is not None:
            assert type(self.__Menu) is Menu
            return self.__Menu
    
    @Menu.setter
    def Menu(self, Object):
        assert type(Object) is Menu
        self.__Menu = Object

    @property
    def SideWindow(self):
        if self.__SideWindow is not None:
            assert issubclass(self.__SideWindow, Parent)
            return self.__SideWindow
        
    @SideWindow.setter
    def SideWindow(self, Object):
        assert issubclass(Object, Parent)
        self.__SideWindow = Object

    @SideWindow.deleter
    def SideWindow(self):
        del self.__SideWindow
        self.__SideWindow = None