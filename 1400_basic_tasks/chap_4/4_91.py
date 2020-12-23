def is_loop(y:int) -> bool:
    res = y % 4 == 0
    res = res and (y % 400 == 0 or y % 100 != 0)
    return(res)


def prev_day(y:int, m:int, d:int) -> tuple:
    if m == 1 and d == 1:
        return(y-1, 12, 31)
    else:
        if is_loop(y):
                month_duration = {1:31,
                      2:29,
                      3:31,
                      4:30,
                      5:31,
                      6:30,
                      7:31,
                      8:31,
                      9:30,
                      10:31,
                      11:30,
                      12:31}
        else:
                month_duration = {1:31,
                      2:28,
                      3:31,
                      4:30,
                      5:31,
                      6:30,
                      7:31,
                      8:31,
                      9:30,
                      10:31,
                      11:30,
                      12:31}
        if d == 1:
            return(y, m-1,
                   month_duration.get(m-1))
        else:
            return(y, m-1, d-1)


def prev_day(y:int, m:int, d:int) -> tuple:
    if m == 12 and d == 31:
        return(y+1, 1, 1)
    else:
        if is_loop(y):
            month_duration = {1:31,
                      2:29,
                      3:31,
                      4:30,
                      5:31,
                      6:30,
                      7:31,
                      8:31,
                      9:30,
                      10:31,
                      11:30,
                      12:31}
        else:
            month_duration = {1:31,
                      2:28,
                      3:31,
                      4:30,
                      5:31,
                      6:30,
                      7:31,
                      8:31,
                      9:30,
                      10:31,
                      11:30,
                      12:31}
        if d == month_duration.get(m):
            return(y, m+1, 1)
        else:
            return(y, m+1, d+1)