def to_string(List):
    return ''.join(List)


def permute(a, l, r, final):
    if l == r:
        final.append(to_string(a))
    else:
        for i in range(l, r + 1):
            a[l], a[i] = a[i], a[l]
            permute(a, l + 1, r, final)
            a[l], a[i] = a[i], a[l]


for t in range(int(input())):
    string = input()
    n = len(string)
    a = list(string)
    final = []
    permute(a, 0, n - 1, final)
    final.sort()
    print(*final)