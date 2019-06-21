t = int(input())
for i in range(0, t):
    size_of_arrays = list(map(int, input().split()))
    array1 = list(map(int, input().split()))
    array2 = list(map(int, input().split()))
    array1 += array2
    array1.sort()
    print(*array1)