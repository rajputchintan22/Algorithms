roman_to_int = {
    'I': 1,
    'V': 5,
    'X': 10,
    'L': 50,
    'C': 100,
    'D': 500,
    'M': 1000
}
for t in range(int(input())):
    given = list(input())
    given.reverse()
    number = 0
    max_so_far = roman_to_int[given[0]]
    for i in given:
        if roman_to_int[i] < max_so_far:
            number -= roman_to_int[i]
        else:
            number += roman_to_int[i]
    print(number)