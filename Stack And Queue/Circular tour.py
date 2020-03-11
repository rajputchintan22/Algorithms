'''
    lis[][0]:Petrol
    lis[][1]:Distance
'''


# Your task isto complete this function
# Your function should return the starting point
def tour(lis, n):
    path = []
    sum = 0
    k = []
    for j in range(0, n):
        temp = lis[j][0] - lis[j][1]
        path.append(temp)
        sum += temp
        if temp > 0:
            k.append(j)
    if sum < 0:
        return -1
    else:
        for j in k:
            sum2 = 0
            for t in range(0, n):
                p = (j+t)%n
                sum2 += path[p]
                if sum2 < 0:
                    break
            else:
                return j



# {
#  Driver Code Starts
t = int(input())
for i in range(t):
    n = int(input())
    arr = list(map(int, input().strip().split()))
    lis = []
    for i in range(1, 2 * n, 2):
        lis.append([arr[i - 1], arr[i]])
    # print n, arr
    print(tour(lis, n))
