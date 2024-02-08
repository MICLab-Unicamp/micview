##
# @brief: This file contains the CursorDataClass which is used to store the current point and label under the cursor.
#

# Classes
class CursorDataClass:
    """!
    @brief: This class is used to store the current point and label under the cursor.
    """
    def __init__(self) -> None:
        super().__init__()
        self.__current_point: "tuple[int,int,int]" = None
        self.__label_under_cursor: int = 0

    @property
    def current_point(self) -> "tuple[int, int, int]":
        """!
        @brief: The getter method of the current_point property.
        @return: tuple[int, int, int]
        """
        return self.__current_point
    
    @current_point.setter
    def current_point(self, value: "tuple[int, int, int]") -> None:
        """!
        @brief: The setter method of the current_point property.
        @param: value: tuple[int, int, int] - The value to be set.
        @return: None
        """
        self.__current_point = value

    @property
    def label_under_cursor(self) -> int:
        """!
        @brief: The getter method of the label_under_cursor property.
        @return: int
        """
        return self.__label_under_cursor

    @label_under_cursor.setter
    def label_under_cursor(self, value: int) -> None:
        """!
        @brief: The setter method of the label_under_cursor property.
        @param: value: int - The value to be set.
        @return: None
        """
        self.__label_under_cursor = value