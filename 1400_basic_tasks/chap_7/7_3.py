per = 0


for x in range(12):
    while True:
        try:
            a = float(input('Введите число: '))
            per += a
            break
        except ValueError:
            print('Вы ввели не число!')
    
print(per)