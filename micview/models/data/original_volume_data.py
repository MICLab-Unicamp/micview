##
# @brief: This file contains the class that holds the original volume data.
#

# Imports
from typing import Any

# Classes
class OriginalVolumeDataClass:
    """!
    @brief: This class is used to store the original volume data.
    @details: This class is used to store the original volume data.
    """
    def __init__(self) -> None:
        """!
        @brief: The constructor of the class.
        """
        super().__init__()
        self.__image_volume: Any = None
        self.__mask_volume: Any = None
        self.__num_of_channels: int = 1
        self.__min_and_max_values: tuple[float, float] = (0, 0)

    @property
    def image_volume(self) -> Any:
        """!
        @brief: The getter method of the image_volume property.
        @return: Any
        """
        return self.__image_volume
    
    @image_volume.setter
    def image_volume(self, value: Any) -> None:
        """!
        @brief: The setter method of the image_volume property.
        @param: value: Any - The value to be set.
        @return: None
        """
        self.__image_volume = value

    @image_volume.deleter
    def image_volume(self) -> None:
        """!
        @brief: The deleter method of the image_volume property.
        @return: None
        """
        if(self.__image_volume is not None):
            del self.__image_volume
            self.__image_volume = None

    @property
    def mask_volume(self) -> Any:
        """!
        @brief: The getter method of the mask_volume property.
        @return: Any
        """
        return self.__mask_volume
    
    @mask_volume.setter
    def mask_volume(self, value: Any) -> None:
        """!
        @brief: The setter method of the mask_volume property.
        @param: value: Any - The value to be set.
        @return: None
        """
        self.__mask_volume = value

    @mask_volume.deleter
    def mask_volume(self) -> None:
        """!
        @brief: The deleter method of the mask_volume property.
        @return: None
        """
        if(self.__mask_volume is not None):
            del self.__mask_volume
            self.__mask_volume = None

    @property
    def num_of_channels(self) -> Any:
        """!
        @brief: The getter method of the num_of_channels property.
        @return: Any
        """
        return self.__num_of_channels
    
    @num_of_channels.setter
    def num_of_channels(self, value: Any) -> None:
        """!
        @brief: The setter method of the num_of_channels property.
        @param: value: Any - The value to be set.
        @return: None
        """
        assert type(value) is int
        self.__num_of_channels = value

    @num_of_channels.deleter
    def num_of_channels(self) -> None:
        """!
        @brief: The deleter method of the num_of_channels property.
        @return: None
        """
        if(hasattr(self, '__num_of_channels')):
            del self.__num_of_channels

    @property
    def min_and_max_values(self) -> "tuple[float, float]":
        """!
        @brief: The getter method of the min_and_max_values property.
        @return: "tuple[float, float]"
        """
        return self.__min_and_max_values
    
    @min_and_max_values.setter
    def min_and_max_values(self, value: "tuple[float, float]") -> None:
        """!
        @brief: The setter method of the min_and_max_values property.
        @param: value: "tuple[float, float]" - The value to be set.
        @return: None
        """
        assert type(value) is tuple
        assert len(value) == 2
        self.__min_and_max_values = value