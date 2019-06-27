for t in range(int(input())):
    given = input()
    given2 = input()
    if given == given2[2:]+given2[:2] or given == given2[-2:]+given2[:-2]:
        print(1)
    else:
        print(0)