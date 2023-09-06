import argparse
import SimpleITK as sitk
import Components.Image_Controller as Imctrl
import Components.Images_Initializer as Iminit
import Components.MainWindow as wndw

if __name__ == "__main__":
    print("Loading...")
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--input', type=str, required=True)
    args = parser.parse_args()
    npz_path = args.input

    if npz_path.endswith(".nii.gz"):
        image = sitk.ReadImage(npz_path)
        image = sitk.GetArrayFromImage(image)
        image = Iminit.ImagesContainer(image)
        Labeled_image = Imctrl.update_POV(image.volume, image.handler_param, image.resize_factor)
        wndw.RootFrame(Labeled_image, image.window_name)
    else:
        raise ValueError("File format not supported.")