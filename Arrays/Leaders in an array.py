for i in range(0, int(input())):
    size_of_arrays = int(input())
    array = list(map(int, input().split()))
    leader = []
    leader.append(array[-1])
    for j in range(size_of_arrays - 1, -1):
        if array[j] > leader[-1]:
            leader.append(array[j])
    leader.reverse()
    print(*leader)
