from typing import Any, Dict

def checkKwargs(**kwargs: Dict[str, Any]) -> Dict[str, Any]:
    params: Dict[str, Any]= {'file': "", 'resized': False, 'mask': ""}
    for key, value in kwargs.items():
        if(key == "file"):
            params["file"] = value
        elif(key == "resized"):
            params["resized"] = value
        elif(key == "mask"):
            params["mask"] = value
    return params