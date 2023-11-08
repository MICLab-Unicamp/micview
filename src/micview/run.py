import argparse
from src.micview.views.windows.MainWindow import MainWindow

def main():
    parser = argparse.ArgumentParser(prog="__init__.py")
    parser.add_argument('-v', '--version', action='version', version='x.x.x')
    parser.add_argument('-t', '--test', action="store_true")
    subparsers = parser.add_subparsers()
    parser_runfile = subparsers.add_parser("runfile")
    parser_runfile.add_argument('-i', '--input', type=str, required=True)
    parser_runfile.add_argument('-m', '--mask', type=str)
    parser_runfile.add_argument('-r','--resize', action="store_true")
    parser_runfile.add_argument('-no','--nomainloop', action="store_true")
    parser_runfile.add_argument('-t', '--test', action="store_true")


    args = parser.parse_args()
    if(vars(args).get('input')):
        if(vars(args).get('mask')):
            if(args.mask.endswith(".nii.gz")):
                mask_param = args.mask
            else:
                raise ValueError("File format not supported.")
        else:
            mask_param = None

        if args.input.endswith(".nii.gz"):
            window = MainWindow(file=args.input, mask=mask_param, resized = args.resize)
            if(args.test):
                return "pass"
            return window.mainloop()
        else:
            raise ValueError("File format not supported.")
    else:
        window = MainWindow()
        if(args.test):
            return "pass"
        return window.mainloop()

if __name__ == "__main__":
    main()