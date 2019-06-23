for t in range(0, int(input())):
    n = list(map(int, input().split()))
    array = list(map(int, input().split()))
    l2 = []
    for j in range(0, n[0] - 1, n[1]):
        l2 += reversed(array[j:j + n[1]])
    print(*l2)
