def pricing(amt: int) -> None:
    kop = amt % 100
    rub = amt // 100
    
    if 11 <= rub <= 19:
        rub_ending = 'рублей'
    elif rub % 10 == 0:
        rub_ending = 'рублей'
    elif rub % 10 == 1:
        rub_ending = 'рубль'
    elif rub % 10 in (2, 3, 4):
        rub_ending = 'рубля'
    else:
        rub_ending = 'рублей'
        
    if kop == 0:
        print('{rub} {rub_ending} ровно')
    elif 11 <= kop <= 19:
        print('{rub} {rub_ending} {kop} копеек')
    elif rub % 10 == 0:
        print('{rub} {rub_ending} {kop} копеек')
    elif rub % 10 == 1:
        print('{rub} {rub_ending} {kop} копейка')
    elif rub % 10 in (2, 3, 4):
        print('{rub} {rub_ending} {kop} копейки')
    else:
        print('{rub} {rub_ending} {kop} копеек')