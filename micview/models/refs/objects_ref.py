class ObjectsRefClass:
    def __init__(self) -> None:
        super().__init__()
        self.__ImagesFrame: object = None
        self.__ToolFrame: object = None
        self.__Menu: object = None
        self.__SideWindow: object = None

    @property
    def ImagesFrame(self) -> object:
        if self.__ImagesFrame is not None:
            return self.__ImagesFrame
    
    @ImagesFrame.setter
    def ImagesFrame(self, Object: object) -> None:
        self.__ImagesFrame = Object

    @property
    def ToolFrame(self) -> object:
        if self.__ToolFrame is not None:
            return self.__ToolFrame
    
    @ToolFrame.setter
    def ToolFrame(self, Object: object) -> None:
        self.__ToolFrame = Object

    @ToolFrame.deleter
    def ToolFrame(self) -> None:
        self.__ToolFrame.delActualTool()

    @property
    def Menu(self) -> object:
        if self.__Menu is not None:
            return self.__Menu
    
    @Menu.setter
    def Menu(self, Object: object) -> None:
        self.__Menu = Object

    @property
    def SideWindow(self) -> object:
        if self.__SideWindow is not None:
            return self.__SideWindow
        
    @SideWindow.setter
    def SideWindow(self, Object: object) -> None:
        self.__SideWindow = Object

    @SideWindow.deleter
    def SideWindow(self) -> None:
        del self.__SideWindow
        self.__SideWindow = None