#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the countingValleys function below.
def countingValleys(n, s):
    t = []
    ans = 0
    last_removed = "U"
    for i in s:
        if len(t) == 0:
            if last_removed == "D":
                ans += 1
            t.append(i)
        elif t[-1] == i:
            t.append(i)
        else:
            last_removed = t.pop(-1)
    if last_removed == "D":
        ans += 1
    return ans


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    s = input()

    result = countingValleys(n, s)

    fptr.write(str(result) + '\n')

    fptr.close()
