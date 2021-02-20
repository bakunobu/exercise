from main_funcs import get_input

def cont_even(n:int) -> bool:
    for _ in range(n):
        a = get_input('Введите число', False)
        if a % 2 == 0:
            return(True)
    return(False)