def feb_fallout(prev_year:float=44.0, is_leap:bool=False) -> bool:
    tot_fall = 0
    if is_leap:
        n = 29
    else:
        n = 28
    for x in range(n):
        while True:
            try:
                f = float(input(f'Укажите число осадков {x+1} февраля: '))
                tot_fall += f
                break
            except ValueError:
                print('Используйте только числа (разделитель - \'.\')')
    return(tot_fall > prev_year)


print(feb_fallout())