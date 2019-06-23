for t in range(int(input())):
    n = int(input())
    array = list(map(int, input().split()))
    counter = 0
    left = [0]
    left_max = array[0]
    right = []
    right_max = array[-1]
    for i in range(1, n-1):
        left.append(left_max)
        right.append(right_max)
        if array[i] > left_max:
            left_max = array[i]
        if array[n-i-1] > right_max:
            right_max = array[n-i-1]
    right.append(0)
    right.reverse()
    for i in range(1, n-1):
        if array[i] < left[i] and array[i] < right[i]:
            counter += min(left[i], right[i]) - array[i]
    print(counter)