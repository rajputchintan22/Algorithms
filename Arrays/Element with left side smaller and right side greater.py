for t in range(int(input())):
    n = int(input())
    array = list(map(int, input().split()))
    counter = 0
    left = [0]
    left_max = array[0]
    right = []
    right_min = array[-1]
    for i in range(1, n - 1):
        left.append(left_max)
        right.append(right_min)
        if array[i] > left_max:
            left_max = array[i]
        if array[n - i - 1] < right_min:
            right_min = array[n - i - 1]
    left = left[1:]
    right.reverse()
    flag = 0
    for i in range(1, n - 1):
        if right[i - 1] >= array[i] >= left[i - 1]:
            print(array[i])
            flag = 1
            break
    if flag == 0:
        print(-1)
