import SimpleITK as sitk
import micview
path = "/home/caio/Documentos/medical_images/caio_multimodal_example/BraTS19_CBICA_AAB_1/multimodal.nii.gz"
path_mask = "/home/caio/Documentos/medical_images/caio_multimodal_example/BraTS19_CBICA_AAB_1/BraTS19_CBICA_AAB_1_seg.nii.gz"
mask = sitk.ReadImage(path_mask)
mask = sitk.GetArrayFromImage(mask)
arr = sitk.ReadImage(path)
arr = sitk.GetArrayFromImage(arr)
micview.openarray(array=arr, mask=mask)