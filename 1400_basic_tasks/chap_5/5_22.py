

def get_input() -> float:
    while True:
        a = input('Введите стоимость 1 кг конфет: ')
        try:
            a = float(a)
            return(a)
        except ValueError:
            print('Пожалуйста, используйте числа')

            

def calc_cost(x: float) -> tuple:
    r = int(x)
    kop = x - r
    return(r, kop)
             
            
def print_price() -> None:
    price = get_input()
    for x in range(100, 2001, 100):
        print(f'{x} г - {calc_cost(price * (x / 1000))[0]} руб.', end=' ')
        print(f'{round(calc_cost(price * (x / 1000))[1], 2)} коп.')
        

if __name__ == '__main__':
    print_price()