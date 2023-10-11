from PIL import Image, ImageTk
import Components.Volume.Volume_Controller as Volctrl

def ComposeImages(image_data, mask_data):
    PIL_images = []
    for i in range(3):
        image = Image.fromarray(image_data[i], mode='L')
        mask = Image.fromarray(mask_data[i], mode='RGBA') #tem que ter 4 camadas
        PIL_images.append([image,mask])
    return PIL_images

def UpdateImages(ControllerObj, square_image_boolean, show_mask=True):
    if(ControllerObj.label_h == None or ControllerObj.label_h <= 1): # Screen Not Open Yet
        return
    
    input_image = ControllerObj.square_image if square_image_boolean else ControllerObj.image
    channel = ControllerObj.root.getvar(name="channel_select")
    #######
    image_data, mask_data = Volctrl.get_2D_slices(input_image, channel_select=channel, show_mask=show_mask)
    Labeled_image = ComposeImages(image_data, mask_data)
    #Labeled_image = [Image.fromarray(composed_data[0],mode='L'),Image.fromarray(composed_data[1],mode='L'),Image.fromarray(composed_data[2],mode='L')]
    
    ControllerObj.label_w = ControllerObj.axis0.winfo_width()
    ControllerObj.label_h = ControllerObj.axis0.winfo_height()
    new_sizes = Volctrl.ImageResizing(input_image, ControllerObj.label_h, channel_select=channel)
    Imgs = [ImageTk.PhotoImage(Labeled_image[0][0].resize((new_sizes["axis0_x"],new_sizes["axis0_y"]))),
            ImageTk.PhotoImage(Labeled_image[1][0].resize((new_sizes["axis1_x"],new_sizes["axis1_y"]))), 
            ImageTk.PhotoImage(Labeled_image[2][0].resize((new_sizes["axis2_x"],new_sizes["axis2_y"]))),
            ImageTk.PhotoImage(Labeled_image[0][1].resize((new_sizes["axis0_x"],new_sizes["axis0_y"]))),
            ImageTk.PhotoImage(Labeled_image[1][1].resize((new_sizes["axis1_x"],new_sizes["axis1_y"]))), 
            ImageTk.PhotoImage(Labeled_image[2][1].resize((new_sizes["axis2_x"],new_sizes["axis2_y"])))]
    ControllerObj.UpdateImageSize(new_sizes, ControllerObj.label_w, ControllerObj.label_h)

    #canvasaxis.create_image(0,0,image=fig)
    '''
    ControllerObj.axis0['Label'].configure(image=Imgs[3])
    ControllerObj.axis0['Label'].image = Imgs[3]
    ControllerObj.axis1['Label'].configure(image=Imgs[4])
    ControllerObj.axis1['Label'].image = Imgs[4]
    ControllerObj.axis2['Label'].configure(image=Imgs[5])
    ControllerObj.axis2['Label'].image = Imgs[5]'''
    ControllerObj.axis0.SetImage(Imgs[0])
    ControllerObj.axis1.SetImage(Imgs[1])
    ControllerObj.axis2.SetImage(Imgs[2])

def Resize_Images_Check(ControllerObj,square_image_boolean):
    ControllerObj.label_w = ControllerObj.axis0.winfo_width()
    ControllerObj.label_h = ControllerObj.axis0.winfo_height()
    if(ControllerObj.label_h != ControllerObj.previous_label_h or ControllerObj.label_w != ControllerObj.previous_label_w):
        ControllerObj.previous_label_w = ControllerObj.axis0.winfo_width()
        ControllerObj.previous_label_h = ControllerObj.axis0.winfo_height()
        UpdateImages(ControllerObj, square_image_boolean=square_image_boolean)