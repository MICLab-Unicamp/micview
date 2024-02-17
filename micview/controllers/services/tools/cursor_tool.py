##
# @brief: This file contains the functions that are used to handle the cursor tool
#

# Imports
import importlib
from types import ModuleType
from typing import Any, List, Tuple
models: ModuleType = importlib.import_module(name='micview.models.getters')

# Functions
def handleSelectedItem(event: Any) -> None:
    """!
    @brief: This function is responsible for handling the selected item.
    @param: event: Any - The event.
    @return: None
    """
    CursorTool: Any = models.views['objects_ref'].ToolFrame.actual_tool
    itemid: int = CursorTool.treeview.focus()
    models.states['toolframe_states'].channel_select = int(CursorTool.treeview.item(itemid, 'values')[0]) - 1

def updateTransparency(value: float) -> None:
    """!
    @brief: This function is responsible for updating the transparency.
    @param: value: float - The value of the transparency.
    @return: None
    """
    models.states['toolframe_states'].transparency_level = float(value)/100

def updateChannelsIntensity() -> None:
    """!
    @brief: This function is responsible for updating the channels intensity.
    @return: None
    """
    original_vol: List[float] = models.data['original_volume_data'].image_volume
    original_shape: Tuple[int] = original_vol.shape
    point: Tuple[int] = models.data['cursor_data'].current_point
    multi: bool = True if len(original_shape) > 3 else False
    intensity: List[str] = []
    if(multi):
        for i in range(original_shape[0]):
            intensity.append(original_vol[i,point[0],point[1],point[2]])
    else:
        intensity.append(original_vol[point[0],point[1],point[2]])
    models.data['toolframe_data'].channel_intensity = str(intensity)
    updateIntensityIndicators()

def updateIntensityIndicators() -> None:
    """!
    @brief: This function is responsible for updating the intensity indicators.
    @return: None
    """
    intensity: List[str] = models.data['toolframe_data'].channel_intensity
    numofchannels: int = models.data['original_volume_data'].num_of_channels
    if(numofchannels > 1):
        parse: List[str] = ((intensity.split('[')[1]).split(']')[0]).split(', ')
        chann_intensity: List[int]= [int(float(i)) for i in parse]
    else:
        parse: List[str] = (intensity.split('[')[1]).split(']')[0]
        chann_intensity = [round(float(parse),2)]
    if(models.views['objects_ref'].ToolFrame.actual_tool is not None):
        if(models.states['toolframe_states'].selected_tool == 'cursor'):
            CursorTool: object = models.views['objects_ref'].ToolFrame.actual_tool
            updatePointIndicators(CursorTool=CursorTool)
            updateItens(intensity_arr=chann_intensity, CursorTool=CursorTool)
            updateLabelUnderCursor(CursorTool=CursorTool)
        elif(models.states['toolframe_states'].selected_tool == 'edit'):
            tool: object = models.views['objects_ref'].ToolFrame.actual_tool
            updatePointIndicators(CursorTool=tool)

def updateItens(intensity_arr: List[str], CursorTool: object) -> None:
    """!
    @brief: This function is responsible for updating the items.
    @param: intensity_arr: List[str] - The intensity array.
    @param: CursorTool: object - The cursor tool.
    @return: None
    """
    try:
        treeview: object = CursorTool.treeview
        itens: Tuple[object] = treeview.get_children()
        for i in range(len(itens)):
            values: List[Any] = treeview.item(itens[i],'values')
            treeview.item(itens[i], values=(values[0], intensity_arr[i]))
    except:
        pass

def updatePointIndicators(CursorTool: object) -> None:
    """!
    @brief: This function is responsible for updating the point indicators.
    @param: CursorTool: object - The cursor tool.
    @return: None
    """
    point: Tuple[int] = models.data['cursor_data'].current_point
    axes_shape: Tuple[int] = models.data['original_volume_data'].image_volume.shape[-3:]
    flipped: Tuple[bool] = models.data['files_data'].flipped_axes
    if(flipped[0]):
        try:
            CursorTool.cursorX.set(axes_shape[2]-point[2])
        except:
            pass
    else:
        try:
            CursorTool.cursorX.set(point[2]+1)
        except:
            pass
    if(flipped[1]):
        try:
            CursorTool.cursorY.set(axes_shape[1]-point[1])
        except:
            pass
    else:
        try:
            CursorTool.cursorY.set(point[1]+1)
        except:
            pass
    if(flipped[2]):
        try:
            CursorTool.cursorZ.set(axes_shape[0]-point[0])
        except:
            pass
    else:
        try:
            CursorTool.cursorZ.set(point[0]+1)
        except:
            pass

def updateLabelUnderCursor(CursorTool: object) -> None:
    """!
    @brief: This function is responsible for updating the label under the cursor.
    @param: CursorTool: object - The cursor tool.
    @return: None
    """
    label: int = models.data['cursor_data'].label_under_cursor
    text = "No Label"
    if(label != 0):
        text = f"Label {label}"
    try:
        CursorTool.label_under_cursor.set(text)
    except:
        pass