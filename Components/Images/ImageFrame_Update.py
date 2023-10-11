from PIL import Image, ImageTk
import Components.Volume.Volume_Controller as Volctrl

def SetImages(ControllerObj, image_data, new_sizes):
    Imgs = []
    for i in range(3):
        Imgs.append(ImageTk.PhotoImage(Image.fromarray(image_data[i], mode='L').resize(new_sizes[i])))
    ControllerObj.axis0.SetImage(Imgs[0])
    ControllerObj.axis1.SetImage(Imgs[1])
    ControllerObj.axis2.SetImage(Imgs[2])

def SetMasks(ControllerObj, mask_data, new_sizes):
    Masks = []
    for i in range(3):
        Masks.append(ImageTk.PhotoImage(Image.fromarray(mask_data[i], mode='RGBA').resize(new_sizes[i])))
    ControllerObj.axis0.SetMask(Masks[0])
    ControllerObj.axis1.SetMask(Masks[1])
    ControllerObj.axis2.SetMask(Masks[2])

def UpdateImages(ControllerObj, square_image_boolean):
    mask_is_set = ControllerObj.root.getvar(name="mask_is_set")
    if(ControllerObj.label_h == None or ControllerObj.label_h <= 1): # Screen Not Open Yet
        return
    
    input_image = ControllerObj.square_image if square_image_boolean else ControllerObj.image
    channel = ControllerObj.root.getvar(name="channel_select")    
    ControllerObj.label_w = ControllerObj.axis0.winfo_width()
    ControllerObj.label_h = ControllerObj.axis0.winfo_height()
    new_sizes = Volctrl.ImageResizing(input_image, ControllerObj.label_h, channel_select=channel)
    if(mask_is_set):
        image_data, mask_data = Volctrl.get_2D_slices(input_image, channel_select=channel, show_mask=mask_is_set)
    else:
        image_data = Volctrl.get_2D_slices(input_image, channel_select=channel, show_mask=False)
        mask_data = None

    SetImages(ControllerObj, image_data, new_sizes)
    SetMasks(ControllerObj, mask_data, new_sizes)
    ControllerObj.UpdateImageSize(new_sizes, ControllerObj.label_w, ControllerObj.label_h)

def Resize_Images_Check(ControllerObj,square_image_boolean):
    ControllerObj.label_w = ControllerObj.axis0.winfo_width()
    ControllerObj.label_h = ControllerObj.axis0.winfo_height()
    if(ControllerObj.label_h != ControllerObj.previous_label_h or ControllerObj.label_w != ControllerObj.previous_label_w):
        ControllerObj.previous_label_w = ControllerObj.axis0.winfo_width()
        ControllerObj.previous_label_h = ControllerObj.axis0.winfo_height()
        UpdateImages(ControllerObj, square_image_boolean=square_image_boolean)