#!/usr/bin/env python3

import subprocess
import sys
from util.io.iter_fpaths import *

def main(test_sub) -> None:
    BIDS_ROOT = '../data/bids'

    for (fpath, sub, task, run) in iter_fpaths(BIDS_ROOT):
        if sub != test_sub:
            continue
        log = open("logs/decoder_test_" + "test_sub" + ".log", 'w')
        subprocess.check_call("./decoder.py %s %s %s %s" % (fpath, sub, task, run), shell=True, stdout = log)
        break

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(__doc__)
        sys.exit(1)
    test_sub = sys.argv[1]
    main(test_sub)
