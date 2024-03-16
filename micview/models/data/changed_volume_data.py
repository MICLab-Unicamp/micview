##
# @brief: This file contains the ChangedVolumeDataClass which is used to store the changed volume data.
#

# Imports
from typing import Any, List

# Classes
class ChangedVolumeDataClass:
    """!
    @brief: This class is used to store the changed volume data.
    """
    def __init__(self) -> None:
        """!
        @brief: The constructor of the class.
        """
        super().__init__()
        self.__changed_image_volume: List[Any] = None
        self.__changed_mask_volume: List[Any] = None
        self.__pre_edit_changed_mask_volume: List[Any] = None
        self.__min_and_max_values: "tuple[float, float]" = (0, 0)

    @property
    def changed_image_volume(self) -> List[Any]:
        """!
        @brief: The getter method of the changed_image_volume property.
        @return: List[Any]
        """
        return self.__changed_image_volume

    @changed_image_volume.setter
    def changed_image_volume(self, value: List[Any]) -> None:
        """!
        @brief: The setter method of the changed_image_volume property.
        @param: value: List[Any] - The value to be set.
        @return: None
        """
        self.__changed_image_volume = value

    @changed_image_volume.deleter
    def changed_image_volume(self) -> None:
        """!
        @brief: The deleter method of the changed_image_volume property.
        @return: None
        """
        if(self.__changed_image_volume is not None):
            del self.__changed_image_volume
            self.__changed_image_volume = None
    
    @property
    def changed_mask_volume(self) -> List[Any]:
        """!
        @brief: The getter method of the changed_mask_volume property.
        @return: List[Any]
        """
        return self.__changed_mask_volume
    
    @changed_mask_volume.setter
    def changed_mask_volume(self, value: List[Any]) -> None:
        """!
        @brief: The setter method of the changed_mask_volume property.
        @param: value: List[Any] - The value to be set.
        @return: None
        """
        self.__changed_mask_volume = value
    
    @changed_mask_volume.deleter
    def changed_mask_volume(self) -> None:
        """!
        @brief: The deleter method of the changed_mask_volume property.
        @return: None
        """
        if(self.__changed_mask_volume is not None):
            del self.__changed_mask_volume
            self.__changed_mask_volume = None

    @property
    def pre_edit_changed_mask_volume(self) -> List[Any]:
        """!
        @brief: The getter method of the pre_edit_changed_mask_volume property.
        @return: List[Any]
        """
        return self.__pre_edit_changed_mask_volume

    @pre_edit_changed_mask_volume.setter
    def pre_edit_changed_mask_volume(self, value: List[Any]) -> None:
        """!
        @brief: The setter method of the pre_edit_changed_mask_volume property.
        @param: value: List[Any] - The value to be set.
        @return: None
        """
        self.__pre_edit_changed_mask_volume = value

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