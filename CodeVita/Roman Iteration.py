def write_roman(num):
    num1 = [1, 4, 5, 9, 10, 40, 50, 90, 100, 400, 500, 900, 1000]
    sym = ["I", "IV", "V", "IX", "X", "XL", "L", "XC", "C", "CD", "D", "CM", "M"]
    i = 12
    stg = ""
    while num > 0:
        div = num // num1[i]
        num = num % num1[i]
        while div:
            div -= 1
            stg += sym[i]
        i -= 1
    return stg


def loop(roman_num):
    base = -1
    for i in list(roman_num):
        temp = ord(i) - 65 + 11
        if temp > base:
            base = temp
    k = len(roman_num) - 1
    total = 0
    for i in list(roman_num):
        total += (ord(i) - 65 + 10) * pow(base, k)
        k -= 1
    return total


number = int(input())
ans = number
while True:
    number = ans
    if not (1 <= number <= 3999):
        break
    ans = loop(write_roman(number))
print(ans)
