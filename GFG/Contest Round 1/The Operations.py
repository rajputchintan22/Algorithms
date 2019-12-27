def operations(S1, S2):
    return (S1 | (S1 & S2)) ^ (S2 & (S2 | S1))


for t in range(0, int(input())):
    size_of_arrays = int(input())
    array = list(map(int, input().split()))
    maximum = 0
    for i in range(0, size_of_arrays):
        for j in range(i, size_of_arrays):
            temp = operations(array[i], array[j])
            if temp > maximum:
                maximum = temp
    print(maximum)
