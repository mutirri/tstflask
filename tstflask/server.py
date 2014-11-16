#!/usr/bin/env python

import sys
import argparse

from core import make_app, settings

DEF_HEADLESS_MODE = settings.HEADLESS_MODE
DEF_HEADLESS_MODE_XDISPLAY = settings.HEADLESS_MODE_XDISPLAY

parser = argparse.ArgumentParser(prog=sys.argv[0])

parser.add_argument('-d', dest='debug_mode', action='store_true', default=False,
    help="Run application in debug mode.")
parser.add_argument('-x', dest='headless_mode', type=str, default=DEF_HEADLESS_MODE,
    help="Switch to browser launching in headless mode. Default value: %i" % (DEF_HEADLESS_MODE))
parser.add_argument('-X', dest='headless_mode_xdisplay', type=str, default=DEF_HEADLESS_MODE_XDISPLAY,
    help="Change value of XDISPLAY variable which is required in headless mode. Default value: %s" % (DEF_HEADLESS_MODE_XDISPLAY))

args = parser.parse_args()

if __name__ == "__main__":
    app = make_app()

    app.run(debug=args.debug_mode, port=settings.PORT)

