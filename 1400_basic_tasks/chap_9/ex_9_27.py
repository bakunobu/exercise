def div_to_list(n:int) -> list:
    div_list = [x for x in range(1, n+1) if not n % x]
    return(div_list)


def div_sum(start:int=50, end:int=70) -> dict:
    sum_dict = {n:sum(div_to_list(n)) for n in range(start, end+1)}
    return(sum_dict)


div_sum_dict = div_sum()

for k, v in sorted(div_sum_dict.items()):
    print(k, v, sep="-> ")
        