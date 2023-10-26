from micview.models.models import get_changed_volume_data

def get_nearest_valid_point(x, y, z):
    volume_shape = get_changed_volume_data().changed_image_volume.shape
    valid_points = [round(x), round(y), round(z)]
    for i in range(3):
        if(valid_points[i] < 0):
            valid_points[i] = 0
        elif(valid_points[i] >= volume_shape[i]):
            valid_points[i] -= 1

    return valid_points