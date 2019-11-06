import math
from fractions import gcd
from functools import reduce
def find_gcd(list):
    x = reduce(gcd, list)
    return x
for t in range(int(input())):
    n = int(input())
    array = list(map(int, input().split()))
    a = 1
    b = 1
    c = 0 - n*2
    num = 0 - int((-b - math.sqrt(b**2 - 4*a*c)) / (2 * a))
    ans = [0] * num
    ans[0] = find_gcd(array[0:num])
    for i in range(1, num):
        ans[i] = array[i-1] // ans[0]
    print(*ans)
