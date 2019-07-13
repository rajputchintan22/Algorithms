def find_Odd_Numbers(number1):
    count = 0
    while number1 > 0:
        count += number1 % 2
        number1 = number1/2
    if count % 2 == 0:
        return False
    else:
        return True

for test_cases in range(int(input())):
    odd_counter = 0
    even_counter = 0
    l1 = []
    for numbers in range(int(input())):
        num = int(input())
        t = len(l1)
        if num % 2 == 0:
            even_counter += 1
        else:
            odd_counter += 1
        l1.append([])
        for i in range(0, t-1):
            for k in range(0, len(l1[i])):
                temp = l1[i][k] ^ num
                l1[i+1].append(temp)
                if find_Odd_Numbers(temp):
                    odd_counter += 1
                else:
                    even_counter += 1
        l1[0].append(num)
        print(even_counter, " ", odd_counter)



