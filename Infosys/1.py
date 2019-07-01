def numOfIds(pool):
    l1 = [int(d) for d in str(pool)]
    useful_digits = [i for i, x in enumerate(l1) if x != 8]
    total_useful_digits = len(useful_digits)
    list_of_8 = []
    for i in range(0, len(l1) - total_useful_digits):
        list_of_8.append(8)
    if len(list_of_8) == 0:
        return 0
    counter = 0
    while len(useful_digits) + len(list_of_8) >= 1:
        try:
            if len(list_of_8) == 0:
                break
            temp = 0
            list_of_8.pop(0)
            temp += 1
            while len(useful_digits) > 0 and temp < 11:
                useful_digits.pop(0)
                temp += 1
            while temp < 11:
                list_of_8.pop(0)
                temp += 1
            counter += 1
        except:
            break
    return counter


if __name__ == '__main__':

    pool = input()

    result = numOfIds(pool)
    print(result)