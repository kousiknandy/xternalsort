# (C) 2021 Kousik Nandy
# Licensed: GNU GPL v3

import os
import time
import sys

# Read a file line by line
def getline(filename, tailmode=False):
    with open(filename) as f:
        if tailmode:
           f.seek(0, os.SEEK_END) 
        while True:
            line = f.readline()
            if not line:
                # if tailing don't be discouraged by EOF
                if tailmode:
                    # sleep for a while and retry
                    time.sleep(0.100)
                    continue
                else:
                    break
            yield line.strip()


# unit test, given a bunch of sorted files with integers,
# k-way merge them and print in a sorted manner
if __name__ == "__main__":
    lessthan = lambda a, b: int(a) < int(b)
    debug_flag = os.getenv("DEBUG", 0)
    if len(sys.argv) < 2: exit(0)
    files = [getline(sys.argv[i]) for i in range(1, len(sys.argv))]
    lines = [next(f) for f in files]
    while True:
        idx = None
        line = None
        for i, l in enumerate(lines):
            if l is None: continue
            if not line or lessthan(l, line):
                line = l
                idx = i
        if idx is None: break
        if debug_flag:
            print(sys.argv[idx+1], line)
        else:
            print(line)
        try:
            lines[idx] = next(files[idx])
        except StopIteration:
            lines[idx] = None
