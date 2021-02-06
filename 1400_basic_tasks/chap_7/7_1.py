my_sum = 0


for x in range(10):
    while True:
        try:
            a = float(input('Введите число: '))
            my_sum += a
            break
        except ValueError:
            print('Вы ввели не число!')
    
print(my_sum)
