from typing import List
import numpy as np
from micview.models.getters import data

def getNearestValidPoint(x: float, y: float, z: float) -> "List[float]":
    volume_shape: List[int] = np.array(data['changed_volume_data'].changed_image_volume.shape)
    valid_points: List[int] = [round(number=x), round(number=y), round(number=z)]
    for i in range(3):
        if(valid_points[i] < 0):
            valid_points[i] = 0
        elif(valid_points[i] >= volume_shape[i]):
            valid_points[i] -= 1

    return valid_points