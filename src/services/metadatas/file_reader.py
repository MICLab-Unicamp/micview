import SimpleITK

def readImageFile(path):
    MetadatasFile = SimpleITK.ReadImage(path)
    ###### setar metadatasfile global
    ArrayFromImage = SimpleITK.GetArrayFromImage(path)
    return ArrayFromImage

def readMaskFile(path):
    MetadatasFile = SimpleITK.ReadImage(path)
    ###### setar metadatasfilemask global
    ArrayFromImage = SimpleITK.GetArrayFromImage(path)
    return ArrayFromImage