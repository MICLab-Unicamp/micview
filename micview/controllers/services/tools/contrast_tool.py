##
# @brief: This file contains the function to change the contrast of the volume data.
#

# Imports
from micview.controllers.services.volume.controller import changeVolumeContrast

# Functions
def changeContrast(min: int, max: int) -> None:
    """!
    @brief: This function is responsible for changing the contrast of the volume.
    @param: min: int - The minimum value of the contrast.
    @param: max: int - The maximum value of the contrast.
    @return: None
    """
    from micview.models.getters import data, states
    data["changed_volume_data"].min_and_max_values = (min, max)
    changeVolumeContrast(min, max)
    states['image_canvas_states'].update_all_childs = True

