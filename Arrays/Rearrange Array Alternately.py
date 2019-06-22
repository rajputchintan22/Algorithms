for i in range(0, int(input())):
    size_of_arrays = int(input())
    array = input().split()
    array2 = []
    for j in range(0, (size_of_arrays//2)):
        array2.append(array[size_of_arrays-1-j])
        array2.append(array[j])
    if size_of_arrays % 2 != 0:
        array2.append(array[size_of_arrays//2])
    print(*array2)