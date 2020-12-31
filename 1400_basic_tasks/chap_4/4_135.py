def which_season(x:int) -> str:
    if 3 <= x < 6:
        return('Spring')
    elif 6 <= x < 9:
        return('Summer')
    elif 9 <= x < 12:
        return('Fall')
    else:
        return('Winter')