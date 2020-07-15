#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the breakingRecords function below.
def breakingRecords(scores):
    min_score = scores[0]
    max_score = scores[0]
    high_score_count = 0
    low_score_count = 0
    for elm in scores[1:]:
        if elm > max_score:
            max_score = elm 
            high_score_count += 1
        if elm < min_score:
            min_score = elm
            low_score_count += 1
    return [high_score_count, low_score_count]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
