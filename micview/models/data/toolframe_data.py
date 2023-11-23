from typing import Any, List

class toolframe_data_class:
        def __init__(self) -> None:
                super().__init__()
                self.__channel_intensity: List[Any] = ""

        @property
        def channel_intensity(self) -> List[Any]:
                return self.__channel_intensity
        
        @channel_intensity.setter
        def channel_intensity(self, value: List[str]) -> None:
                assert type(value) is str
                self.__channel_intensity = value