def h_to_min(h:int) -> int:
    return(h * 60)


def min_to_sec(m:int) -> int:
    return(m * 60)

def sec_to_deg(s: int) -> float:
    return(s * 0.1)

def main(h:int, m:int, s:int) -> float:
    m += h_to_min(h)
    s += min_to_sec(m)
    return(sec_to_deg(s) / 12)


print(main(6, 0, 0))