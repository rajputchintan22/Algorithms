for t in range(int(input())):
    n = list(map(int, input().split()))
    array = []
    for i in range(0, n[1]):
        array.append(list(map(int, input().split())))
    ans = list(range(1, n[0]+1))
    for i in array:
        for j in range(i[0]-1, i[1]):
            ans[j] += i[2]
    print(*ans)
