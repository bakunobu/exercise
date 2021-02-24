from main_funcs import get_iput


def seq_class_heith(n:int) -> bool:
    a_0 = get_input('Укажите рост ученика: ')
    for _ in range(n-1):
        a = get_input('Укажите рост ученика: ')
        if a_0 <= a:
            return(False)
        a_0 = a
    return(True)