def div_to_list(n:int) -> list:
    div_list = [x for x in range(1, n+1) if not n % x]
    return(div_list)


def div_sum(start:int, end:int) -> dict:
    sum_dict = {n:sum(div_to_list(n)) for n in range(start, end+1) if not sum(div_to_list(n)) % 10}
    return(sum_dict)


div_sum_dict = div_sum(300, 600)

for k, v in sorted(div_sum_dict.items()):
    print(k, v, sep="-> ")