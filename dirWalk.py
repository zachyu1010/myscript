#!/usr/bin/python3
import os

for (dirpath, dirnames, filenames) in os.walk('.'):
    for filename in filenames:
        if not filename.endswith('txt'):
            continue
        if 'input' in filename and 'fx' not in filename and 'fp' not in filename:
            target = os.path.join(dirpath, filename)
            out = target + ".fp"
            os.system('fl2fp.py 8 1 4 {} {}'.format(target, out))

