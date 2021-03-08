#!/usr/bin/python3

import sys

print('Number of arguments:' + str(len(sys.argv)) +  ' arguments.')
print('Argument List:' + str(sys.argv))

iFile = sys.argv[1]
(rows, cols, chs) = sys.argv[2].split('x')
(r_st, r_end, c_st, c_end, ch_st, ch_end) = sys.argv[3].split(',')
oFile = sys.argv[1] + "_" + rows + "x" + cols + "x" + chs + "_" + r_st + "." + c_st + "." + ch_st
rows = int(rows)
cols = int(cols)
chs = int(chs)
r_st = int(r_st)
c_st = int(c_st)
ch_st = int(ch_st)
r_end = int(r_end)
c_end = int(c_end)
ch_end = int(ch_end)
print("input: " + iFile)
print("output " + oFile)
print(str(rows) + " " + str(cols) + " " + str(chs))
"""
try:
    with open(iFile, 'r') as ifd:
        with open(oFile, 'wb') as ofd: 
            for x in ifd:
                b = [int('0x' + str(x[i:i+2]), 16) for i in range(lineLen) if i % 2 == 0]
                b.reverse()
                
                ofd.write(bytes(b))
except:
    print("usage: weightHex2Bin.py input.hex output.bin")
"""  
