import tkinter as tk
from micview.controllers.hooks.toolframe_states_hooks import channelSelectHook, selectedToolHook, toolIsSetHook, transparencyLevelHook, zoomHook

class ToolframeStatesClass:
    def __init__(self, master: tk.Tk) -> None:
        super().__init__()      
        self.__channel_select = tk.IntVar(master=master, value=0, name="channel_select")
        self.__channel_select.trace(mode='w', callback=channelSelectHook)
        self.__selected_tool = tk.StringVar(master=master, value="none", name="selected_tool")
        self.__selected_tool.trace(mode='w', callback=selectedToolHook)
        self.__tool_is_set = tk.BooleanVar(master=master, value=False, name="tool_is_set")
        self.__tool_is_set.trace(mode='w', callback=toolIsSetHook)
        self.__transparency_level = tk.DoubleVar(master=master, value=1.0, name="transparency_level")
        self.__transparency_level.trace(mode='w', callback=transparencyLevelHook)
        self.__zoom = tk.DoubleVar(master=master, value=1.0, name="zoom")
        self.__zoom.trace(mode='w', callback=zoomHook)    

    @property
    def channel_select(self) -> int:
        return self.__channel_select.get()

    @channel_select.setter
    def channel_select(self, value: int) -> None:
        assert type(value) is int
        self.__channel_select.set(value=value)

    @property
    def selected_tool(self) -> str:
        return self.__selected_tool.get()

    @selected_tool.setter
    def selected_tool(self, value: str) -> None:
        assert type(value) is str
        self.__selected_tool.set(value=value)

    @selected_tool.deleter
    def selected_tool(self) -> None:
        self.__selected_tool.set(value="none")

    @property
    def tool_is_set(self) -> bool:
        return self.__tool_is_set.get()
    
    @tool_is_set.setter
    def tool_is_set(self, value: bool) -> None:
        assert type(value) is bool
        self.__tool_is_set.set(value=value)

    @property
    def transparency_level(self) -> float:
        return self.__transparency_level.get()
    
    @transparency_level.setter
    def transparency_level(self, value: float) -> None:
        assert type(value) is float
        self.__transparency_level.set(value=value)

    @property
    def zoom(self) -> float:
        return self.__zoom.get()
    
    @zoom.setter
    def zoom(self, value: float) -> None:
        assert type(value) is float
        self.__zoom.set(value=value)