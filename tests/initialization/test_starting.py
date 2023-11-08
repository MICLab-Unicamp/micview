import tkinter as tk
import pytest
import time
from threading import Thread
from src.micview.views.windows.MainWindow import MainWindow

class Window(Thread):
    def __init__(self):
        super().__init__()
        self.window = MainWindow()        

    def run(self):
        self.window.mainloop()

@pytest.fixture
def window_init():
    windowprocess = Window()
    window = windowprocess.window
    windowprocess.start()
    return {"window": window}

@pytest.mark.filterwarnings("ignore::pytest.PytestUnhandledThreadExceptionWarning")
def test_window_init(window_init):
    window = window_init["window"]
    time.sleep(1)
    menu = window.Menu
    assert menu.master == window
    assert window.window_name == "MICView"
    time.sleep(1)
    window.destroy()