# a

def calc_sum(num_1:list, num_2:list) -> list:
    num_3 = []
    for i in range(len(num_1) - 1):
        u = num_1[i] + num_2[i]
        if u > 9:
            num_1[i+1] = u // 10
            u %= 10
        num_3.append(u)
    u = num_1[-1] + num_2[-1]
    if u > 9:
        extra_u = u // 10
        u %= 10
        num_3.append(u)
        num_3.append(extra_u)
    else:
        num_3.append(u)
    return(num_3)


# b
def calc_diff(num_1:list, num_2:list) -> list:
    num_3 = []
    for i in range(len(num_1 - 1)):
        if num_1[i] < num_2[i]:
            num_1[i + 1] -= 1
            num_1[i] += 10
        u = num_1[i] - num_2[i]
        num_3.append(u)
    u = num_1[-1] - num_2[-1]
    num_3.append(u)
    return(num_3)