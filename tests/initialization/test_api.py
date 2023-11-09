import subprocess
import os
from dotenv import load_dotenv

load_dotenv()
pathmultimodal = os.getenv('MULTIMODAL')
pathmask = os.getenv('MASK')

def test_micview_runs_successfully():
    result = subprocess.run(["micview", "--test"], capture_output=True, text=True)
    assert result.returncode == 0, f"Failed to run micview"

def test_micview_runs_file_successfully():
    result = subprocess.run(["micview", "-i", pathmultimodal, "-m", pathmask, "-r", "-t"], capture_output=True, text=True)    
    assert result.returncode == 0, f"Failed to run micview"