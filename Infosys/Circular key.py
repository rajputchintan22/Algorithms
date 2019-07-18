import sys
x = int(sys.stdin.readline())
n = int(sys.stdin.readline())
t = []
last_add = 0
len_of_l = 1
t.append(int(sys.stdin.readline()))
for i in range(1, n):
    k = int(sys.stdin.readline())
    len_of_l += 1
    temp = (x+1+last_add) % len_of_l
    last_add = temp
    t = t[:last_add]+[k]+t[last_add:]
print(*t)