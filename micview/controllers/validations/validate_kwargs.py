from typing import Any, Dict

def checkKwargs(**kwargs: Dict[str, Any]) -> Dict[str, Any]:
    params: Dict[str, Any]= {'file': "", 'resized': False, 'mask': "", 'array': False}
    for key, value in kwargs.items():
        if(key == "file"):
            params["file"] = value
        elif(key == "resized"):
            params["resized"] = value
        elif(key == "mask"):
            params["mask"] = value
        elif(key == "array"):
            params["array"] = value
    return params