def remover(stg):
    temp_new_string = []
    previous = stg[0]
    temp_new_string.append(stg[0])
    flag = 0
    delete_flag = 0
    for i in range(1, len(stg)):
        if previous == stg[i]:
            if flag == 0:
                temp_new_string.pop(-1)
                flag = 1
                delete_flag = 1
        else:
            temp_new_string.append(stg[i])
            flag = 0
            previous = stg[i]
    return "".join(temp_new_string), delete_flag


for t in range(int(input())):
    given = input()
    new_string, flg = remover(given)
    while flg == 1 and len(new_string) > 0:
        new_string, flg = remover(new_string)
    print("".join(new_string))
