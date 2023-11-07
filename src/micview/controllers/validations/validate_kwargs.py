def checkKwargs(**kwargs):
    params = {'file': "", 'resized': False, 'mask': ""}
    for key, value in kwargs.items():
        if(key == "file"):
            params["file"] = value
        elif(key == "resized"):
            params["resized"] = value
        elif(key == "mask"):
            params["mask"] = value
    return params