##
# @brief: This file contains the class that holds the references to the objects
#

# Classes
class ObjectsRefClass:
    """!
    @brief: This class is used to store the references to the objects.
    """
    def __init__(self) -> None:
        """!
        @brief: The constructor of the class.
        """
        super().__init__()
        self.__ImagesFrame: object = None
        self.__ToolFrame: object = None
        self.__Menu: object = None
        self.__SideWindow: object = None

    @property
    def ImagesFrame(self) -> object:
        """!
        @brief: The getter method of the ImagesFrame property.
        @return: object
        """
        if self.__ImagesFrame is not None:
            return self.__ImagesFrame
    
    @ImagesFrame.setter
    def ImagesFrame(self, Object: object) -> None:
        """!
        @brief: The setter method of the ImagesFrame property.
        @param: Object: object - The value to be set.
        @return: None
        """
        self.__ImagesFrame = Object

    @property
    def ToolFrame(self) -> object:
        """!
        @brief: The getter method of the ToolFrame property.
        @return: object
        """
        if self.__ToolFrame is not None:
            return self.__ToolFrame
    
    @ToolFrame.setter
    def ToolFrame(self, Object: object) -> None:
        """!
        @brief: The setter method of the ToolFrame property.
        @param: Object: object - The value to be set.
        @return: None
        """
        self.__ToolFrame = Object

    @ToolFrame.deleter
    def ToolFrame(self) -> None:
        """!
        @brief: The deleter method of the ToolFrame property.
        @return: None
        """
        self.__ToolFrame.delActualTool()

    @property
    def Menu(self) -> object:
        """!
        @brief: The getter method of the Menu property.
        @return: object
        """
        if self.__Menu is not None:
            return self.__Menu
    
    @Menu.setter
    def Menu(self, Object: object) -> None:
        """!
        @brief: The setter method of the Menu property.
        @param: Object: object - The value to be set.
        @return: None
        """
        self.__Menu = Object

    @property
    def SideWindow(self) -> object:
        """!
        @brief: The getter method of the SideWindow property.
        @return: object
        """
        if self.__SideWindow is not None:
            return self.__SideWindow
        
    @SideWindow.setter
    def SideWindow(self, Object: object) -> None:
        """!
        @brief: The setter method of the SideWindow property.
        @param: Object: object - The value to be set.
        @return: None
        """
        self.__SideWindow = Object

    @SideWindow.deleter
    def SideWindow(self) -> None:
        """!
        @brief: The deleter method of the SideWindow property.
        @return: None
        """
        del self.__SideWindow
        self.__SideWindow = None