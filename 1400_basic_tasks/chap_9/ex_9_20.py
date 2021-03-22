def num_div(n:int) -> int:
    n_divs = 0
    for x in range(1, n+1):
        if not n % x:
            n_divs += 1
    return(n_divs)


def count_divs(start:int=120, end:int=140) -> dict:
    div_counter = {}
    for n in range(start, end+1):
        n_divs = num_div(n)
        div_counter[n] = n_divs
    return(div_counter)


def fancy_print_div() -> None:
    while True:
        try:
            n = int(input('Введите целое положительное число: '))
            if n > 0:
                break
            else:
                print('Число должно быть больше нуля!')
        except ValueError:
            print('Используете только целые числа бльше нуля')
    div_counter = count_divs(1, n)
    for key in sorted(div_counter.keys()):
        print(key, end='')
        print('+' * div_counter[key])

fancy_print_div()