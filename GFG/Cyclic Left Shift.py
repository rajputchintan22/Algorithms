def rotate_left(l):
    l1 = l[1:] + l[0]
    return l1


for t in range(int(input())):
    i = int(input())
    stg = '{0:032b}'.format(i)
    ans = int(stg, 2)
    if i == 0:
        print("0")
    else:
        for i in range(0, 33):
            stg = rotate_left(stg)
            temp = int(stg, 2)
            if ans < temp:
                ans = temp
        print(ans)

