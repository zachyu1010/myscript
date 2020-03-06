#!/usr/bin/python3

import sys

help_msg = """usage: ./split num string
    num tells split cmmand to chunk the string by the num number."""

if (len(sys.argv) != 4):
    print(help_msg)
    sys.exit(2)

n = int(sys.argv[1])
grp = int(sys.argv[2]);
line = sys.argv[3]

line_by_n = [line[i:i+n] for i in range(0, len(line), n)]

print('\n\n')
#print(line_by_n)

idx = 0
for l in line_by_n:
    print(l)
    if (grp != 0 and idx == (grp - 1)):
        print('')
        idx = -1;
    
    idx = idx + 1;
 
