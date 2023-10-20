class toolframe_data_class:
        def __init__(self, master):
                self.__channel_intensity = ""

        @property
        def channel_intensity(self):
                return self.__channel_intensity
        
        @channel_intensity.setter
        def channel_intensity(self, value):
                assert type(value) is str
                self.__channel_intensity = value