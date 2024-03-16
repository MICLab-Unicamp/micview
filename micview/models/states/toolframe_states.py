##
# @brief: This file contains the class that holds the states of the toolframe.
#

# Imports
import tkinter as tk
from micview.controllers.hooks.toolframe_states_hooks import channelSelectHook, selectedToolHook, toolIsSetHook, transparencyLevelHook, zoomHook, paintHooks

# Classes
class ToolframeStatesClass:
    """!
    @brief: This class holds the states of the toolframe.
    """
    def __init__(self, master: tk.Tk) -> None:
        """!
        @brief: The constructor of the class.
        @param: master: tk.Tk - The master window of the application.
        """
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
        self.__paint_mode = tk.BooleanVar(master=master, value=False, name="paint_mode")
        self.__paint_mode.trace(mode='w', callback=paintHooks)
        self.__color_paint_mode = (255, 0, 0, 255)
        self.__brush_size = 1

    @property
    def channel_select(self) -> int:
        """!
        @brief: The getter method of the channel_select property.
        @return: int
        """
        return self.__channel_select.get()

    @channel_select.setter
    def channel_select(self, value: int) -> None:
        """!
        @brief: The setter method of the channel_select property.
        @param: value: int - The value to be set.
        @return: None
        """
        assert type(value) is int
        self.__channel_select.set(value=value)

    @property
    def selected_tool(self) -> str:
        """!
        @brief: The getter method of the selected_tool property.
        @return: str
        """
        return self.__selected_tool.get()

    @selected_tool.setter
    def selected_tool(self, value: str) -> None:
        """!
        @brief: The setter method of the selected_tool property.
        @param: value: str - The value to be set.
        @return: None
        """
        assert type(value) is str
        self.__selected_tool.set(value=value)

    @selected_tool.deleter
    def selected_tool(self) -> None:
        """!
        @brief: The deleter method of the selected_tool property.
        @return: None
        """
        self.__selected_tool.set(value="none")

    @property
    def tool_is_set(self) -> bool:
        """!
        @brief: The getter method of the tool_is_set property.
        @return: bool
        """
        return self.__tool_is_set.get()
    
    @tool_is_set.setter
    def tool_is_set(self, value: bool) -> None:
        """!
        @brief: The setter method of the tool_is_set property.
        @param: value: bool - The value to be set.
        @return: None
        """
        assert type(value) is bool
        self.__tool_is_set.set(value=value)

    @property
    def transparency_level(self) -> float:
        """!
        @brief: The getter method of the transparency_level property.
        @return: float
        """
        return self.__transparency_level.get()
    
    @transparency_level.setter
    def transparency_level(self, value: float) -> None:
        """!
        @brief: The setter method of the transparency_level property.
        @param: value: float - The value to be set.
        @return: None
        """
        assert type(value) is float
        self.__transparency_level.set(value=value)

    @property
    def zoom(self) -> float:
        """!
        @brief: The getter method of the zoom property.
        @return: float
        """
        return self.__zoom.get()
    
    @zoom.setter
    def zoom(self, value: float) -> None:
        """!
        @brief: The setter method of the zoom property.
        @param: value: float - The value to be set.
        @return: None
        """
        assert type(value) is float
        self.__zoom.set(value=value)

    @property
    def paint_mode(self) -> bool:
        """!
        @brief: The getter method of the paint_mode property.
        @return: bool
        """
        return self.__paint_mode.get()
    
    @paint_mode.setter
    def paint_mode(self, value: bool) -> None:
        """!
        @brief: The setter method of the paint_mode property.
        @param: value: bool - The value to be set.
        @return: None
        """
        assert type(value) is bool
        self.__paint_mode.set(value=value)

    @property
    def color_paint_mode(self):
        """!
        @brief: The getter method of the color_paint_mode property.
        @return: str
        """
        return self.__color_paint_mode

    @color_paint_mode.setter
    def color_paint_mode(self, value) -> None:
        """!
        @brief: The setter method of the color_paint_mode property.
        @param: value: str - The value to be set.
        @return: None
        """
        self.__color_paint_mode=value

    @property
    def brush_size(self):
        """!
        @brief: The getter method of the brush_size property.
        @return: str
        """
        return self.__brush_size

    @brush_size.setter
    def brush_size(self, value) -> None:
        """!
        @brief: The setter method of the brush_size property.
        @param: value: str - The value to be set.
        @return: None
        """
        self.__brush_size=value
