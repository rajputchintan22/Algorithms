for t in range(int(input())):
    given = input().split(' ')
    flag = 0
    counter = []
    for i in range(0, 26):
        counter.append(0)
    for i in given[0]:
        counter[ord(i) - 97] += 1
    for i in given[1]:
        counter[ord(i) - 97] -= 1
    for i in counter:
        if i != 0:
            flag = 1
    if flag == 0:
        print("YES")
    else:
        print("NO")