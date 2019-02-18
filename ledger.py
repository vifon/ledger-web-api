#!/usr/bin/env python3

from ledger import app

if __name__ == '__main__':
    from flaskrun import flaskrun
    flaskrun(app, threaded=True)
