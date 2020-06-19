#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'decryptPassword' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def decryptPassword(s):
    s = list(s)
    numbers = []
    count = 0
    for i in s:
        if 49 <= ord(i) <= 57:
            numbers.append(i)
            count += 1
        else:
            break
    if count > 0:
        s = s[count:]
    ans = ""
    t = len(s)
    j = 0
    while j < t:
        if s[j] == "*":
            t1 = ans[-1]
            t2 = ans[-2]
            ans = ans[:-2] + t1 + t2
        elif s[j] == "0":
            ans += "" + numbers.pop(-1)
        else:
            ans += s[j]
        j += 1
    return ans


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = decryptPassword(s)

    fptr.write(result + '\n')

    fptr.close()
