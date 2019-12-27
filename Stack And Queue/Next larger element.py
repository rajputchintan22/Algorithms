for t in range(0, int(input())):
    size_of_arrays = int(input())
    array = list(map(int, input().split()))
    l = []
    size_of_stack = 0
    ans = [-1] * size_of_arrays
    i = size_of_arrays - 1
    while i >= 0:
        if size_of_stack == 0:
            l.append(array[i])
            size_of_stack += 1
            i -= 1
        elif array[i] >= l[-1]:
            l.pop()
            size_of_stack -= 1
        else:
            ans[i] = l[-1]
            l.append(array[i])
            size_of_stack += 1
            i -= 1
    print(*ans)
