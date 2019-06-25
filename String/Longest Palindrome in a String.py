for t in range(int(input())):
    stg = input()
    i = 0
    j = len(stg) - 1
    index_left = 0
    index_right = 0
    while i < j:
        if str[i] == str[j]:
            index_left = i
            index_right = j
            while str[i] == str[j] and i < j:
                i += 1
                j -= 1

