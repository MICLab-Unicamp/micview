class changed_volume_data_class:
    def __init__(self):
        self.__changed_image_volume = None
        self.__changed_mask_volume = None
        self.__zoom_factors = None

    @property
    def changed_image_volume(self):
        return self.__changed_image_volume
    
    @changed_image_volume.setter
    def changed_image_volume(self, value):
        self.__changed_image_volume = value

    @changed_image_volume.deleter
    def changed_image_volume(self):
        del self.__changed_image_volume
    
    @property
    def changed_mask_volume(self):
        return self.__changed_mask_volume
    
    @changed_mask_volume.setter
    def changed_mask_volume(self, value):
        self.__changed_mask_volume = value
    
    @changed_mask_volume.deleter
    def changed_mask_volume(self):
        del self.__changed_mask_volume

    @property
    def zoom_factors(self):
        return self.__zoom_factors
    
    @zoom_factors.setter
    def zoom_factors(self, value):
        self.__zoom_factors = value

    @zoom_factors.deleter
    def zoom_factors(self):
        del self.__zoom_factors