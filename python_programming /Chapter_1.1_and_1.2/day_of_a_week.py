"""
Составьте программу, получающую дату и выводящую день недели, выпадающий на эту дату.
Программа должна получать три аргу­мента командной строки: m (месяц), d (день) и у (год).
Значение 1 перемен­ной m соответствует январю, 2 -февралю и т.д.
В вы  воде О соответствует воскресенью, 1 -понедельнику, 2 -вторнику и т.д. 
"""

days_dict = {1: 'понедельник',
             2: 'вторник',
             3: 'среда',
             4: 'четверг',
             5: 'пятница',
             6: 'суббота',
             7: 'воскресенье'}


def check_day(m:int, d:int, y:int) -> int:
    """
    Converts a date to a day of a week (Grigorian)
    
    Args:
    =====
    m: int
    month
    d: int
    day
    y: int
    year
    
    Return:
    =======
    d_0: int
    1 for Monday etc
    """
    y_0 = y - (14 - m) / 12
    x = y_0 + y_0 / 4 - y_0 / 100 + y_0 / 400
    m_0 = m + 12 * ((14 - m) / 12) - 2
    d_0 = (d + int(x) + (31 * m_0) / 12) % 7
    
    return(int(d_0))

day = check_day(2, 15, 2000)
print(days_dict[day])