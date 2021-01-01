days = ['воскресенье',
        'понедельник',
        'вторник',
        'среда',
        'четверг',
        'пятница',
        'суббота',]


# a
def which_day(k:int) -> str:
    i = k % 7
    return(days[i])


# b
def which_d_day(d:int, k:int) -> str:
    i = (k + d) % 7
    return(days[i])
