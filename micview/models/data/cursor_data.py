class cursor_data_class:
    def __init__(self):
        self.__current_point = None

    @property
    def current_point(self):
        return self.__current_point
    
    @current_point.setter
    def current_point(self, value):
        self.__current_point = value