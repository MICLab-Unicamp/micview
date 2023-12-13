def changeZoom(zoom: float) -> None:
    from micview.models.getters import states
    states['toolframe_states'].zoom = zoom