
class ImageFrame_Controller:
    def __init__(self, axis0, axis1, axis2, imageorientation):
        self.axis0 = axis0
        self.axis1 = axis1
        self.axis2 = axis2
        self.imageorientation = imageorientation
        self.BindAxis()

    def BindAxis(self):

        self.axis0['Label'].bind('<Button-1>', self.UpdatePointAxis0)
        self.axis0['Label'].bind('<B1-Motion>', self.UpdatePointAxis0)

        self.axis1['Label'].bind('<Button-1>', self.UpdatePointAxis1)
        self.axis1['Label'].bind('<B1-Motion>', self.UpdatePointAxis1)

        self.axis2['Label'].bind('<Button-1>', self.UpdatePointAxis2)
        self.axis2['Label'].bind('<B1-Motion>', self.UpdatePointAxis2)

    def UpdatePointAxis0(self, event):
        click = event.__dict__
        x = click['x']
        y = click['y']
        print(f"Click: x={x}, y={y}")
        #print(f"Image Size: x={self.images_sizes['axis0_x']}, y={self.images_sizes['axis0_y']}")
        #print(f"Label Size: x={self.image_w}, y={self.image_h}")

    def UpdatePointAxis1(self, event):
        print(f"eixo 1: {event}")

    def UpdatePointAxis2(self, event):
        print(f"eixo 2: {event}")