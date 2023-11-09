#!/bin/bash
pip uninstall micview
rm -rf dist
rm -rf MICView.egg-info/
pip cache purge
cd ..
find . -name "*.pyc" -exec rm -f {} \;
find . -type d -name "__pycache__" -exec rm -r {} +
python setup.py clean --all
python setup.py sdist bdist_wheel
pip install .
