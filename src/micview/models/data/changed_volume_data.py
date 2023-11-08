class changed_volume_data_class:
    def __init__(self):
        self.__changed_image_volume = None
        self.__changed_mask_volume = None

    @property
    def changed_image_volume(self):
        return self.__changed_image_volume
    
    @changed_image_volume.setter
    def changed_image_volume(self, value):
        self.__changed_image_volume = value

    @changed_image_volume.deleter
    def changed_image_volume(self):
        if(hasattr(self, '__changed_image_volume')):
            del self.__changed_image_volume
    
    @property
    def changed_mask_volume(self):
        return self.__changed_mask_volume
    
    @changed_mask_volume.setter
    def changed_mask_volume(self, value):
        self.__changed_mask_volume = value
    
    @changed_mask_volume.deleter
    def changed_mask_volume(self):
        if(hasattr(self, '__changed_mask_volume')):
            del self.__changed_mask_volume