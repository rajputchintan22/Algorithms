import math


def nCr(n, r):
    f = math.factorial
    return int(f(n) / f(r) / f(n - r))


for test_case in range(0, int(input())):
    l1 = list(map(int, input().split(" ")))
    ansh = nCr(l1[0], l1[1]) - nCr(l1[0] - l1[2], l1[1])
    chhed = nCr(l1[0], l1[1])
    ansh1 = ansh // math.gcd(ansh, chhed)
    chhed1 = chhed // math.gcd(ansh, chhed)
    m = 1000000007
    print((ansh1 * pow(chhed1, m - 2, m)) % m)
