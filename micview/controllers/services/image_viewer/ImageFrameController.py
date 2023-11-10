from threading import Event, Thread
from micview.models.getters import views
from micview.controllers.services.loading.Animation import Animation

class LoadingCircles(Thread):
    def __init__(self, event: Event):
        self.event = event
        super().__init__(daemon=True)
        self.images_frame = views['objects_ref'].ImagesFrame
        self.animation_a = self.images_frame.axial.loading_circle = Animation(self.images_frame.axial, self.event)
        self.animation_c = self.images_frame.coronal.loading_circle = Animation(self.images_frame.coronal, self.event)
        self.animation_s = self.images_frame.sagital.loading_circle = Animation(self.images_frame.sagital, self.event)

    def run(self):
        self.animation_a.start()
        self.animation_c.start()
        self.animation_s.start()
        self.animation_a.join()
        self.animation_c.join()
        self.animation_s.join()

def enable_all_canvas():
    images_frame = views['objects_ref'].ImagesFrame
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

def disable_all_canvas():
    images_frame = views['objects_ref'].ImagesFrame
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

