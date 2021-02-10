def compet_res() -> str:
    scores = {}
    for x in range(2):
        part = x
        scores[part]= 0
        print('Результаты {}-го спортсмена'.format(part+1))
        for i in range(10):
            while True:
                try:
                    score = float(input('Введите результат: '))
                    scores[part] += score
                    break
                except ValueError:
                    print('Используйте только числа (разделитель - \'.\')')
    
    if scores[0] < scores[1]:
        return('Второй спортсмен победил')
    elif scores[0] > scores[1]:
        return('Первый спортсмен победил')
    else:
        return('Спортсмены показали одинаковый результат')


print(compet_res())
    