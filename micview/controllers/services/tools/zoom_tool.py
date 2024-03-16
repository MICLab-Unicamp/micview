##
# @brief: This file contains the zoom tool service.
#

# Functions
def changeZoom(zoom: float) -> None:
    """!
    @brief: This function is responsible for changing the zoom of the image.
    @param: zoom: float - The zoom value.
    @return: None
    """
    from micview.models.getters import states
    states['toolframe_states'].zoom = zoom

def reset_shifting() -> None:
    """!
    @brief: This function is used to reset the shifting.
    @return: None
    """
    from micview.models.getters import views
    images_frame: object = views['objects_ref'].ImagesFrame
    images_frame.axial.controller.shift = [0, 0]
    images_frame.axial.controller.refresh()
    images_frame.coronal.controller.shift = [0, 0]
    images_frame.coronal.controller.refresh()
    images_frame.sagital.controller.shift = [0, 0]
    images_frame.sagital.controller.refresh()
