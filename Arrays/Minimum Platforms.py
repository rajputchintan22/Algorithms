for trial in range(int(input())):
    n = int(input())
    arrival = list(map(int, input().split()))
    depart = list(map(int, input().split()))
    dictionary = []

    for i in range(n):
        dictionary.append((arrival[i], 'a'))
        dictionary.append((depart[i], 'd'))

    dictionary = sorted(dictionary)
    count = 0
    max_count = 0
    for i in range(2 * n):
        if dictionary[i][1] == 'a':
            count += 1
        else:
            count -= 1
        if count > max_count:
            max_count = count
    print(max_count)
