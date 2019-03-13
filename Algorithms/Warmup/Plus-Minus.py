#https://www.hackerrank.com/challenges/plus-minus/problem
#!/bin/python3

import math
import os
import random
import re
import sys
#begin
count_positive = 0
count_negative = 0
count_zero = 0
# Complete the plusMinus function below.
def plusMinus(arr):
    global count_negative,count_positive,count_zero
    for i in range(len(arr)):
        if arr[i] > 0:
            count_positive+=1
        elif arr[i] == 0:
            count_zero+=1
        else: 
            count_negative+=1
    print(count_positive/n)
    print(count_negative/n)
    print(count_zero/n)
#end
if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
