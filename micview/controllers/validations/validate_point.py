from micview.models.getters import data

def get_nearest_valid_point(x: float, y: float, z: float) -> "list[float]":
    volume_shape: list[int] = data['changed_volume_data'].changed_image_volume.shape
    valid_points: list[int] = [round(number=x), round(number=y), round(number=z)]
    for i in range(3):
        if(valid_points[i] < 0):
            valid_points[i] = 0
        elif(valid_points[i] >= volume_shape[i]):
            valid_points[i] -= 1

    return valid_points