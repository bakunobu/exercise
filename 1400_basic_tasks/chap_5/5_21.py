

def get_input() -> float:
    while True:
        a = input('Введите стоимость 1 кг сыра: ')
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
    for x in range(50, 1001, 50):
        print(f'{x} г - {calc_cost(price * (x / 1000))[0]} руб.', end=' ')
        print(f'{round(calc_cost(price * (x / 1000))[1], 2)} коп.')
        

if __name__ == '__main__':
    print_price()