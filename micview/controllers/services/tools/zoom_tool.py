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