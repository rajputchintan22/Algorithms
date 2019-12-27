def converter(strg):
    i = strg.index('#')
    a = strg[i-1]
    a = chr(((ord(a)-65)+1) % 26+65)
    strg[i-1] = a
    strg.pop(i)
    return strg

for t in range(0, int(input())):
    str1 = list(input())
    str2 = list(input())
    while '#' in str1:
        str1 = converter(str1)
    while '#' in str2:
        str2 = converter(str2)
    if str2 == str1:
        print("Yes")
    else:
        print("No")