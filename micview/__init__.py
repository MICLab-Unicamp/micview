__version__="1.0.0.dev1"

def open():
    import micview.run as run
    run.main([])

def openfile(file: str, mask: str=None, resized: bool=False, block: bool=False) -> None:
    mask = str(mask) if mask else None
    argv: 'list[str]' = ['-i', file]
    if(mask):
        argv.extend(['-m', mask])
    if(resized):
        argv.append('-r')

    import threading
    from micview.run import main

    if block:
        main(argv)
    else:
        daemon = threading.Thread(target=main, args=(argv,))
        daemon.setDaemon(True)
        daemon.start()
        