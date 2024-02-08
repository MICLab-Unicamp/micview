##
# @brief: This function is used to validate the kwargs passed to the function

# Imports
from typing import Any, Dict

# Functions
def checkKwargs(**kwargs: Dict[str, Any]) -> Dict[str, Any]:
    """!
        @brief: This function is used to validate the kwargs passed to the function
        @param kwargs: Dict[str, Any]
        @return: Dict[str, Any]
    """
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