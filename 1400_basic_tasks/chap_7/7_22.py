def compet_res() -> str:
    scores = {}
    for x in range(2):
        part = x
        scores[part]= 0
        print('Предметы {}-го набора'.format(part+1))
        for i in range(8):
            while True:
                try:
                    score = float(input('Введите цену: '))
                    scores[part] += score
                    break
                except ValueError:
                    print('Используйте только числа (разделитель - \'.\')')
    
    if scores[0] < scores[1]:
        return('Второй набор дороже')
    elif scores[0] > scores[1]:
        return('Первый набор дороже')
    else:
        return('Наборы стоят одинаково')


print(compet_res())
    