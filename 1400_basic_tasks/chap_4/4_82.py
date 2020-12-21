def print_age(age:int) -> None:
    if 11 <= age <= 19:
        return('Мне {age} лет.')
    elif age % 10 == 0:
        return('Мне {age} лет.')
    elif age % 10 == 1:
        return('Мне {age} год.')
    else:
        return('Мне {age} года.')