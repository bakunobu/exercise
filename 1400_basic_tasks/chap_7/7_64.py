from main_funcs import get_input


def birth_ages(n:int) -> tuple:
    before_1990 = 0
    after_2000 = 0
    for x in range(n):
        y = get_input('Укажите год рождения: ', False)
        if y < 1990:
            before_1990 += 1
        elif y > 2000:
            after_2000 += 1
    return(before_1990, after_2000)