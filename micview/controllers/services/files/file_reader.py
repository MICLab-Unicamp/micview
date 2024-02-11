##
# @brief: This file contains the file reader service, which is responsible for reading the image and mask files.
#

# Imports
import os
import tkinter as tk
import numpy as np
from typing import Any, List, Dict
import SimpleITK as sitk
from micview.models.getters import data
import pydicom
import dicom2nifti
import tempfile

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

def readImageFilesFromDir(path: str) -> List[Any]:
    """!
        @brief: This function is used to read a DICOM series from a directory, order the slices and convert them to a NIfTI file
        @param path: str
        @return: str
    """
    onlyfiles = [path+'/'+f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))]
    openfiles = []
    for file in onlyfiles:
        if file.endswith('.dcm'):
            openfiles.append(pydicom.dcmread(file))
    slices = sorted(openfiles, key=lambda s: s.SliceLocation)    
    with tempfile.TemporaryDirectory() as workdir:
        for i in slices:
            tmpfile = tempfile.NamedTemporaryFile(delete=False, dir=workdir, suffix='.dcm')
            pydicom.dcmwrite(tmpfile.name, i)
        newPath = "/tmp/niftitempfile.nii.gz"
        dicom2nifti.dicom_series_to_nifti(workdir, "/tmp/niftitempfile", reorient_nifti=True)

    return newPath

def readImageFile(path: str) -> List[Any]:
    """!
        @brief: This function is used to read the image file
        @param path: str
        @return: List[Any]
    """
    if(os.path.isdir(path)):
        path = readImageFilesFromDir(path=path)
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
    if(os.path.isdir(path)):
        path = readImageFilesFromDir(path=path)
    MetadatasFile: sitk.Image = sitk.ReadImage(fileName=path)
    mask_metadatas: Dict[str, Any] = dict()
    for key in MetadatasFile.GetMetaDataKeys():
        mask_metadatas[key] = MetadatasFile.GetMetaData(key=key)
    ArrayFromImage: List[Any] = orientImage(file=MetadatasFile)
    if ArrayFromImage.ndim != 3:
        tk.messagebox.showerror(title="Error", message="Mask volume must be 3D.")
    if(ArrayFromImage.shape[-3:] != data['original_volume_data'].image_volume.shape[-3:]):
        tk.messagebox.showerror(title="Error", message="Mask volume must have the same dimensions as the image volume.")
    else:
        data['files_data'].mask_metadatas = mask_metadatas
        return ArrayFromImage