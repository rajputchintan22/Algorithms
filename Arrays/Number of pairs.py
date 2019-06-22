for i in range(0, int(input())):
    size_of_arrays = list(map(int, input().split()))
    array1 = list(map(int, input().split()))
    array2 = list(map(int, input().split()))
    counter = 0
    array2.sort()
    array1.sort()
    while array2[0] == 1:
        counter += len(array1)
        array2.pop(0)
        if 1 in array1:
            counter -= 1
            array1.pop(0)
    for x in array1:
        for y in array2:
            if x**y > y**x:
                counter += 1
    print(counter)