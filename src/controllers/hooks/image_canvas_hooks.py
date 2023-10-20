from models.models import image_canvas_states, objects_ref

def action_on_child(* args):
    print(args)
    parent = objects_ref.ImagesFrame
    child = image_canvas_states.action_on_child
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