def which_result(a: int,
                 b: int,
                 c: int,
                 d: int) -> bool:
    partial = a / b
    return(partial in (c, d))

