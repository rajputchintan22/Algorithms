all_linear_magic = [[6, 1, 8, 7, 5, 3, 2, 9, 4], [4, 3, 8, 9, 5, 1, 2, 7, 6], [2, 7, 6, 9, 5, 1, 4, 3, 8],
                    [8, 1, 6, 3, 5, 7, 4, 9, 2], [2, 9, 4, 7, 5, 3, 6, 1, 8], [4, 9, 2, 3, 5, 7, 8, 1, 6],
                    [6, 7, 2, 1, 5, 9, 8, 3, 4], [8, 3, 4, 1, 5, 9, 6, 7, 2], [6, 1, 8, 7, 5, 3, 2, 9, 4],
                    [4, 3, 8, 9, 5, 1, 2, 7, 6], [2, 7, 6, 9, 5, 1, 4, 3, 8]]

for t in range(0, int(input())):
    n = int(input())
    mat = []
    temp2 = []
    for i in range(n):
        x = list(map(int, input().split()))
        temp2 += x
        mat.append(x)
    all_zeroes = []
    for i in all_linear_magic:
        count = 0
        for j in range(9):
            temp2[j] -= i[j]
            if temp2[j] == 0:
                count += 1
        all_zeroes.append(count)
    temp3 = max(all_zeroes)
    i = all_zeroes.index(temp3)
    if temp3 == 0:
        print(0)


