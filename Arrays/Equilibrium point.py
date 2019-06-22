for i in range(0, int(input())):
    size_of_arrays = int(input())
    array = list(map(int, input().split()))
    total_left = 0
    total = sum(array)
    if len(array) == 1:
        print(1)
    else:
        flag = 0
        k = 0
        total -= array[0]
        for j in range(1, len(array)):
            try:
                total -= array[j]
                total_left += array[j-1]
                if total_left == total:
                    flag = 1
                    k = j
                    break
            finally:
                pass
        if flag == 0:
            print(-1)
        else:
            print(k+1)

