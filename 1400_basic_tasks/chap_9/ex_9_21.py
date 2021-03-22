def num_div(n:int) -> int:
    n_divs = 0
    for x in range(1, n+1):
        if not n % x:
            n_divs += 1
    return(n_divs)


def count_n_divs(start:int=120, end:int=140, n:int=5) -> dict:
    div_counter = {}
    for i in range(start, end+1):
        n_divs = num_div(i)
        if n_divs == n:
            div_counter[i] = n_divs
    return(div_counter)


# result
result = count_n_divs(1, 300)