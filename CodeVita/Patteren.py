n = int(input())

Sequence = []
Charec = 1
for i in range(n):
    te = ""
    for k in range(i):
        te += "**"
    for j in range(n-i):
        te += str(Charec)
        te += "0"
        Charec += 1
    Sequence.append(te)

Sequence2 = []
for i in range(n):
    te = ""
    for j in range(i):
        te += str(Charec)
        te += "0"
        Charec += 1
    te += str(Charec)
    Charec += 1
    Sequence2.append(te)

pattern = []
for i in range(n):
    pattern.append(Sequence[i] + Sequence2[n - i - 1])

for i in range(n):
    print(pattern[i])