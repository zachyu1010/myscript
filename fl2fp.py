#!/usr/bin/python3

import sys
import os

#print('Number of arguments:' + str(len(sys.argv)) +  ' arguments.')
#print('Argument List:' + str(sys.argv))

def saturate(val, bw):
    max = (1 * (2 ** (bw - 1))) - 1
    min = -1 ** (2 ** (bw - 1))

    if val > max:
        return max
    elif val < min:
        return min
    else:
        return val

def fl2fp(val, radix):
    return round(val * (2 ** (radix)))

sign = lambda v : (v > 0) - (v < 0)


try:
    bw = int(sys.argv[1])
    if bw != 8 and bw != 16:
        raise
    scale = int(sys.argv[2])
    radix = int(sys.argv[3])
    iFile = sys.argv[4]
    oFile = sys.argv[5]
    bFile = os.path.splitext(oFile)[0] + ".bin"

    obyte = []
    bbyte = []
    with open(iFile, 'r') as ifd:
        with open(oFile, 'w') as ofd:
            with open(bFile, 'wb') as bfd:
                for x in ifd:
                    fl = float(x)
                    fp = fl2fp(fl * scale, radix)
                    if bw == 8:
                        obyte = [abs(fp) * sign(fp)]
                        bbyte = [fp & ((2 ** 8) - 1)]
                    elif bw == 16:
                        obyte = [fp & ((2 ** 8) - 1)]
                        obyte.append(abs(fp >> 8) * sign(fp))
                        bbyte = [fp & ((2 ** 8) - 1)]
                        bbyte.append(fp & ((2 ** 8) - 1))
                    else:
                        raise

                    for b in obyte:
                        ofd.write(str(b) + '\n')

                    bfd.write(bytes(bbyte))

except:
    print("usage: fl2fp.py bitwidth scale radix input.hex output.bin")






