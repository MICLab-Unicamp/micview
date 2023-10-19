def checkKwargs(**kwargs):
    params = {'file': "", 'resized': False, 'order': 0, 'mask': ""}
    for key, value in kwargs.items():
        if(key == "file"):
            params["file"] = value
        elif(key == "resized"):
            params["resized"] = value
        elif(key == "order"):
            params["order"] = value
        elif(key == "mask"):
            params["mask"] = value
    return params