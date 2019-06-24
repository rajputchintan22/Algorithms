for t in range(int(input())):
    N = int(input())
    arr = list(map(int, input().split()))
    for i in range(0, N - 1):
        if i % 2 == 0:
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
        if i % 2 == 1:
            if arr[i] < arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
    print(*arr)