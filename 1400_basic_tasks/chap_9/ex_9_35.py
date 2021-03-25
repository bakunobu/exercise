def min_notes_n(n:int) -> int:
    amt = []
    for x in range(n, n+11):
        cur_amt = 0
        for i in range(6, -1, -1):
            a = x // 2 ** i
            cur_amt += a
            x -= a * 2 ** i
        amt.append(cur_amt)
    return(amt)
