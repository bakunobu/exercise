"""
Срединное из пяти.
Составьте функцию, получающую в аргументах командной строки пять разных целых чисел и выводящую срединное из них.
Решите задачу, использовав меньше семи сравнений для любого ввода.
"""



def median_of_five(a:int, b:int, c:int, d:int, e:int) -> int:
    list_of_three = [min(a, b), max(a, b)]
    if c > list_of_three[1]:
        list_of_three.append(c)
    elif c > list_of_three[0]:
        list_of_three.insert(1, c)
    else:
        list_of_three.insert(0, c)
    
        
    list_of_two = [min(d, e), max(d,e)]
    
    if list_of_two[0] < list_of_three[2]:
        if list_of_two[1] < list_of_three[0]:
            return(list_of_three[0])
        else:
            return(list_of_two[1])
    else:
        if list_of_two[0] < list_of_three[2]:
            return(list_of_two[0])
        else:
            return(list_of_three[2])


from itertools import permutations
for _ in permutations([1, 2, 3, 4, 5], 5):
    print(_)
    print(median_of_five(* _))

    
        
    

    