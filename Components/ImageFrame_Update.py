from PIL import Image, ImageTk
import Components.Volume_Controller as Volctrl

def UpdateImages(ControllerObj, square_image, resized_window=False):
    if(ControllerObj.label_h == None or ControllerObj.label_h <= 1): # Screen Not Open Yet
        return
    if(not resized_window):
        ControllerObj.label_w = ControllerObj.axis0['Label'].winfo_width()
        ControllerObj.label_h = ControllerObj.axis0['Label'].winfo_height()
    if(square_image):
        new_sizes = Volctrl.ImageResizing(ControllerObj.squared_image, ControllerObj.label_h)
    else:
        new_sizes = Volctrl.ImageResizing(ControllerObj.image, ControllerObj.label_h)

    image_data = Volctrl.update_volume_point(ControllerObj.image)
    Labeled_image = [Image.fromarray(image_data[0],mode='F'),Image.fromarray(image_data[1],mode='F'),Image.fromarray(image_data[2],mode='F')]
    Imgs = [ImageTk.PhotoImage(Labeled_image[0].resize((new_sizes["axis0_x"],new_sizes["axis0_y"]))),
            ImageTk.PhotoImage(Labeled_image[1].resize((new_sizes["axis1_x"],new_sizes["axis1_y"]))), 
            ImageTk.PhotoImage(Labeled_image[2].resize((new_sizes["axis2_x"],new_sizes["axis2_y"])))]
    ControllerObj.axis0['Label'].configure(image=Imgs[0])
    ControllerObj.axis0['Label'].image = Imgs[0]
    ControllerObj.axis1['Label'].configure(image=Imgs[1])
    ControllerObj.axis1['Label'].image = Imgs[1]
    ControllerObj.axis2['Label'].configure(image=Imgs[2])
    ControllerObj.axis2['Label'].image = Imgs[2]
    ControllerObj.UpdateImageSize(new_sizes, ControllerObj.label_w, ControllerObj.label_h)

def Resize_Images(ControllerObj,square_image):
    ControllerObj.label_w = ControllerObj.axis0['Label'].winfo_width()
    ControllerObj.label_h = ControllerObj.axis0['Label'].winfo_height()
    if(ControllerObj.label_h != ControllerObj.previous_label_h or ControllerObj.label_w != ControllerObj.previous_label_w):
        ControllerObj.previous_label_w = ControllerObj.axis0['Label'].winfo_width()
        ControllerObj.previous_label_h = ControllerObj.axis0['Label'].winfo_height()
        UpdateImages(ControllerObj, square_image=square_image, resized_window=True)