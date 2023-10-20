from models.models import objects_ref, toolframe_data, toolframe_states, original_volume_data, cursor_data

def handle_selected_item(event):
    CursorTool = objects_ref.ToolFrame.actual_tool
    itemid = CursorTool.treeview.focus()
    toolframe_states.channel_select = int(CursorTool.treeview.item(itemid, 'values')[0]) - 1

def update_intensity():
    intensity = toolframe_data.channel_intensity
    numofchannels = original_volume_data.num_of_channels
    if(numofchannels > 1):
        parse = ((intensity.split('[')[1]).split(']')[0]).split(', ')
        chann_intensity = [int(float(i)) for i in parse]
    else:
        parse = (intensity.split('[')[1]).split(']')[0]
        chann_intensity = [round(float(parse),2)]
    CursorTool = objects_ref.ToolFrame.actual_tool
    update_itens(intensity_arr=chann_intensity, CursorTool=CursorTool)
    update_point_indicators(CursorTool)

def update_itens(intensity_arr, CursorTool):
    treeview = CursorTool.treeview
    itens = treeview.get_children()
    for i in range(len(itens)):
        values = treeview.item(itens[i],'values')
        treeview.item(itens[i], values=(values[0], intensity_arr[i]))

def update_point_indicators(CursorTool):
    point = cursor_data.current_point_original_vol
    CursorTool.cursorX.set(point[2]+1)
    CursorTool.cursorY.set(point[1]+1)
    CursorTool.cursorZ.set(point[0]+1)