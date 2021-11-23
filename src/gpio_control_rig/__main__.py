from . import main

from . import config as env

if env.DEBUG_FLAG:
    import ptvsd
    ptvsd.enable_attach(address=('127.0.0.1', 3000))
    ptvsd.wait_for_attach()

main.main()
