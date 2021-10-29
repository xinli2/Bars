###
### Author: Xin Li
### Description:  Center-aligned bars (cab.py).
###In this program each pair of numbers is used to produce the output
###on a given row. the bars should 'start' from the center of the
###20-character-wide box, and the input string specifies how much
###they should jut-out to the left and to the right.
###
from os import _exit as exit
size = input('Enter bar string:\n')
print('+------------------+')
i = 0
while i < len(size) :
    char_1 = size[i]
    char_2 = size[i+1]
    char_1 = int(char_1)
    char_2 = int(char_2)
    i += 2
    print('|',' '*(9-char_1),'#'*char_1,'#'*char_2,' '*(9-char_2),'|',sep='')
print('+------------------+')
exit(0)
