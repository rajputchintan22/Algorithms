#!/bin/python3

import math
import os
import random
import re
import sys


def MaxGCD(arr, n, k):
    high1 = max(arr)
    divisors1 = [0] * (high1 + 1)
    for i in range(n):
        for j in range(1, int(math.sqrt(arr[i])) + 1):
            if (arr[i] % j == 0):
                divisors1[j] += 1
                if (j != arr[i] // j):
                    divisors1[arr[i] // j] += 1
    for i in range(high1, 0, -1):
        if (divisors1[i] >= k):
            return i


def findSubsequence(n, numbers, k):
    # Write your code here
    t = MaxGCD(numbers, n, k)
    t2 = t
    ans = []
    for i in numbers:
        if math.gcd(t2, i) == t:
            ans.append(i)
    return ans


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    numbers_count = int(input().strip())

    numbers = []

    for _ in range(numbers_count):
        numbers_item = int(input().strip())
        numbers.append(numbers_item)

    k = int(input().strip())

    result = findSubsequence(numbers_count, numbers, k)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
