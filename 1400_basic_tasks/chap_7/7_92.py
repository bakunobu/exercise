from main_funcs import get_input


def get_neg_marks(n:int=28) -> bool:
    for _ in range(n):
        g = get_input('Укажите оценку: ', False)
        if g == 2:
            return(False)
    return(True)