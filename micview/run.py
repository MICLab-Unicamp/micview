import sys
from argparse import ArgumentParser, ArgumentTypeError, Namespace
from micview import __version__
from micview.views.windows.MainWindow import MainWindow
from typing import Optional, Sequence

def niigz(s: str) -> None:
    if(s.endswith(".nii.gz")):
        return s
    else:
        raise ArgumentTypeError("File format not supported, expected .nii.gz")


def main(argv: Optional[Sequence[str]] = sys.argv[1:]) -> None:
    parser = ArgumentParser(prog="micview")

    parser_file = parser.add_argument_group(title="run_file", description="Opens micview passing a file as argument")
    parser_file.add_argument('-i', '--input', type=niigz, help="Input image file, archive must ends with .nii.gz", required=False)
    parser_file.add_argument('-m', '--mask', type=niigz, help="Mask image file, requires input argument, archive must ends with .nii.gz", required=False)
    parser_file.add_argument('-r','--resize', action="store_true", help="Resize image to fit screen, requires input argument", required=False)
    
    parser.add_argument('-v', '--version', action='version', version=__version__)
    parser.add_argument('-t', '--test', action="store_true", help="Test if argument is valid, dont opens the window", required=False)
    parser.add_argument('-d', '--description', action="version", version="Open-source GUI for visualization of multimodal medical images and segmentations viewing")

    args: Namespace = parser.parse_args(args=argv)    

    if args.mask and not args.input:
        raise ValueError("Mask argument requires input argument")
    if args.resize and not args.input:
        raise ValueError("Resize argument requires input argument")

    if(args.input):
            window = MainWindow(file=args.input, mask=args.mask, resized = args.resize)
    else:
        window = MainWindow()

    if(args.test):
        return 0
    
    return window.mainloop()

if __name__ == "__main__":
    main()