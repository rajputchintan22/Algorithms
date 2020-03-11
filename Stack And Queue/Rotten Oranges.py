def access_element_1D(i, j):
    return n * i + j


def access_element_2D(one_d_index):
    return (one_d_index // n) , one_d_index % n


for t in range(int(input())):
    m, n = map(int, input().split())
    arr = list(map(int, input().split()))
    size = m * n
    final = 0
    prev_sum = 0
    for i in arr:
        if i == 1:
            final += 2
            prev_sum += 1
        else:
            final += i
            prev_sum += i
    current_sum = prev_sum
    time = 0
    arr2 = arr[:]
    if final == 0:
        print(-1)
    elif prev_sum == final:
        print(0)
    else:
        while True:
            for k in range(0, size):
                if arr[k] == 2:
                    i, j = access_element_2D(k)
                    left = access_element_1D(i, j - 1)
                    right = access_element_1D(i, j + 1)
                    up = access_element_1D(i - 1, j)
                    down = access_element_1D(i + 1, j)
                    if 0 <= left <= size - 1 and n > j - 1 >= 0:
                        if arr[left] == 1:
                            arr2[left] = 2
                    if 0 <= right <= size - 1 and n > j + 1 >= 0:
                        if arr[right] == 1:
                            arr2[right] = 2
                    if 0 <= up <= size - 1 and m > i - 1 >= 0:
                        if arr[up] == 1:
                            arr2[up] = 2
                    if 0 <= down <= size - 1 and m > i + 1 >= 0:
                        if arr[down] == 1:
                            arr2[down] = 2
            prev_sum = current_sum
            current_sum = sum(arr2)
            del arr
            arr = arr2[:]
            time += 1
            if current_sum == final:
                print(time)
                break
            if current_sum == prev_sum:
                print(-1)
                break