import pytest
import time
import os
from dotenv import load_dotenv
from threading import Thread
from micview.views.windows.MainWindow import MainWindow

load_dotenv()
pathsingle = os.getenv('SINGLE_CHANNEL')
pathmultimodal = os.getenv('MULTIMODAL')
pathmask = os.getenv('MASK')

@pytest.fixture
def window_init_simple():
    window = MainWindow()
    thread = Thread(target=window.mainloop)
    thread.start()
    while window.winfo_exists() == False:
        time.sleep(0.1)
    yield window
    window.quit()
    thread.join()

@pytest.fixture
def window_init_single():
    window = MainWindow(image = pathsingle)
    thread = Thread(target=window.mainloop)
    thread.start()
    while window.winfo_exists() == False:
        time.sleep(0.1)
    yield window
    window.quit()
    thread.join()

@pytest.fixture
def window_init_single_resized():
    window = MainWindow(image = pathsingle, mask = None, resized = True)
    thread = Thread(target=window.mainloop)
    thread.start()
    while window.winfo_exists() == False:
        time.sleep(0.1)
    yield window
    window.quit()
    thread.join()

@pytest.fixture
def window_init_multimodal_nomask():
    window = MainWindow(image = pathmultimodal)
    thread = Thread(target=window.mainloop)
    thread.start()
    while window.winfo_exists() == False:
        time.sleep(0.1)
    yield window
    window.quit()
    thread.join()

@pytest.fixture
def window_init_multimodal_mask():
    window = MainWindow(image = pathmultimodal, mask = pathmask)
    thread = Thread(target=window.mainloop)
    thread.start()
    while window.winfo_exists() == False:
        time.sleep(0.1)
    yield window
    window.quit()
    thread.join()