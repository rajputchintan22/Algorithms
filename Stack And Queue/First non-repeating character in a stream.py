for t in range(0, int(input())):
    size_of_arrays = int(input())
    array = input().split()
    alphabets = [0] * 26
    queue = []
    ans = []
    for i in array:
        index = ord(i)-97
        alphabets[index] += 1
        if alphabets[index] == 1:
            queue.append(i)
        elif alphabets[index] == 2:
            queue.remove(i)
        if len(queue) == 0:
            ans.append('-1')
        else:
            ans.append(queue[0])
    print(*ans, sep=' ')
