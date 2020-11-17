a, b = 3, 4


def print_stuff(a:float, b:float) -> None:
    print(f'{a}+{b} = {a+b}')
    print(f'{a}-{b} = {a-b}')
    print(f'{a}*{b} = {a*b}')
    try:
        print(f'{a}:{b} = {a/b}')
    except ZeroDivisionError:
        print('Деление на ноль')

print_stuff(a, b)        
print_stuff(a, 0)