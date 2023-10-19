from globals.globals import objects_ref, toolframe_states, toolframe_infos, volume_infos

def handle_selected_item(event):
    CursorTool = objects_ref.get_ToolFrame().actual_tool
    itemid = CursorTool.treeview.focus()
    selected_channel = int(CursorTool.treeview.item(itemid, 'values')[0]) - 1
    toolframe_states.set_channel_select(selected_channel)

def update_intensity():
    intensity = toolframe_infos.get_channel_intensity()
    numofchannels = volume_infos.get_num_of_channels()
    if(numofchannels > 1):
        parse = ((intensity.split('[')[1]).split(']')[0]).split(', ')
        chann_intensity = [int(float(i)) for i in parse]
    else:
        parse = (intensity.split('[')[1]).split(']')[0]
        chann_intensity = [round(float(parse),2)]
    CursorTool = objects_ref.get_ToolFrame().actual_tool
    update_itens(intensity_arr=chann_intensity, CursorTool=CursorTool)
    update_point_indicators(CursorTool)

def update_itens(intensity_arr, CursorTool):
    treeview = CursorTool.treeview
    itens = treeview.get_children()
    for i in range(len(itens)):
        values = treeview.item(itens[i],'values')
        treeview.item(itens[i], values=(values[0], intensity_arr[i]))

def update_point_indicators(CursorTool):
    point = volume_infos.get_current_point_original_vol()
    CursorTool.cursorX.set(point[2]+1)
    CursorTool.cursorY.set(point[1]+1)
    CursorTool.cursorZ.set(point[0]+1)