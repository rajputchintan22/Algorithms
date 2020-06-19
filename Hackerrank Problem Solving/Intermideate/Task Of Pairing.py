#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'taskOfPairing' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts LONG_INTEGER_ARRAY freq as parameter.
#

def taskOfPairing(n,freq):
    ans = 0
    temp = []
    j = 0
    while j < n-1:
        ans += freq[j] // 2
        if freq[j+1] > 0:
            freq[j+1] +=  freq[j] % 2
        j += 1
    ans += freq[j] // 2
    return ans


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    freq_count = int(input().strip())

    freq = []

    for _ in range(freq_count):
        freq_item = int(input().strip())
        freq.append(freq_item)

    result = taskOfPairing(freq_count,freq)

    fptr.write(str(result) + '\n')

    fptr.close()
