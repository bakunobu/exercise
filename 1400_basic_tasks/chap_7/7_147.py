from main_funcs import get_input


def calc_interval(n:int) -> int:
    msg = 'Укажите число учащихся в классе: '
    num_stud = [get_input(msg, False) for x in range(n)]
    return(max(num_stud) - min(num_stud))