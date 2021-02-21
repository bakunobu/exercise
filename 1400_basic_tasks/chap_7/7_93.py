from main_funcs import get_input


def get_engine_power(n:int=30, p:float=200.0) -> bool:
    for _ in range(n):
        hp = get_input('Укажите мощность двигателя: ')
        if hp > p:
            return(True)
    return(False)