#https://www.hackerrank.com/challenges/compare-the-triplets/problem
# #!/bin/python3

import math
import os
import random
import re
import sys
# begin
def compareTriplets(a, b):
    a_score = 0
    b_score = 0
    for i in range(0, len(a)):
        if a[i] > b[i]:
            a_score = a_score + 1
        elif a[i] < b[i]:
            b_score = b_score + 1
    result = []
    result.append(a_score)
    result.append(b_score)
    return result
#end
# Complete the compareTriplets function below.
if __name__ == '__main__':
        fptr = open(os.environ['OUTPUT_PATH'], 'w')

        a = list(map(int, input().rstrip().split()))

        b = list(map(int, input().rstrip().split()))

        result = compareTriplets(a, b)

        fptr.write(' '.join(map(str, result)))
        fptr.write('\n')

        fptr.close()

