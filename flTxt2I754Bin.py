#!/usr/bin/python3

import sys
import os
import struct

#print('Number of arguments:' + str(len(sys.argv)) +  ' arguments.')
#print('Argument List:' + str(sys.argv))

#try:
(chs, rows, cols) = sys.argv[1].split('x')
chs = int(chs);
rows = int(rows);
cols = int(cols);
iFile = sys.argv[2]
bFile = os.path.splitext(iFile)[0] + ".bin"

bbyte = []
with open(iFile, 'r') as ifd:
    for x in ifd:
        x = float(x.rstrip("\n"));
        i754 = struct.unpack('I', struct.pack('f', x))[0]
        #bfd.write(struct.pack('f', x))
        bbyte.extend([i754 & 0xff, (i754 >> 8) & 0xff, (i754 >> 16) & 0xff, (i754 >> 24) & 0xff])

with open(bFile, 'wb') as bfd:
    for ch in range(chs):
        for r in range(rows):
            for c in range(cols):
                for i in range(4):
                    idx = r*cols*chs*4 + c*chs*4 + ch*4 + i
                    bfd.write(bytes([bbyte[idx]]))

#except:
#    print("usage: flTxt2I754Bin.py #CHx#ROWx#COL inputFloatFile")






