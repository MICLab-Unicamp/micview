import pytest
import time
from micview.views.windows.MainWindow import MainWindow

@pytest.mark.filterwarnings("ignore::pytest.PytestUnhandledThreadExceptionWarning")
def test_window_init_simple(window_init_simple):
    window = window_init_simple
    assert type(window) == MainWindow
    time.sleep(2)

@pytest.mark.filterwarnings("ignore::pytest.PytestUnhandledThreadExceptionWarning")
def test_window_init_single(window_init_single):
    window = window_init_single
    assert type(window) == MainWindow
    time.sleep(2)

@pytest.mark.filterwarnings("ignore::pytest.PytestUnhandledThreadExceptionWarning")
def test_window_init_single_resized(window_init_single_resized):
    window = window_init_single_resized
    assert type(window) == MainWindow
    time.sleep(2)

@pytest.mark.filterwarnings("ignore::pytest.PytestUnhandledThreadExceptionWarning")
def test_window_init_multimodal_nomask(window_init_multimodal_nomask):
    window = window_init_multimodal_nomask
    assert type(window) == MainWindow
    time.sleep(2)

@pytest.mark.filterwarnings("ignore::pytest.PytestUnhandledThreadExceptionWarning")
def test_window_init_multimodal_mask(window_init_multimodal_mask):
    window = window_init_multimodal_mask
    assert type(window) == MainWindow
    time.sleep(2)