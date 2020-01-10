if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        (ac1, ac2, ac3, sl, gn) = [int(x) for x in input().split()]
        # print(ac1, ac2, ac3, sl, gn)
        temp = [ac1//1, ac2//2, ac3//3, sl//6, gn//10]

        print(min(temp))