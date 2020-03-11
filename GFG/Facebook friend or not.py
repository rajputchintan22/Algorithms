for t in range(int(input())):
    m, n = input().split(" ")
    m = int(m)
    n = int(n)
    persons = input().split(" ")
    connections = [-1]*m
    for i in range(0, n):
        k = input().split(" ")
        if k[0] == "addincircle":
            in1 = persons.index(k[1])
            in2 = persons.index(k[2])
            connections[in2] = in1
        else:
            in1 = persons.index(k[1])
            in2 = persons.index(k[2])
            while connections[in1] != -1:
                in1 = connections[connections[in1]]
            while connections[in2] != -1:
                in2 = connections[connections[in2]]
            if persons[in2] == persons[in1]:
                print(1)
            else:
                print(0)


