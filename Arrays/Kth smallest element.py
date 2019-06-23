for t in range(0, int(input())):
    n = int(input())
    array = list(map(int, input().split()))
    k = int(input())
    array.sort()
    print(array[k-1])