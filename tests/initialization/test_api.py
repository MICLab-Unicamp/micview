import subprocess
import os
from dotenv import load_dotenv

load_dotenv()
pathmultimodal = os.getenv('MULTIMODAL')
pathmask = os.getenv('MASK')

def test_micview_runs_successfully():
    result = subprocess.run(["micview", "--test"], text=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)    
    assert result.stderr == "pass\n", f"Failed to run micview"

def test_micview_runs_file_successfully():
    result = subprocess.run(["micview", "runfile","-i", pathmultimodal, "-m", pathmask, "-r", "-t"], text=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)    
    assert result.stderr == "pass\n", f"Failed to run micview"