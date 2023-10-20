class original_volume_data_class:
    def __init__(self, master):
        self.__image_volume = None
        self.__mask_volume = None
        self.__num_of_channels = 1

    @property
    def image_volume(self):
        return self.__image_volume
    
    @image_volume.setter
    def image_volume(self, value):
        self.__image_volume = value

    @image_volume.deleter
    def image_volume(self):
        del self.__image_volume

    @property
    def mask_volume(self):
        return self.__mask_volume
    
    @mask_volume.setter
    def mask_volume(self, value):
        self.__mask_volume = value

    @mask_volume.deleter
    def mask_volume(self):
        del self.__mask_volume

    @property
    def num_of_channels(self):
        return self.__num_of_channels
    
    @num_of_channels.setter
    def num_of_channels(self, value):
        assert type(value) is int
        self.__num_of_channels = value

    @num_of_channels.deleter
    def num_of_channels(self):
        del self.__num_of_channels