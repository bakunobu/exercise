my_prod = ``


for x in range(10):
    while True:
        try:
            a = float(input('Введите число: '))
            my_prod *= a
            break
        except ValueError:
            print('Вы ввели не число!')
    
print(my_sum)
