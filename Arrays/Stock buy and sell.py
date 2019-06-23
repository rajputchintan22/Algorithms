def to_string(l):
    stg = ""
    for k in range(0, len(l), 2):
        stg += "(" + str(l[k]) + " " + str(l[k + 1]) + ") "
    return stg[0:-1]


for t in range(int(input())):
    n = int(input())
    array = list(map(int, input().split()))
    min_so_far = 0
    max_so_far = 0
    l1 = []
    for i in range(1, n):
        if array[i] < array[max_so_far]:
            l1.append(min_so_far)
            l1.append(max_so_far)
            min_so_far = max_so_far = i
        elif array[i] > array[max_so_far]:
            max_so_far = i
    l1.append(min_so_far)
    l1.append(max_so_far)
    l2 = l1.copy()
    for p in range(0, len(l1)-1):
        if l1[p] in l1[p+1:]:
            temp = l1[p]
            l2.remove(temp)
            l2.remove(temp)
    if len(l2) > 0:
        print(to_string(l2))
    else:
        print("No Profit")