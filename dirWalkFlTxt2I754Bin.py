#!/usr/bin/python3
import os

for (dirpath, dirnames, filenames) in os.walk('.'):
    for filename in filenames:
        if not filename.endswith('txt'):
            continue
        if 'input' in filename and 'fx' not in filename and 'fp' not in filename:
            target = os.path.join(dirpath, filename)
            os.system('flTxt2I754Bin.py {}'.format(target))
        if 'golden' in filename:
            target = os.path.join(dirpath, filename)
            os.system('flTxt2I754Bin.py {}'.format(target))


