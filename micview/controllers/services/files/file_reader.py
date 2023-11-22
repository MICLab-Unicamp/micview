import numpy as np
import SimpleITK as sitk
from micview.models.getters import data

def OrientImage(file: sitk.Image):
    oriented_image: sitk.Image = sitk.DICOMOrient(file, desiredCoordinateOrientation="LPI")
    extracted = np.array(sitk.GetArrayFromImage(image=oriented_image))
    return extracted

def readImageFile(path):
    MetadatasFile = sitk.ReadImage(path)
    image_metadatas = dict()
    for key in MetadatasFile.GetMetaDataKeys():
        image_metadatas[key] = MetadatasFile.GetMetaData(key)
    data['files_data'].image_metadatas = image_metadatas
    ArrayFromImage = OrientImage(file=MetadatasFile)
    return ArrayFromImage

def readMaskFile(path):
    MetadatasFile = sitk.ReadImage(path)
    mask_metadatas = dict()
    for key in MetadatasFile.GetMetaDataKeys():
        mask_metadatas[key] = MetadatasFile.GetMetaData(key)
    data['files_data'].mask_metadatas = mask_metadatas
    ArrayFromImage = OrientImage(file=MetadatasFile)
    return ArrayFromImage