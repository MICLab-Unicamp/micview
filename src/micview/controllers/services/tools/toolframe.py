from src.micview.views.components.toolframe.CursorTool import CursorTool

def Set_Tool(tool, master):
    if(tool == "cursor"):
        master.set_actual_tool(CursorTool(master))