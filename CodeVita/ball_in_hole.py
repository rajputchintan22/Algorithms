nh = int(input())
d_holes = list(map(int, input().split()))
nb = int(input())
d_balls = list(map(int, input().split()))
ans = []
stack_holes =[]
for i in range(-1, (0-nh-1), -1):
    stack_holes.append([d_holes[i], nh + i+1, nh + i+1])
for k in d_balls:
    for j in range(0, nh):
        if k <= stack_holes[j][0] and stack_holes[j][1] != 0:
            ans.append(stack_holes[j][2])
            stack_holes[j][1] -= 1
            break
    else:
        ans.append(0)
print(*ans, sep=' ')