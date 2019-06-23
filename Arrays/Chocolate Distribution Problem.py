for t in range(int(input())):
    n = int(input())
    array = list(map(int, input().split()))
    students = int(input())
    if students > 1:
        array.sort()
        minimum_diff = 1000000
        print(array)
        for i in range(0, n-students+1):
            temp = array[i+students-1] - array[i]
            print(array[i+students-1])
            if temp < minimum_diff:
                minimum_diff = temp
        print(minimum_diff)
    else:
        print(0)