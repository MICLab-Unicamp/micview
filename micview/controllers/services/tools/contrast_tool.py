from micview.controllers.services.volume.controller import changeVolumeContrast

def changeContrast(min: int, max: int) -> None:
    from micview.models.getters import data, states
    data["changed_volume_data"].min_and_max_values = (min, max)
    changeVolumeContrast(min, max)
    states['image_canvas_states'].update_all_childs = True

