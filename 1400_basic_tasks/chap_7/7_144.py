def calc_max_sum_min_prod(n:int) -> tuple:
    max_sum = False
    min_prod = False
    msg = 'Укажите числа a и b (через запятую)'
    
    for _ in range(n):
        
        try:
            a, b = [float(x) for x in input(msg).split(',')]
        except ValueError:
            print('Используйте вещественные числа и запятую для их разделения')
        
        my_sum = a + b
        my_prod = a * b
        
        if not max_sum:
            max_sum = my_sum
        
        if not min_prod:
            min_prod = my_prod
        
        if max_sum < my_sum:
            max_sum = my_sum
        
        if min_prod > my_prod:
            min_prod = my_prod
    return(max_sum, min_prod)


test_n = 10
# a
print(calc_max_sum_min_prod(test_n)[0])

# b
print(calc_max_sum_min_prod(test_n)[1])