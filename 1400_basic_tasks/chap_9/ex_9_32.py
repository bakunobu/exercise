def div_to_list(n:int) -> list:
    div_list = [x for x in range(1, n+1) if not n % x]
    return(div_list)


def div_sum(a:int, b:int) -> list:
    sum_list = [(n,sum(div_to_list(n)),) for n in range(a, b+1)]
    return(sum_list)


def max_sum_div(my_list:list) -> int:
    return(sorted(my_list, key=lambda x: x[1], reverse=True)[0][0])


def main(a:int, b:int) -> int:
    sum_list = div_sum(a, b)
    return(max_sum_div(sum_list))


print(main(100, 300))