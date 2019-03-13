#https://www.hackerrank.com/challenges/time-conversion/problem
#!/bin/python3

import os
import sys
import time
#begin

def timeConversion(s):
    #restructure time format base on the input
    timeM = time.strptime(s, "%I:%M:%S%p")
    #print the time format
    print(timeM)
    # convert from 12h => 24h
    result = time.strftime('%H:%M:%S',timeM)
    return str(result)
#end
if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    f.write(result + '\n')

    f.close()

# for testing
# input: 07:05:45PM
# output: 19:05:45