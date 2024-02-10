##
# @brief: This file contains the FilesDataClass which is used to store the image and mask files and their metadatas.
#

# Imports
from typing import Any, Dict
import SimpleITK as sitk

# Classes
class FilesDataClass:
    """!
    @brief: This class is used to store the image and mask files and their metadatas.
    @details: This class is used to store the image and mask files and their metadatas.
    """
    def __init__(self) -> None:
        """!
        @brief: The constructor of the class.
        """
        super().__init__()
        self.__image_file: sitk.Image = None
        self.__mask_file: sitk.Image = None
        self.__image_metadatas: Dict[str, Any] = None
        self.__mask_metadatas: Dict[str, Any] = None
        self.__flipped_axes: tuple[int] = (False, False, False)
        self.__orient_text: Dict[str, Any] = None

    @property
    def image_file(self) -> sitk.Image:
        """!
        @brief: The getter method of the image_file property.
        @return: sitk.Image
        """
        return self.__image_file
    
    @image_file.setter
    def image_file(self, value: sitk.Image) -> None:
        """!
        @brief: The setter method of the image_file property.
        @param: value: sitk.Image - The value to be set.
        @return: None
        """
        self.__image_file = value

    @property
    def mask_file(self) -> sitk.Image:
        """!
        @brief: The getter method of the mask_file property.
        @return: sitk.Image
        """
        return self.__mask_file
    
    @mask_file.setter
    def mask_file(self, value: sitk.Image) -> None:
        """!
        @brief: The setter method of the mask_file property.
        @param: value: sitk.Image - The value to be set.
        @return: None
        """
        self.__mask_file = value

    @property
    def image_metadatas(self) -> Dict[str, Any]:
        """!
        @brief: The getter method of the image_metadatas property.
        @return: Dict[str, Any]
        """
        return self.__image_metadatas

    @image_metadatas.setter
    def image_metadatas(self, value: Dict[str, Any]) -> None:
        """!
        @brief: The setter method of the image_metadatas property.
        @param: value: Dict[str, Any] - The value to be set.
        @return: None
        """
        self.__image_metadatas = value
    
    @property
    def mask_metadatas(self) -> Dict[str, Any]:
        """!
        @brief: The getter method of the mask_metadatas property.
        @return: Dict[str, Any]
        """
        return self.__mask_metadatas
    
    @mask_metadatas.setter
    def mask_metadatas(self, value: Dict[str, Any]) -> None:
        """!
        @brief: The setter method of the mask_metadatas property.
        @param: value: Dict[str, Any] - The value to be set.
        @return: None
        """
        self.__mask_metadatas = value

    @property
    def flipped_axes(self) -> "tuple[int]":
        """!
        @brief: The getter method of the flipped_axes property.
        @return: "tuple[int]"
        """
        return self.__flipped_axes
    
    @flipped_axes.setter
    def flipped_axes(self, value: "tuple[int]") -> None:
        """!
        @brief: The setter method of the flipped_axes property.
        @param: value: "tuple[int]" - The value to be set.
        @return: None
        """
        self.__flipped_axes = value

    @property
    def orient_text(self) -> Dict[str, Any]:
        """!
        @brief: The getter method of the orient_text property.
        @return: Dict[str, Any]
        """
        return self.__orient_text

    @orient_text.setter
    def orient_text(self, value: Dict[str, Any]) -> None:
        """!
        @brief: The setter method of the orient_text property.
        @param: value: Dict[str, Any] - The value to be set.
        @return: None
        """
        self.__orient_text = value