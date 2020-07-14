#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countApplesAndOranges function below.
def countApplesAndOranges(s, t, a, b, apples, oranges):
    apples_position = [a + apple for apple in apples]
    oranges_position = [b + orange for orange in oranges]
    count_apple = 0
    count_orange = 0
    for apple in apples_position:
        if apple in range(s, t + 1):
            count_apple += 1
    for orange in oranges_position:
        if orange in range(s, t + 1):
            count_orange += 1
    print(count_apple)
    print(count_orange) 

if __name__ == '__main__':
    st = input().split()

    s = int(st[0])

    t = int(st[1])

    ab = input().split()

    a = int(ab[0])

    b = int(ab[1])

    mn = input().split()

    m = int(mn[0])

    n = int(mn[1])

    apples = list(map(int, input().rstrip().split()))

    oranges = list(map(int, input().rstrip().split()))

    countApplesAndOranges(s, t, a, b, apples, oranges)