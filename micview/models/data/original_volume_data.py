from typing import Any

class original_volume_data_class:
    def __init__(self) -> None:
        super().__init__()
        self.__image_volume: Any = None
        self.__mask_volume: Any = None
        self.__num_of_channels: Any = 1

    @property
    def image_volume(self) -> Any:
        return self.__image_volume
    
    @image_volume.setter
    def image_volume(self, value: Any) -> None:
        self.__image_volume = value

    @image_volume.deleter
    def image_volume(self) -> None:
        if(hasattr(self, '__image_volume')):
            del self.__image_volume

    @property
    def mask_volume(self) -> Any:
        return self.__mask_volume
    
    @mask_volume.setter
    def mask_volume(self, value: Any) -> None:
        self.__mask_volume = value

    @mask_volume.deleter
    def mask_volume(self) -> None:
        if(hasattr(self, '__mask_volume')):
            del self.__mask_volume

    @property
    def num_of_channels(self) -> Any:
        return self.__num_of_channels
    
    @num_of_channels.setter
    def num_of_channels(self, value: Any) -> None:
        assert type(value) is int
        self.__num_of_channels = value

    @num_of_channels.deleter
    def num_of_channels(self) -> None:
        if(hasattr(self, '__num_of_channels')):
            del self.__num_of_channels