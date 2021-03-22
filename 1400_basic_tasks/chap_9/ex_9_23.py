def num_div(n:int) -> int:
    n_divs = 0
    for x in range(1, n+1):
        if not n % x:
            n_divs += 1
    return(n_divs)


def count_k_divs(a, b, k) -> dict:
    div_counter = {}
    for i in range(a, b+1):
        n_divs = num_div(i)
        if n_divs == k:
            div_counter[i] = n_divs
    return(div_counter)

