#!/usr/bin/python3

import sys

help_msg = """usage: ./split num feed string
    num tells split cmmand to chunk the integers seperated by comma by the num number and appending \n*feed to it."""

if (len(sys.argv) != 4):
    print(help_msg)
    sys.exit(2)

n = int(sys.argv[1])
feed = int(sys.argv[2])
line = sys.argv[3]

nums = line.split(",")
nums_by_n = [nums[i:i+n] for i in range(0, len(nums), n)]

print('\n\n')
for l in nums_by_n:
    print(l)
    if feed != 0:
        print('\n' * (feed - 1))
 
