class files_data_class:
    def __init__(self):
        self.__image_file = None
        self.__mask_file = None
        self.__metadatas = None

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
    def metadatas(self):
        return self.__metadatas
    
    @metadatas.setter
    def metadatas(self, value):
        self.__metadatas = value