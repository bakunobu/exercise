def calc_factorial(n:int) -> int:
    if n == 0:
        return(1)
    else:
        return(n * calc_factorial(n-1))
    
    
def calc_fact_sum(n:int) -> int:
    fact_list = [calc_factorial(i) for i in range(1, n+1)]
    return(sum(fact_list))


def get_num() -> int:
    while True:
        try:
            n = int(input('Введите число от 2 до 10: '))
            if 1 < n <= 10:
                return(n)
        except ValueError:
            print('Используйте только числа от 2 до 10!')
            
n = get_num()
result = calc_fact_sum(n)