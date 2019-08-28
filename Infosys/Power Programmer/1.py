import sys


def my_max(a):
    max_till_now = a[0]
    current = a[0]
    for i in range(1, len(a)):
        current = max(a[i], current + a[i])
        max_till_now = max(max_till_now, current)

    return max_till_now

n = int(sys.stdin.readline())
array = list(map(int, (sys.stdin.readline()).split()))
array2 = []
for i in range(0, n):
    if array[i] == 0:
        array2.append(1)
    else:
        array2.append(-1)
i = 0
j = n - 1
ans = sum(array) + my_max(array2)
sys.stdout.write(str(ans))
