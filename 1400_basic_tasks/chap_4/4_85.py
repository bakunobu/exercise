def month_to_years(n:int) -> int:
    years = n // 12
    month = n % 12
    
    if 11 <= years <= 19:
        y_ending = 'лет'
    elif years % 10 == 0:
        y_ending = 'лет'
    elif years % 10 == 1:
        y_ending = 'год'
    elif years % 10 in (2, 3, 4):
        y_ending = 'года'
    else:
        y_ending = 'лет'
        
    if month == 0:
        print('{years} {y_ending} ровно')
    elif 11 <= month <= 19:
        print('{years} {y_ending} {month} месяцев')
    elif month % 10 == 0:
        print('{years} {y_ending} {month} месяцев')
    elif month % 10 == 1:
        print('{years} {y_ending} {month} месяц')
    elif month % 10 in (2, 3, 4):
        print('{years} {y_ending} {month} месяца')
    else:
        print('{years} {y_ending} {month} месяцев')