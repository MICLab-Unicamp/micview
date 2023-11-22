class files_data_class:
    def __init__(self):
        self.__image_file = None
        self.__mask_file = None
        self.__image_metadatas = None
        self.__mask_metadatas = None
        self.__flipped_axes = None
        self.__orient_text = None

    @property
    def image_file(self):
        return self.__image_file
    
    @image_file.setter
    def image_file(self, value):
        self.__image_file = value

    @property
    def mask_file(self):
        return self.__mask_file
    
    @mask_file.setter
    def mask_file(self, value):
        self.__mask_file = value

    @property
    def image_metadatas(self):
        return self.__image_metadatas
    
    @image_metadatas.setter
    def image_metadatas(self, value):
        self.__image_metadatas = value
    
    @property
    def mask_metadatas(self):
        return self.__mask_metadatas
    
    @mask_metadatas.setter
    def mask_metadatas(self, value):
        self.__mask_metadatas = value

    @property
    def flipped_axes(self):
        return self.__flipped_axes
    
    @flipped_axes.setter
    def flipped_axes(self, value):
        self.__flipped_axes = value

    @property
    def orient_text(self):
        return self.__orient_text

    @orient_text.setter
    def orient_text(self, value):
        self.__orient_text = value