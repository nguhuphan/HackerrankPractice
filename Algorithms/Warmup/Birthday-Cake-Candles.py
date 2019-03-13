#https://www.hackerrank.com/challenges/birthday-cake-candles/problem
#!/bin/python3

import math
import os
import random
import re
import sys
#begin
# Complete the birthdayCakeCandles function below.
def birthdayCakeCandles(ar):
    return ar.count(max(ar))
#end
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ar_count = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = birthdayCakeCandles(ar)

    fptr.write(str(result) + '\n')

    fptr.close()