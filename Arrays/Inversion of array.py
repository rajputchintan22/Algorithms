import sys


def count(arr, l, r):
    if l < r:
        m = (l+r)//2
        left = count(arr, l, m)  # left inversions
        right = count(arr, m+1, r)  # right inversions
        return merge(arr, l, m, r) + left + right  # all inversions
    return 0


def merge(arr, l, m, r):
    # returns the split inversions
    cnt = 0
    n1 = m-l+1
    n2 = r-m
    left = [0]*(n1+1)
    right = [0]*(n2+1)
    left[-1] = sys.maxsize
    right[-1] = sys.maxsize
    for i in range(n1):
        left[i] = arr[l+i]
    for j in range(n2):
        right[j] = arr[m+j+1]
    i = j = 0
    k = l
    while k <= r:
        '''
        if j == n1:
            arr[k] = right[k]
            k += 1
        elif k == n2:
            arr[k] = left[j]
            j += 1
        '''
        if left[i] <= right[j]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            # remaining elements to the right of the selected element
            cnt += (n1-i)
            j += 1
        k += 1
    return cnt


for _ in range(int(input())):
    n = int(input())
    arr = [int(x) for x in input().strip().split()]
    # This is a beautiful problem, can be found in CLRS as well P-2.4
    print(count(arr, 0, n-1))