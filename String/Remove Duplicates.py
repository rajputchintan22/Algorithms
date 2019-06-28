for t in range(int(input())):
    given = input().split(' ')
    answer = []
    counter = []
    for i in range(0, 256):
        counter.append(0)
    for i in given[0]:
        if counter[ord(i)] == 0:
            counter[ord(i)] +=1
            answer.append(i)
    print("".join(answer))