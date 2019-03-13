#!/bin/python3

import math
import os
import random
import re
import sys
#begin
# Complete the breakingRecords function below.
def breakingRecords(scores):
    min = max = scores[0]
    min_count = max_count = 0
    for i in range(len(scores)):
        if scores[i] > max:
            max_count += 1
            max = scores[i]
        if scores[i] < min:
            min_count += 1
            min = scores[i]
    return max_count, min_count
#end
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
