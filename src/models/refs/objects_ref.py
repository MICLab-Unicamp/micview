class objects_ref_class:
    def __init__(self):
        self.__ImagesFrame = None
        self.__ToolFrame = None
        self.__Menu = None
        self.__SideWindow = None

    @property
    def ImagesFrame(self):
        if self.__ImagesFrame is not None:
            return self.__ImagesFrame
    
    @ImagesFrame.setter
    def ImagesFrame(self, Object):
        self.__ImagesFrame = Object

    @property
    def ToolFrame(self):
        if self.__ToolFrame is not None:
            return self.__ToolFrame
    
    @ToolFrame.setter
    def ToolFrame(self, Object):
        self.__ToolFrame = Object

    @property
    def Menu(self):
        if self.__Menu is not None:
            return self.__Menu
    
    @Menu.setter
    def Menu(self, Object):
        self.__Menu = Object

    @property
    def SideWindow(self):
        if self.__SideWindow is not None:
            return self.__SideWindow
        
    @SideWindow.setter
    def SideWindow(self, Object):
        self.__SideWindow = Object

    @SideWindow.deleter
    def SideWindow(self):
        del self.__SideWindow
        self.__SideWindow = None