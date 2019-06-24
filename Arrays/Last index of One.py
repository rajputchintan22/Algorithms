for t in range(int(input())):
    array = input().split('')
    n = len(array)
    flag = 0
    for i in range(n-1, -1):
        if array[i] == '1':
            print(i)
            flag = 1
            break
    if flag == 0:
        print(-1)