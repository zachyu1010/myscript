#!/usr/bin/python3

import sys

#print('Number of arguments:' + str(len(sys.argv)) +  ' arguments.')
#print('Argument List:' + str(sys.argv))

try:
    iFile = sys.argv[1]
    oFile = sys.argv[2]
except:
    print("usage: weightHex2Bin.py input.hex output.bin")

lineLen = 32
with open(iFile, 'r') as ifd:
    with open(oFile, 'wb') as ofd: 
        for x in ifd:
            b = [int('0x' + str(x[i:i+2]), 16) for i in range(lineLen) if i %2 == 0]
            b.reverse()
            
            ofd.write(bytes(b))
            
        
        
            


