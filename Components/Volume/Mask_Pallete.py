pallete = [
    {'Number': 1, 'RGB': (255, 0, 0)},
    {'Number': 2, 'RGB': (0, 255, 0)},
    {'Number': 3, 'RGB': (0, 0, 255)},
    {'Number': 4, 'RGB': (255, 255, 0)},
    {'Number': 5, 'RGB': (0, 255, 255)},
    {'Number': 6, 'RGB': (255, 0, 255)},
    {'Number': 7, 'RGB': (255, 255, 255)}
]

def MaskPallete(index):
    if(index < 7):
        return dict.copy(pallete[index])
    else:
        color = dict.copy(pallete[index%7])
        color["Number"] = index + 1
        rgb = [0,0,0]
        for i in range(3):
            ton = abs(color["RGB"][i] - 30*(index//7))
            if(ton>255):
                ton = 255
            rgb[i] = ton
        color["RGB"] = tuple(rgb)
        return color