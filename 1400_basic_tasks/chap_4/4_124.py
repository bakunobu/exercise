def whos_older(age_1:int, age_2:int) -> str:
    if age_1 > age_2:
        return('Митя')
    elif age_1 < age_2:
        return('Вася')
    else:
        return('Одного возраста')