##
# @brief This file contains the ImageFrameController class, which is responsible for controlling the ImageFrame class.
#

# Imports
from threading import Event, Thread
from micview.models.getters import views
from micview.controllers.services.loading.Animation import Animation
from threading import Event, Thread
from micview.models.getters import views

# Class
class LoadingCircles(Thread):
    """!
    @brief This class is responsible for controlling the loading circles.
    """
    def __init__(self, event: Event) -> None:
        """!
        @brief Constructor method
        @param event: Event
        @return None
        """
        self.event: Event = event
        super().__init__(daemon=True)
        self.images_frame: object = views['objects_ref'].ImagesFrame
        self.animation_a = self.images_frame.axial.loading_circle = Animation(master=self.images_frame.axial, event=self.event)
        self.animation_c = self.images_frame.coronal.loading_circle = Animation(master=self.images_frame.coronal, event=self.event)
        self.animation_s = self.images_frame.sagital.loading_circle = Animation(master=self.images_frame.sagital, event=self.event)

    def run(self) -> None:
        """!
        @brief This method is used to start the loading circles
        @return None
        """
        self.animation_a.start()
        self.animation_c.start()
        self.animation_s.start()
        self.animation_a.join()
        self.animation_c.join()
        self.animation_s.join()

def enableAllCanvas() -> None:
    """!
    @brief This function is used to enable all canvas
    @return None
    """
    images_frame: object = views['objects_ref'].ImagesFrame
    images_frame.axial.delete("all")
    images_frame.axial.bind('<Configure>', images_frame.axial.controller.resize)
    images_frame.axial.bind('<Button-1>', images_frame.axial.controller.click)
    images_frame.axial.bind('<B1-Motion>', images_frame.axial.controller.click)
    images_frame.coronal.delete("all")
    images_frame.coronal.bind('<Configure>', images_frame.coronal.controller.resize)
    images_frame.coronal.bind('<Button-1>', images_frame.coronal.controller.click)
    images_frame.coronal.bind('<B1-Motion>', images_frame.coronal.controller.click)
    images_frame.sagital.delete("all")
    images_frame.sagital.bind('<Configure>', images_frame.sagital.controller.resize)
    images_frame.sagital.bind('<Button-1>', images_frame.sagital.controller.click)
    images_frame.sagital.bind('<B1-Motion>', images_frame.sagital.controller.click)
    images_frame.update()

def disableAllCanvas() -> None:
    """!
    @brief This function is used to disable all canvas
    @return None
    """
    images_frame: object = views['objects_ref'].ImagesFrame
    images_frame.axial.delete("all")
    images_frame.axial.unbind('<Configure>')
    images_frame.axial.unbind('<Button-1>')
    images_frame.axial.unbind('<B1-Motion>')
    images_frame.coronal.delete("all")
    images_frame.coronal.unbind('<Configure>')
    images_frame.coronal.unbind('<Button-1>')
    images_frame.coronal.unbind('<B1-Motion>')
    images_frame.sagital.delete("all")
    images_frame.sagital.unbind('<Configure>')
    images_frame.sagital.unbind('<Button-1>')
    images_frame.sagital.unbind('<B1-Motion>')
    images_frame.update()

