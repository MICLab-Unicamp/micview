import argparse
import SimpleITK as sitk
import Image_Controller as Imctrl
import Image_Displayer as Imgdispl
from Multiview import *

if __name__ == "__main__":
    print("Loading...")
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--input', type=str, required=True)
    args = parser.parse_args()
    npz_path = args.input

    if npz_path.endswith(".nii.gz"):
        image = sitk.GetArrayFromImage(sitk.ReadImage(npz_path))
        image = Imgdispl.MultiViewer(image)
        Labeled_image = Imctrl.display(image.volume, image.handler_param, image.resize_factor)
        MainFrame(Labeled_image, image.window_name)
    else:
        raise ValueError("File format not supported.")