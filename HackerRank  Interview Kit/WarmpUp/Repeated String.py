#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the repeatedString function below.
def repeatedString(s, n):
    k = len(s)
    t = n % k
    count1 = 0
    count2 = 0
    for i in range(k):
        if i <= t:
            count2 = count1
        if s[i] == 'a':
            count1 += 1
    return count1 * (n // k) + count2


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    n = int(input())

    result = repeatedString(s, n)

    fptr.write(str(result) + '\n')

    fptr.close()
