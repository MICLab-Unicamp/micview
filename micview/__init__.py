__version__="1.0.0"

def open():
    import micview.run as run
    run.main([])

def openfile(file: str, mask: str=None, resized: bool=False, block: bool=True, array: bool=False) -> None:
    mask = str(mask) if mask else None
    if(array):
        argv: 'list[str]' = ['-ia', file]
        if(mask):
            argv.extend(['-ma', mask])
        if(resized):
            argv.append('-r')
    else:
        argv: 'list[str]' = ['-i', file]
        if(mask):
            argv.extend(['-m', mask])
        if(resized):
            argv.append('-r')

    from multiprocessing import Process
    from micview.run import main

    if block:
        main(argv)
    else:
        daemon = Process(target=main, args=(argv,))
        daemon.daemon = True
        daemon.start()    

def openarray(array: list, mask: list=None, resized: bool=False, block: bool=True) -> None:
    import numpy as np
    import tempfile

    if not isinstance(array, np.ndarray):
        raise TypeError("Array must be a numpy.ndarray")

    if not isinstance(mask, np.ndarray) and mask is not None:
        raise TypeError("Mask must be a numpy.ndarray")

    if array.ndim < 3:
        raise ValueError("Invalid dimensions number for Array")

    if mask is not None and mask.ndim < 3:
        raise ValueError("Invalid dimensions number for Mask")

    tmpfile = tempfile.NamedTemporaryFile(delete=False)
    np.save(file=tmpfile.name, arr=array)
    tmpfile.close()
    if mask is not None:
        tmpmask = tempfile.NamedTemporaryFile(delete=False)
        np.save(file=tmpmask.name, arr=mask)
        tmpmask.close()
        openfile(file=tmpfile.name, mask=tmpmask.name, resized=resized, block=block, array=True)
    else:
        openfile(file=tmpfile.name, mask=None, resized=resized, block=block, array=True)
