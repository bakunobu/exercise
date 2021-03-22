def num_div(n:int) -> int:
    n_divs = 0
    for x in range(1, n+1):
        if not n % x:
            n_divs += 1
    return(n_divs)


def count_divs(start:int=120, end:int=140) -> dict:
    div_counter = {}
    for n in range(start, end+1):
        n_divs = num_div(n)
        div_counter[n] = n_divs
    return(div_counter)