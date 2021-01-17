def calc_factorial(n:int) -> int:
    if n == 0:
        return(1)
    else:
        return(n * calc_factorial(n-1))
    
    
def nonlin_fact_sum(n:int, x:int=2) -> float:
    part_fact = [x ** i / calc_factorial(i) for i in range(n+1)]
    return(sum(part_fact))


def get_num() -> int:
    while True:
        try:
            n = int(input('Введите число от 2 до 10: '))
            if 1 < n <= 10:
                return(n)
        except ValueError:
            print('Используйте только числа от 2 до 10!')
            
n = get_num()
result = nonlin_fact_sum(n)