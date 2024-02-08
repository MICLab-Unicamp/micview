##
# @brief: This file contains the file reader service, which is responsible for reading the image and mask files.
#

# Imports
import numpy as np
from typing import Any, List, Dict
import SimpleITK as sitk
from micview.models.getters import data

# Functions
def orientImage(file: sitk.Image) -> List[Any]:
    """!
        @brief: This function is used to orient the image
        @param file: sitk.Image
        @return: List[Any]
    """
    Orient = sitk.DICOMOrientImageFilter()
    Orient.SetDesiredCoordinateOrientation(DesiredCoordinateOrientation="LPI")
    oriented_image: Any = Orient.Execute(image1=file)
    data['files_data'].flipped_axes = Orient.GetFlipAxes()
    data['files_data'].orient_text = dict({
        0: ["R", "A", "L", "P"],
        1: ["R", "S", "L", "I"],
        2: ["A", "S", "P", "I"]
    })
    extracted: List[Any] = np.array(object=sitk.GetArrayFromImage(image=oriented_image))
    return extracted

def readImageFile(path: str) -> List[Any]:
    """!
        @brief: This function is used to read the image file
        @param path: str
        @return: List[Any]
    """
    MetadatasFile: sitk.Image = sitk.ReadImage(fileName=path)
    image_metadatas: Dict[str, Any] = dict()
    for key in MetadatasFile.GetMetaDataKeys():
        image_metadatas[key] = MetadatasFile.GetMetaData(key=key)
    data['files_data'].image_metadatas = image_metadatas
    ArrayFromImage: List[Any] = orientImage(file=MetadatasFile)
    return ArrayFromImage

def readMaskFile(path: str) -> List[Any]:
    """!
        @brief: This function is used to read the mask file
        @param path: str
        @return: List[Any]
    """
    MetadatasFile: sitk.Image = sitk.ReadImage(fileName=path)
    mask_metadatas: Dict[str, Any] = dict()
    for key in MetadatasFile.GetMetaDataKeys():
        mask_metadatas[key] = MetadatasFile.GetMetaData(key=key)
    data['files_data'].mask_metadatas = mask_metadatas
    ArrayFromImage: List[Any] = orientImage(file=MetadatasFile)
    return ArrayFromImage