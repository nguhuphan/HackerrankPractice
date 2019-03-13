#https://www.hackerrank.com/challenges/diagonal-difference/problem
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the diagonalDifference function below.
# begin
sum_left = 0
sum_right = 0

def diagonalDifference(arr):
    for i in range(n):
        for j in range(n):
            if i == j:
                global sum_left,sum_right
                sum_left = sum_left + arr[i][j]
            if i + j == n - 1:
                sum_right = sum_right + arr[i][j]
    return abs(sum_left - sum_right)        

#end

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
