class myStack:
    def __init__(self, l):
        self.lis = l
        self.count = k
    def push(self, k):
        temp = []
        while len(self.lis) != 0 and self.lis[-1] > k:
            temp.append(self.lis.pop(-1))
        self.lis.append(k)
        self.lis += reversed(temp)
    def rem(self, k):
        temp =[]
        while self.lis[-1] != k:
            temp.append(self.lis.pop(-1))
        self.lis.pop(-1)
        self.lis += reversed(temp)
    def tos(self):
        return self.lis[-1]


for t in range(int(input())):
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))
    queue = []
    myStackObj = myStack([])
    for i in range(0, k):
        t = arr[i]
        queue.append(t)
        myStackObj.push(t)
    ans = [myStackObj.tos()]
    for i in range(k, n):
        t = arr[i]
        queue.append(t)
        myStackObj.push(t)
        t = queue.pop(0)
        myStackObj.rem(t)
        ans.append(myStackObj.tos())
    print(*ans)