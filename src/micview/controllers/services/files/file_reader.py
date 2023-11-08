import SimpleITK

def readImageFile(path):
    MetadatasFile = SimpleITK.ReadImage(path)
    ArrayFromImage = SimpleITK.GetArrayFromImage(MetadatasFile)
    return ArrayFromImage

def readMaskFile(path):
    MetadatasFile = SimpleITK.ReadImage(path)
    ArrayFromImage = SimpleITK.GetArrayFromImage(MetadatasFile)
    return ArrayFromImage