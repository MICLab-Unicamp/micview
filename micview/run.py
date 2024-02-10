##
# @mainpage MICView
#
# @file run.py
#
# @brief Entrypoint for micview, where the main window is created and the arguments are parsed

# Imports
import sys
from argparse import ArgumentParser, ArgumentTypeError, Namespace
from micview import __version__
from micview.views.windows.MainWindow import MainWindow
from typing import Optional, Sequence

# Functions
def verifyType(s: str) -> None:
    """! Verifies if the file format is supported
    @param s: File path
    @return: s if the file format is supported or raises an ArgumentTypeError
    """
    if(s.endswith(".nii.gz" or ".dcm")):
        return s
    else:
        raise ArgumentTypeError("File format not supported, expected .nii.gz or .dcm")


def main(argv: Optional[Sequence[str]] = sys.argv[1:]) -> None:
    """! Main function for micview, where the main window is created and the arguments are parsed
    @param argv: Arguments passed to the program
    @return: 0 if the test argument is passed, else the main window is opened
    """
    parser = ArgumentParser(prog="micview")

    parser_file = parser.add_argument_group(title="run_file", description="Opens micview passing a file as argument")
    parser_file.add_argument('-i', '--input', type=verifyType, help="Input image file, archive must ends with .nii.gz or .dcm", required=False)
    parser_file.add_argument('-m', '--mask', type=verifyType, help="Mask image file, requires input argument, archive must ends with .nii.gz or .dcm", required=False)
    parser_file.add_argument('-r','--resize', action="store_true", help="Resize image to fit screen, requires input argument", required=False)

    parser_directory = parser.add_argument_group(title="run_directory_files", description="Opens micview passing a dir with multiples .dcm files as argurment")
    parser_directory.add_argument('-id', '--inputDir', type=str, help="Input image file directory, files must ends with .dcm", required=False)
    parser_directory.add_argument('-md', '--maskDir', type=str, help="Mask image file directory, requires input argument, archives must ends with .dcm", required=False)

    parser_array = parser.add_argument_group(title="run_array", description="Opens micview passing a numpy.ndarray as argument")
    parser_array.add_argument('-ia', '--inputArray', help="Input image array, must be a numpy.ndarray", required=False)
    parser_array.add_argument('-ma', '--maskArray', help="Input mask array, must be a numpy.ndarray", required=False)
    
    parser.add_argument('-v', '--version', action='version', version=__version__)
    parser.add_argument('-t', '--test', action="store_true", help="Test if argument is valid, dont opens the window", required=False)
    parser.add_argument('-d', '--description', action="version", version="Open-source GUI for visualization of multimodal medical images and segmentations viewing")

    args: Namespace = parser.parse_args(args=argv)    

    if args.mask and not args.input:
        raise ValueError("Mask argument requires input argument")
    if args.maskArray and not args.inputArray:
        raise ValueError("Mask argument requires input argument")
    if args.resize and not (args.input or args.inputArray):
        raise ValueError("Resize argument requires input argument")
    
    if(args.input):
        window = MainWindow(file=args.input, mask=args.mask, resized = args.resize)
    elif(args.inputArray):
        window = MainWindow(file=args.inputArray, mask=args.maskArray, resized = args.resize, array=True)
    elif(args.inputDir):
        window = MainWindow(file=args.inputDir, mask=args.maskDir, resized = args.resize)
    else:
        window = MainWindow()

    if(args.test):
        return 0
    
    return window.mainloop()

if __name__ == "__main__":
    main()