# a
def calc_series(n:int) -> str:
    num_1 = 1
    num_2 = 2
    den_1 = 1
    den_2 = 1
    for x in range(n-2):
        num_1, num_2 = num_2, num_1 + num_2
        den_1, den_2 = den_2, den_1 + den_2
    return(f'{num_2}/{den_2}')


# b
def save_series(n:int) -> list:
    num_1 = 1
    num_2 = 2
    den_1 = 1
    den_2 = 1
    list_of_partial = []
    list_of_partial.append(f'{num_1}/{den_1}')
    list_of_partial.append(f'{num_2}/{den_2}')
    for x in range(n-2):
        num_1, num_2 = num_2, num_1 + num_2
        den_1, den_2 = den_2, den_1 + den_2
        list_of_partial.append(f'{num_2}/{den_2}')
    return(list_of_partial)

