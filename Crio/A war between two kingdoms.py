T = int(input())
for t in range(T):
    n = int(input())
    A = list(map(int, input().strip().split()))
    B = list(map(int, input().strip().split()))
    A.sort()
    B.sort()
    A.reverse()
    B.reverse()
    i = 0
    j = 0
    ans = 0
    while i< n and j<n:
        if A[i] > B[j]:
            i += 1
            j += 1
            ans += 1
        else:
            j += 1
    print(ans)