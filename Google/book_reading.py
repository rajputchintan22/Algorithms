for t in range(int(input())):
    temp_var = list(map(int, input().split()))
    torn_pages = list(map(int, input().split()))
    readers = list(map(int, input().split()))
    total_pages = 0
    for i in readers:
        total_pages += temp_var[0] // i
        for j in torn_pages:
            if j % i == 0:
                total_pages -= 1
    print("Case #"+str(t+1)+":"+" "+str(total_pages))

