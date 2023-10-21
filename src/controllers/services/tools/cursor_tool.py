import importlib
models = importlib.import_module('src.models.models')

def handle_selected_item(event):
    CursorTool = models.get_objects_ref().ToolFrame.actual_tool
    itemid = CursorTool.treeview.focus()
    models.get_toolframe_states().channel_select = int(CursorTool.treeview.item(itemid, 'values')[0]) - 1

def update_intensity():
    intensity = models.get_toolframe_data().channel_intensity
    numofchannels = models.get_original_volume_data().num_of_channels
    if(numofchannels > 1):
        parse = ((intensity.split('[')[1]).split(']')[0]).split(', ')
        chann_intensity = [int(float(i)) for i in parse]
    else:
        parse = (intensity.split('[')[1]).split(']')[0]
        chann_intensity = [round(float(parse),2)]
    CursorTool = models.get_objects_ref().ToolFrame.actual_tool
    update_itens(intensity_arr=chann_intensity, CursorTool=CursorTool)
    update_point_indicators(CursorTool)

def update_itens(intensity_arr, CursorTool):
    treeview = CursorTool.treeview
    itens = treeview.get_children()
    for i in range(len(itens)):
        values = treeview.item(itens[i],'values')
        treeview.item(itens[i], values=(values[0], intensity_arr[i]))

def update_point_indicators(CursorTool):
    point = models.get_cursor_data().current_point_original_vol
    CursorTool.cursorX.set(point[2]+1)
    CursorTool.cursorY.set(point[1]+1)
    CursorTool.cursorZ.set(point[0]+1)