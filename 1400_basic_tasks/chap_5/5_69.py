def calc_factorial(n:int) -> int:
    if n == 0:
        return(1)
    else:
        return(n * calc_factorial(n-1))
    
    
def part_fact_sum(n:int) -> float:
    part_fact = [1 / calc_factorial(i) for i in range(n+1)]
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
result = part_fact_sum(n)