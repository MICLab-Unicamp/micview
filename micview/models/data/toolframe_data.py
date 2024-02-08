##
# @brief: This file contains the ToolframeDataClass which is a data class for the toolframe data.
#

# Imports
from typing import Any, List

# Classes
class ToolframeDataClass:
        """!
        @brief: This class is a data class for the toolframe data.
        """
        def __init__(self) -> None:
          """!
          @brief: The constructor of the class.
          """
          super().__init__()
          self.__channel_intensity: List[Any] = ""
          self.__dirpath: str = ""

        @property
        def channel_intensity(self) -> List[Any]:
          """!
          @brief: The getter method of the channel_intensity property.
          @return: List[Any]
          """
          return self.__channel_intensity

        @channel_intensity.setter
        def channel_intensity(self, value: List[str]) -> None:
                """!
                @brief: The setter method of the channel_intensity property.
                @param: value: List[str] - The value to be set.
                @return: None
                """
                assert type(value) is str
                self.__channel_intensity = value

        @property
        def dirpath(self) -> str:
                """!
                @brief: The getter method of the dirpath property.
                @return: str
                """
                return self.__dirpath

        @dirpath.setter
        def dirpath(self, value: str) -> None:
                """!
                @brief: The setter method of the dirpath property.
                @param: value: str - The value to be set.
                @return: None
                """
                assert type(value) is str
                self.__dirpath = value