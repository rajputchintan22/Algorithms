no = int(input())
radius = list(map(int, input().split()))
radius.sort()
ans = 0
while len(radius) > 0:
    k = 0
    while k < len(radius):
        j = k
        Check = 0
        while j < len(radius):
            if radius[j] > radius[k]:
                Check = 1
                break
            j += 1
        if Check == 1:
            radius.pop(k)
            k = j - 1
        else:
            radius.pop(k)
            ans += 1
            k += len(radius)
print(ans)