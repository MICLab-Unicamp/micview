import argparse
import src.views.windows.MainWindow as wndw

if __name__ == "__main__":
    parser = argparse.ArgumentParser(prog="__init__.py")
    subparsers = parser.add_subparsers()
    parser_runfile = subparsers.add_parser("runfile")
    parser_runfile.add_argument('-i', '--input', type=str, required=True)
    parser_runfile.add_argument('-m', '--mask', type=str)
    parser_runfile.add_argument('-r','--resize', action="store_true")
    parser_runfile.add_argument('-o','--order', type=int)
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
            if(args.order == None):
                wndw.MainWindow(file=args.input, mask=mask_param, order=0, resized = args.resize).join()
            else:
                if(args.order < 0 or args.order > 5):
                    raise argparse.ArgumentTypeError("Order must be between 0 and 5")
                else:
                    wndw.MainWindow(file=args.input, mask=mask_param, order=args.order, resized = args.resize).join()
        else:
            raise ValueError("File format not supported.")
    else:
        wndw.MainWindow().join()