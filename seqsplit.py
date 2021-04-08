#!/usr/bin/python3

import sys
import re

#print('Number of arguments:' + str(len(sys.argv)) +  ' arguments.')
#print('Argument List:' + str(sys.argv))

try:
    iFile = sys.argv[1]
    (rows, cols, chs) = sys.argv[2].split('x')
    (r_st, r_end, c_st, c_end, ch_st, ch_end) = sys.argv[3].split(',')
    oFile = sys.argv[1] + "_" + rows + "x" + cols + "x" + chs + "_" + r_st + "." + r_end + "." + c_st + "." + c_end + "." + ch_st + "." + ch_end
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
    print("output: " + oFile)

    count = 0
    with open(iFile, 'r') as ifd:
        fd = ifd.read()
        fd = re.split('\s+', fd)
        with open(oFile, 'w') as ofd: 
            for ch in range (ch_st, ch_end):
                for r in range (r_st, r_end):
                    offset = ch*rows*cols + r*cols
                    flag = 0
                    for c in range (c_st, c_end):
                        ofd.write(str(fd[offset + c] + "\n"));
                        #if flag == 0:
                        #    print(str(count) + " " + str(offset + c) + " " + fd[offset + c])
                        #    print(str(r) + " " + str(c) + " " + str(ch));
                        flag = flag + 1
                        count = count + 1

    print("total count = ", count)
    print("............. [done]")
except:
    print("""usage: seqsplit ROWSxCOLSxCHS r_st,r_end,c_st,c_end,ch_st,ch_end
(x_st is inclsive, x_end is exclusive)
    """)
