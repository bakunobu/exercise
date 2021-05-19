def strange_shift(elements:list) -> list:
    new_list = []
    j = len(elements) - 1
    for i in range(6):
        new_list.append(elements[i])
        new_list.append(elements[j - i])
    return(new_list)


# els = [x for x in range(1, 13)]
# print(strange_shift(els))