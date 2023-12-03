class CursorDataClass:
    def __init__(self) -> None:
        super().__init__()
        self.__current_point: "tuple[int,int,int]" = None

    @property
    def current_point(self) -> "tuple[int, int, int]":
        return self.__current_point
    
    @current_point.setter
    def current_point(self, value: "tuple[int, int, int]") -> None:
        self.__current_point = value