#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'pickingNumbers' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
#

def pickingNumbers(a):
    # Write your code here

    #From the given array first pick the possible pairs 
    set_a = set(a)
    possible_pairs = []
    picked_numbers = 0
    for i in set_a: 
        current_pair_count_1 = a.count(i) + a.count(i + 1) 
        current_pair_count_2 = a.count(i) + a.count(i - 1)
        if current_pair_count_1 > picked_numbers:
            picked_numbers = current_pair_count_1
        if current_pair_count_2 > picked_numbers:
            picked_numbers = current_pair_count_2
        
    return picked_numbers 
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    result = pickingNumbers(a)

    fptr.write(str(result) + '\n')

    fptr.close()
