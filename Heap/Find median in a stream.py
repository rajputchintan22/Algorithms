import bisect


def median(lis, n):
    if n % 2 == 0:
        median1 = lis[n // 2]
        median2 = lis[n // 2 - 1]
        med = (median1 + median2) // 2
    else:
        med = lis[n // 2]
    return med


current = []
count = 0
size = int(input())
n = int(input())
print(n)
count += 1
current.append(n)
for t in range(size - 1):
    n = int(input())
    bisect.insort(current, n)
    count += 1
    print(median(current, count))
