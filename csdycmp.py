#!/usr/bin/python3

import sys
import csv
from os import listdir
from os.path import isfile, join


ioInfoCsvPath = sys.argv[1]
csDir = sys.argv[2]
dyDir = sys.argv[3]


def cmpTwoSeqFile(path1, path2):
    idx = 0
    with open(path1, 'r') as fd1:
        with open(path2, 'r') as fd2:
            f1 = fd1.read().splitlines();
            f2 = fd2.read().splitlines();

            if len(f1) != len(f2):
                return (False, False, 0)

            for l1, l2 in zip(f1, f2):
                if l1 == l2:
                    idx += 1
                else:
                    return (False, len(f1), idx)

            return (True, len(f1), idx)


ioInfo = []
with open(ioInfoCsvPath, newline='') as f:
    reader = csv.reader(f)
    ioInfo = list(reader)

ioInfo = [ \
        y[0:2]+y[2:3]+[int(y[3])]+[int(y[4])]+[int(y[5])]+y[6:] \
        for y in ioInfo \
        if y[0] == 'o'
        ]

dySeqs = [ \
        f for f in listdir(dyDir) \
        if isfile(join(dyDir, f)) and 'fx.txt' in f \
        ]

for y in ioInfo:
    dyTmps = [f for f in dySeqs if y[2] in f]
    dyFn = sorted(dyTmps, key=len)[0]
    dyPath = join(dyDir, dyFn)
    csFn = "dma2seq_" + y[1] + ".seq"
    csPath = join(csDir, csFn)

    (isEqu, flen, idx) = cmpTwoSeqFile(csPath, dyPath)
    (chs, rows, cols) = y[3:6]

    #print(isEqu, flen, idx, csFn, dyFn)
    if isEqu == False:
        chIdx = idx // (rows * chs)
        rowIdx = (idx % (rows * chs)) // rows
        colIdx = idx % chs
        print(flen, idx, chIdx, rowIdx, colIdx, csFn, dyFn)
        break

