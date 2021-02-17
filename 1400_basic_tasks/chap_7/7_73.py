from main_funcs import get_input


def count_divs(n:int) -> tuple:
    div_three = 0
    div_seven = 0
    for _ in range(n):
        a = get_input('Введите число: ', False)
        if a % 3 == 0:
            div_three += 1
        if a % 7 == 0:
            div_seven += 1
    return(div_three, div_seven)