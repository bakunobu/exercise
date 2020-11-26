def find_age(y:int, m:int) -> int:
    cur_year = 2020
    cur_month = 11
    
    if cur_m > m:
        return(cur_year - y - 1)
    else:
        return(cur_year - y)