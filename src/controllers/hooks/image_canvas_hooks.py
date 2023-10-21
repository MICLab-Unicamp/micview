import importlib
models = importlib.import_module('src.models.models')

def action_on_child(* args):
    print("action_on_child")
    parent = models.get_objects_ref().ImagesFrame
    child = models.get_image_canvas_states().action_on_child
    print(parent)
    print(child)
    match child:
        case 0:
            parent.axial.controller.event_handler()
            parent.sagital.controller.event_handler()
        case 1:
            parent.coronal.controller.event_handler()
            parent.sagital.controller.event_handler()    
        case 2:
            parent.coronal.controller.event_handler()
            parent.axial.controller.event_handler()
        case 3:
            parent.coronal.controller.event_handler()
            parent.axial.controller.event_handler()         
            parent.sagital.controller.event_handler()
        case _:
            raise Exception ###################