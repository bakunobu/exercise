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

def prev_day(m:int, d:int) -> tuple:
    if d == 1:
        return(m-1, month_duration.get(m-1))
    else:
        return(m, d-1)


def next_day(m:int, d:int) -> tuple:
    if d <= 27:
        return(m, d+1)
    else:
        if d < month_duration.get(m):
            return(m, d+1)
        else:
            return(m+1, 1)

def prev_next_day(m:int, d:int) -> None:
    print(f'Previos day: {prev_day(m,d)[1]} {prev_day(m,d)[1]}')
    print(f'Next day: {next_day(m, d)[1]} {next_day(m,d)[0]}')
