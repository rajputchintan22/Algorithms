import math


def compare_list(l1, l2):
    temp = min(l1[1], l2[1])
    num1 = int(l1[0] / pow(10, l1[1] - temp))
    num2 = int(l2[0] / pow(10, l2[1] - temp))
    if num1 > num2:
        return True
    elif l1[0] == l2[0]:
        return False
    elif num2 == num1:
        if l1[1] > l2[1]:
            d1 = int(l1[0] % pow(10, l1[1] - temp))
            d2 = l2[0]
            return compare_list([d1, l1[1]-temp-1], [d2, temp])
        else:
            d1 = int(l2[0] % pow(10, l2[1] - temp))
            d2 = l1[0]
            return not compare_list([d1, l2[1] - temp-1], [d2, temp])

    return False


def insertion_sort(arr):
    for q in range(1, len(arr)):
        key = arr[q]
        r = q - 1
        while r >= 0 and compare_list(key, arr[r]):
            arr[r + 1] = arr[r]
            r -= 1
        arr[r + 1] = key


for t in range(int(input())):
    n = int(input())
    array = list(map(int, input().split()))
    l = []
    biggest_number = []
    for i in array:
        l.append([i, int(math.log10(i))])
    insertion_sort(l)
    for j in l:
        biggest_number.append(j[0])
    print(*biggest_number, sep='')
