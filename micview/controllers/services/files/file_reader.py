import numpy as np
from typing import Any, List, Dict
import SimpleITK as sitk
from micview.models.getters import data

def OrientImage(file: sitk.Image) -> List[Any]:
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
    MetadatasFile: sitk.Image = sitk.ReadImage(fileName=path)
    image_metadatas: Dict[str, Any] = dict()
    for key in MetadatasFile.GetMetaDataKeys():
        image_metadatas[key] = MetadatasFile.GetMetaData(key=key)
    data['files_data'].image_metadatas = image_metadatas
    ArrayFromImage: List[Any] = OrientImage(file=MetadatasFile)
    return ArrayFromImage

def readMaskFile(path: str) -> List[Any]:
    MetadatasFile: sitk.Image = sitk.ReadImage(fileName=path)
    mask_metadatas: Dict[str, Any] = dict()
    for key in MetadatasFile.GetMetaDataKeys():
        mask_metadatas[key] = MetadatasFile.GetMetaData(key=key)
    data['files_data'].mask_metadatas = mask_metadatas
    ArrayFromImage: List[Any] = OrientImage(file=MetadatasFile)
    return ArrayFromImage