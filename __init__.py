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
        #squared_image = Iminit.ImagesContainer(image,square=True)
        #image = Iminit.ImagesContainer(image)
        wndw.RootFrame(image, "MultiViewer")
    else:
        raise ValueError("File format not supported.")