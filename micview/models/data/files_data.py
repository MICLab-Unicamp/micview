from typing import Any, Dict
import SimpleITK as sitk

class FilesDataClass:
    def __init__(self) -> None:
        super().__init__()
        self.__image_file: sitk.Image = None
        self.__mask_file: sitk.Image = None
        self.__image_metadatas: Dict[str, Any] = None
        self.__mask_metadatas: Dict[str, Any] = None
        self.__flipped_axes: tuple[int] = None
        self.__orient_text: Dict[str, Any] = None

    @property
    def image_file(self) -> sitk.Image:
        return self.__image_file
    
    @image_file.setter
    def image_file(self, value: sitk.Image) -> None:
        self.__image_file = value

    @property
    def mask_file(self) -> sitk.Image:
        return self.__mask_file
    
    @mask_file.setter
    def mask_file(self, value: sitk.Image) -> None:
        self.__mask_file = value

    @property
    def image_metadatas(self) -> Dict[str, Any]:
        return self.__image_metadatas

    @image_metadatas.setter
    def image_metadatas(self, value: Dict[str, Any]) -> None:
        self.__image_metadatas = value
    
    @property
    def mask_metadatas(self) -> Dict[str, Any]:
        return self.__mask_metadatas
    
    @mask_metadatas.setter
    def mask_metadatas(self, value: Dict[str, Any]) -> None:
        self.__mask_metadatas = value

    @property
    def flipped_axes(self) -> "tuple[int]":
        return self.__flipped_axes
    
    @flipped_axes.setter
    def flipped_axes(self, value: "tuple[int]") -> None:
        self.__flipped_axes = value

    @property
    def orient_text(self) -> Dict[str, Any]:
        return self.__orient_text

    @orient_text.setter
    def orient_text(self, value: Dict[str, Any]) -> None:
        self.__orient_text = value