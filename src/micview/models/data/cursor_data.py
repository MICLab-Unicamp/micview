from typing import Any


class cursor_data_class:
    def __init__(self):
        self.__current_point = None
        self.__current_point_original_vol = None

    @property
    def current_point(self) -> Any | None:
        return self.__current_point
    
    @current_point.setter
    def current_point(self, value):
        self.__current_point = value

    @property
    def current_point_original_vol(self):
        return self.__current_point_original_vol
    
    @current_point_original_vol.setter
    def current_point_original_vol(self, value):
        self.__current_point_original_vol = value