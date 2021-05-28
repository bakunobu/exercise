def big_num_calc(num:list) -> list:
    num_2 = num[:]
    total = []

    for i in range(len(num) - 1):
        u = num[i] + num_2[i]
        if u > 9:
            num[i+1] += 1
            u %= 10
        total.append(u)
    u = num[-1] + num_2[-1]
    if u > 9:
        total.append(u % 10)
        total.append(1)
    else:
        total.append(u)
        
    return(total)


def pow_two_to_list(power:int=3) -> list:
    num_1 = [1]
    for x in range(power):
        num_1 = big_num_calc(num_1)
    return(num_1) 


# print(pow_two_to_list(100))

print(2 ** 100)
print(* pow_two_to_list(100)[::-1], sep='')

