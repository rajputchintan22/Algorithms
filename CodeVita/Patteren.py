n = int(input())
First_Sequence = 10
Second_Sequence = 0
Third_Sequence = 0
Temp_ss = 0
for i in range(0, n):
    stg = ""
    if i == 0:
        for j in range(0, n):
            stg += str(First_Sequence)
            First_Sequence += 10
        Second_Sequence = (First_Sequence - 10) * ((First_Sequence - 10) // 10) + 10
        Temp_ss = Second_Sequence
        for j in range(0, n):
            stg += str(Second_Sequence)
            Second_Sequence += 10
        Third_Sequence = (Second_Sequence - 10) // 10 + 1
        stg += str(Third_Sequence)
    else:
        for j in range(0, i):
            stg += "**"
        for j in range(0, n-1):
            stg += str(First_Sequence)
            First_Sequence += 10
        Second_Sequence = Temp_ss - (n - i) * 10
        Temp_ss = Second_Sequence
        for j in range(0, n-i-1):
            stg += str(Second_Sequence)
            Second_Sequence += 10
        Third_Sequence = Third_Sequence - (n - i + 1)
        stg += str(Third_Sequence)
    print(stg)
