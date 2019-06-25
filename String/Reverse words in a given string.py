for t in range(int(input())):
    array = input().split('.')
    n = len(array)
    print(*reversed(array), sep='.')