from typing import Any, List

class ToolframeDataClass:
        def __init__(self) -> None:
                super().__init__()
                self.__channel_intensity: List[Any] = ""
                self.__dirpath: str = ""

        @property
        def channel_intensity(self) -> List[Any]:
                return self.__channel_intensity
        
        @channel_intensity.setter
        def channel_intensity(self, value: List[str]) -> None:
                assert type(value) is str
                self.__channel_intensity = value

        @property
        def dirpath(self) -> str:
                return self.__dirpath

        @dirpath.setter
        def dirpath(self, value: str) -> None:
                assert type(value) is str
                self.__dirpath = value