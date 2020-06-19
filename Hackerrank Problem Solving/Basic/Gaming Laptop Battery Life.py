#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'getBattery' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY events as parameter.
#

def getBattery(events):
    # Write your code here
    ans = 50
    for i in events:
        ans += i
        if ans > 100:
            ans = 100
        elif ans < 0:
            ans = 0
    return ans

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    events_count = int(input().strip())

    events = []

    for _ in range(events_count):
        events_item = int(input().strip())
        events.append(events_item)

    result = getBattery(events)

    fptr.write(str(result) + '\n')

    fptr.close()
