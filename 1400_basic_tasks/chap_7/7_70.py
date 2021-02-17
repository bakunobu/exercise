from main_funcs import get_input

# a
def calc_fallout(moist:float=0.0) -> int:
    counter = 0
    m = get_input('Укажите число осадков: ')
    while m == moist:
        counter += 1
        m = get_input('Укажите число осадков: ')
    return(counter)


# b
def calc_fallout(moist:float=0.0, days:int=31) -> int:
    counter = 0
    m = get_input('Укажите число осадков: ')
    while m == moist and counter < days:
        counter += 1
        m = get_input('Укажите число осадков: ')
    return(counter)
    