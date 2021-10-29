###
### Author: Xin Li
### Description:  Left-aligned bars (lab.py)
###The program should iterate through each of the
###digits in the string and convert the individual
###digits to integers. For each of the numbers,
###the program should print out the corresponding
###number of horizontal bars of # characters, within a
###nicely-formatted box. The box should always be 11
###characters wide in total, but the height may vary based
###on the length of the input string.
###
from os import _exit as exit
size = input('Enter bar string:\n')
print('+---------+')
i = 0
while i < len(size) :
    char = size[i]
    char = int(char)
    i += 1
    print('|','#'*char,' '*(9-char),'|',sep='')
print('+---------+')
exit(0)
