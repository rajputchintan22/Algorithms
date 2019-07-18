# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys
k = int(sys.stdin.readline())
m = int(sys.stdin.readline())
height = []
for i in range(0,m):
    height.append(int(sys.stdin.readline()))

previous_peak = [0]*m
peaks = [0]*m
for i in range(1,m-1):
    if height[i]> height[i-1] and height[i] > height[i+1]:
        peaks[i] = 1
count = 1
for i in range(1,m-1):
    if peaks[i] == 0:
        previous_peak[i] = count
        count += 1
    else:
        count = 1
j = 1
k1 = k
ans = 0
while j < m-1:
    k1 -= 1
    if k1 == 0:
        ans += 1
        k1 = k - previous_peak[j-1] -1
    j += 1
sys.stdout.write(str(ans))
