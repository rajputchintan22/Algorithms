for t in range(0, int(input())):
    size_of_arrays = int(input())
    array = list(map(int, input().split()))
    ans = 0
    counter = 0
    while counter < size_of_arrays-1:
        if array[counter] == array[counter+1] - 1:
            ans += 1
            while (array[counter] == array[counter+1] - 1) and counter < size_of_arrays-1:
                counter += 1
        else:
            counter += 1
    print(ans)