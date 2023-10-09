import argparse
import Components.MainWindow as wndw

if __name__ == "__main__":
    parser = argparse.ArgumentParser(prog="__init__.py")
    subparsers = parser.add_subparsers()
    parser_runfile = subparsers.add_parser("runfile")
    parser_runfile.add_argument('-i', '--input', type=str, required=True)
    parser_runfile.add_argument('-r','--resize', action="store_true")
    parser_runfile.add_argument('-o','--order', type=int)
    args = parser.parse_args()
    if(vars(args).get('input')):
        if args.input.endswith(".nii.gz"):
            if(args.order == None):
                wndw.RootFrame("Micview", file=args.input, order=0, resized = args.resize)
            else:
                if(args.order < 0 or args.order > 5):
                    raise argparse.ArgumentTypeError("Order must be between 0 and 5")
                else:
                    wndw.RootFrame("MultiViewer", file=args.input, order=args.order, resized = args.resize)
        else:
            raise ValueError("File format not supported.")
    else:
        wndw.RootFrame("MultiViewer")