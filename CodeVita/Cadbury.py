p = int(input())
q = int(input())
r = int(input())
s = int(input())
output = 0
for i in range(p, q+1):
    for j in range(r, s+1):
        a = i
        b = j
        remainder = 1
        while remainder != 0:
            if a >= b:
                temp = a // b
                output += temp
                remainder = a % b
                a = remainder
            else:
                temp = b // a
                output += temp
                remainder = b % a
                b = remainder
print(output)