def find_Odd_Numbers(number1):
    count = 0
    while number1 > 0:
        count += number1 % 2
        number1 = number1 // 2
    return count % 2

for test_cases in range(int(input())):
    odd_counter = 0
    even_counter = 0
    l1 = []
    for numbers in range(0, int(input())):
        num = int(input())
        odd_counter += find_Odd_Numbers(num)
        even_counter += 1
        k = len(l1)
        for i in range(0, k-1):
            temp = num ^ l1[k]
            odd_counter += find_Odd_Numbers(temp)
            l1.append(temp)
            even_counter += 1
        print(even_counter - odd_counter, " ", odd_counter)



