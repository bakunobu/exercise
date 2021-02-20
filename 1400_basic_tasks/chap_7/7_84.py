from main_funcs import get_input


def count_pos(n:int, p:int=5) -> bool:
    pos_count = 0
    for _ in range(n):
        a = get_input('Введите число: ', False)
        if a >= 0:
            pos_count += 1
        if pos_count > p:
            break
    print(pos_count <= p)