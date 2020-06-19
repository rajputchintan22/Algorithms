for t in range(int(input())):
    given = input()
    mapped = [0] * 26
    total = 0
    for i in given:
        mapped[ord(i) - 97] += 1
        total += 1
    most_frequent = max(mapped)
    j = total - most_frequent
    if j >= most_frequent:
        print(1)
    else:
        print(0)
