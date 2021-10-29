###
### Author: Xin Li
### Description:
###This program should accept the same type of
###input as lab.py. It should print out a box
###with the bars right-aligned, instead of
###left-aligned. Two example runs of
###the program are shown on the left.
###
from os import _exit as exit
size = input('Enter bar string:\n')
print('+---------+')
i = 0
while i < len(size) :
    char = size[i]
    char = int(char)
    i += 1
    print('|',' '*(9-char),'#'*char,'|',sep='')
print('+---------+')
exit(0)
