# MICView
This project is an open-source API of a GUI for visualization of multimodal medical images and segmentations viewing. It was produced in a scenario of need for the assistance of graphical tools for the study of deep-learning neural networks for segmenting medical images, and also as the final project of my Bachelor's degree on Computer Engineering in FEEC-Unicamp. The project was made using Tkinter, and designed in a MVC software architecture (Model View Controller).

## Requirements
The software was developed and tested in Ubuntu 22.04, and tested on Windows. The minimum required version of Python is 3.8, others required libs are described in [requirements](./requirements.txt)

## Installation
It is suggested to create a Python environment with Conda:

    conda create -n micview python=3.8
    conda activate micview

To download the package, do:

    git clone https://github.com/MICLab-Unicamp/micview
    cd micview
    pip install . 

## Using
You can use the API calling inside a terminal, and calling functions of micview inside your Python code, to call micview inside a terminal do:

    micview

You can also pass arguments as the file path, the mask path, and if you want to see the image in the original shape or in a squared shape.

    micview --input 'filepath' --mask 'maskpath' --resized

In the above example the GUI will open with an image and segmentation loaded, and in a squared shape. To call the GUI inside your Python code, you can use the functions:

    micview.open() #Opens the GUI
    micview.openfile(file='filepath', mask: optional ='maskpath', resized: optional = False (default)) #Opens the GUI with an image

Pay attention that if you call this functions inside a Python code, the programm will block in this line until you closes the MICView window, it occurs because the Tkinter mainloop is a blocking process.