import importlib
from types import ModuleType
from typing import Any, List, Tuple
models: ModuleType = importlib.import_module(name='micview.models.getters')

def handleSelectedItem(event: Any) -> None:
    CursorTool: Any = models.views['objects_ref'].ToolFrame.actual_tool
    itemid: int = CursorTool.treeview.focus()
    models.states['toolframe_states'].channel_select = int(CursorTool.treeview.item(itemid, 'values')[0]) - 1

def updateTransparency(value: float) -> None:
    models.states['toolframe_states'].transparency_level = float(value)/100

def updateChannelsIntensity() -> None:
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
    intensity: List[str] = models.data['toolframe_data'].channel_intensity
    numofchannels: int = models.data['original_volume_data'].num_of_channels
    if(numofchannels > 1):
        parse: List[str] = ((intensity.split('[')[1]).split(']')[0]).split(', ')
        chann_intensity: List[int]= [int(float(i)) for i in parse]
    else:
        parse: List[str] = (intensity.split('[')[1]).split(']')[0]
        chann_intensity = [round(float(parse),2)]
    CursorTool: object = models.views['objects_ref'].ToolFrame.actual_tool
    updateItens(intensity_arr=chann_intensity, CursorTool=CursorTool)
    updatePointIndicators(CursorTool=CursorTool)
    updateLabelUnderCursor(CursorTool=CursorTool)

def updateItens(intensity_arr: List[str], CursorTool: object) -> None:
    treeview: object = CursorTool.treeview
    itens: Tuple[object] = treeview.get_children()
    for i in range(len(itens)):
        values: List[Any] = treeview.item(itens[i],'values')
        treeview.item(itens[i], values=(values[0], intensity_arr[i]))

def updatePointIndicators(CursorTool: object) -> None:
    point: Tuple[int] = models.data['cursor_data'].current_point
    axes_shape: Tuple[int] = models.data['original_volume_data'].image_volume.shape[-3:]
    flipped: Tuple[bool] = models.data['files_data'].flipped_axes
    if(flipped[0]):
        CursorTool.cursorX.set(axes_shape[2]-point[2])
    else:
        CursorTool.cursorX.set(point[2]+1)
    if(flipped[1]):
        CursorTool.cursorY.set(axes_shape[1]-point[1])
    else:
        CursorTool.cursorY.set(point[1]+1)
    if(flipped[2]):
        CursorTool.cursorZ.set(axes_shape[0]-point[0])
    else:
        CursorTool.cursorZ.set(point[0]+1)

def updateLabelUnderCursor(CursorTool: object) -> None:
    label: int = models.data['cursor_data'].label_under_cursor
    text = "No Label"
    if(label != 0):
        text = f"Label {label}"
    CursorTool.label_under_cursor.set(text)