def maxColumn(L):
    return list(map(max, zip(*L)))

n = int(input())
t = int(input())
racers = []
steps_distance = []
distance_cover = []
for i in range(0, n):
    racers.append(list(map(int, input().split())))
    steps_distance.append(racers[i].pop(-1))
seconds_partcipants = []
for i in range(0, n):
    distance_cover.append([])
    for j in range(0, t, 2):
        k = ((racers[i][j]+racers[i][j+1])*steps_distance[i])+sum(distance_cover[i])

        distance_cover[i].append(k)
maxes = maxColumn(distance_cover)
counts = []
for i in range(0, n):
    counts.append(0)
for i in range(0, len(distance_cover[0])):
    for j in range(0, len(distance_cover)):
        if distance_cover[j][i] == maxes[i]:
            counts[j] += 1
k = max(counts)
for i in range(0, n):
    if counts[i] == k:
        print(i+1)
        break

