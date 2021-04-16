# a
def transform_one(my_list:list) -> list:
    my_list = [x * 2 if not x % 4 else x for x in my_list]
    return(my_list)


# b
def transform_two(my_list:list) -> list:
    my_list = [x ** 2 if not x % 2 else x * 2 for x in my_list]
    return(my_list)


# c
"""
Не вполне ясно, исключает ли наступление одного условия другого.
Я исходил из того, что оба условия могут наступить одновременно.
в противном случае, сначала надо проверять число на четность индекса,
а затем, если индекс нечетный, на четность самого числа:
if not i % 2:
    my_list[i] -= b
else:
    if not my_list[i] % 2:
        my_list[i] += a 
"""

def transform_three(my_list:list, a:int, b:int) -> list:
    for i in range(len(my_list)):
        if not my_list[i] % 2:
            my_list[i] += a
        if not i % 2:
            my_list[i] -= b
    return(my_list)