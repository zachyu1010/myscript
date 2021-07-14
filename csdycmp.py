#!/usr/bin/python3

import sys
import csv
import os
from os import listdir
from os.path import isfile, join


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

if __name__ == '__main__':
    try:
        ioInfoCsvPath = sys.argv[1]
        cmpType = sys.argv[2]
        csDir = sys.argv[3]
        dyDir = sys.argv[4]
        if cmpType != 'o' and cmpType != 'c':
            raise

        ioInfoCsvPath = os.path.abspath(ioInfoCsvPath)
        ioInfo = []
        with open(ioInfoCsvPath, newline='') as f:
            reader = csv.reader(f)
            ioInfo = list(reader)

            ioInfo = [ \
                    y[0:2]+y[2:3]+[int(y[3])]+[int(y[4])]+[int(y[5])]+y[6:] \
                    for y in ioInfo \
                    if y[0] == cmpType
                    ]

            csSeqs = []
            dySeqs = []
            if cmpType == 'o':
                dySeqs = [ \
                        f for f in listdir(dyDir) \
                        if isfile(join(dyDir, f)) and 'fx.txt' in f \
                        ]
            elif cmpType == 'c':
                csSeqs = [ \
                        f for f in listdir(csDir) \
                        if isfile(join(csDir, f)) and 'cpu_node_' in f \
                            and '.seq' in f and  '_out_' in f\
                        ]

                dySeqs = [ \
                        f for f in listdir(dyDir) \
                        if isfile(join(dyDir, f)) and 'fl.txt' in f \
                        ]

            for y in ioInfo:
                dyTmps = [f for f in dySeqs if y[2] in f]
                dyFn = sorted(dyTmps, key=len)[0]
                dyPath = join(dyDir, dyFn)

                csPath = ''
                if cmpType == 'o':
                    csFn = "dma2seq_" + y[1] + ".seq"
                elif cmpType == 'c':
                    csTmps = [f for f in csSeqs if y[2].strip('_o0') in f]
                    csFn = sorted(csTmps, key=len)[0]
                csPath = join(csDir, csFn)

                (isEqu, flen, idx) = cmpTwoSeqFile(csPath, dyPath)
                (chs, rows, cols) = y[3:6]

                chIdx = idx // (rows * chs)
                rowIdx = (idx % (rows * chs)) // chs
                colIdx = idx % chs
                if isEqu == True:
                    print(flen, idx, chIdx, rowIdx, colIdx, csFn, dyFn)
                else:
                    print("-> mismatch: ", flen, idx, chIdx, rowIdx, colIdx, csFn, dyFn)
                    break
    except:
        print("usage: csdycmp.py ioinfo.csv type csimDumpDir dynastyDumpDir")

