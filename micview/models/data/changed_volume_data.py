from typing import Any, List

class ChangedVolumeDataClass:
    def __init__(self) -> None:
        super().__init__()
        self.__changed_image_volume: List[Any] = None
        self.__changed_mask_volume: List[Any] = None

    @property
    def changed_image_volume(self) -> List[Any]:
        return self.__changed_image_volume

    @changed_image_volume.setter
    def changed_image_volume(self, value: List[Any]) -> None:
        self.__changed_image_volume = value

    @changed_image_volume.deleter
    def changed_image_volume(self) -> None:
        if(self.__changed_image_volume is not None):
            del self.__changed_image_volume
            self.__changed_image_volume = None
    
    @property
    def changed_mask_volume(self) -> List[Any]:
        return self.__changed_mask_volume
    
    @changed_mask_volume.setter
    def changed_mask_volume(self, value: List[Any]) -> None:
        self.__changed_mask_volume = value
    
    @changed_mask_volume.deleter
    def changed_mask_volume(self) -> None:
        if(self.__changed_mask_volume is not None):
            del self.__changed_mask_volume
            self.__changed_mask_volume = None