priority = {
    '(': 1,
    ')': 1,
    '[': 2,
    ']': 2,
    '{': 3,
    '}': 3
}
for t in range(0, int(input())):
    stg = list(input())
    k = []
    t = 0
    for i in stg:
        if t == 0:
            k.append(i)
            t += 1
        elif priority[k[-1]] == priority[i]:
            k.pop()
            t -= 1
        else:
            k.append(i)
            t += 1
    if len(k) == 0:
        print("balanced")
    else:
        print("not balanced")


