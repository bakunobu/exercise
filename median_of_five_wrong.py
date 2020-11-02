"""
Срединное из пяти.
Составьте функцию, получающую в аргументах командной строки пять разных целых чисел и выводящую срединное из них.
Решите задачу, использовав меньше семи сравнений для любого ввода.
"""


def triplet_sorting(a: int, b: int, c: int) -> list:
    triplet_1 = []
    if a > b:
        if b > c:
            triplet_1 = [c, b, a]
        else:
            if a > c:
                triplet_1 = [b, c, a]
            else:
                triplet_1 = [b, a, c]
    else:
        if a > c:
            triplet_1 = [c, a, b]
        else:
            if b > c:
                triplet_1 = [a, c, b]
            else:
                triplet_1 = [a, b, c]
    
    return(triplet_1)
    

def median_of_five(a:int, b:int, c:int, d:int, e:int) -> int:
    # triplet_1 (a, b, c) manipulation
    triplet_1 = triplet_sorting(a, b, c)
    
    # triplet_2 (c, d, e) manipulation
    triplet_2 = triplet_sorting(c, d, e)
    
    # indexing of the common element (c)
    i = triplet_1.index(c) # index in the first triplet
    j = triplet_2.index(c) # index in the second triplet
    
    
    # logical part: using a common element to find out all the relations
    if i == 2:
        
        if j == 0:
            return(c)
        
        elif j == 1:
            return(max(triplet_1[1], triplet_2[0]))
        
        elif j == 2:
            if triplet_1[1] > triplet_2[1]:
                
                if triplet_1[0] > triplet_2[0]:
                    
                    if triplet_1[0] > triplet_2[1]:
                        return(triplet_1[0])
                    else:
                        return(triplet_2[1])
                
                else:
                    return(triplet_2[1])
            
            else:
                
                if triplet_1[0] < triplet_2[0]:
                    
                    if triplet_1[1] > triplet_2[0]:
                        return(triplet_1[1])
                    else:
                        return(triplet_2[0])
                
                else:
                    return(triplet_1[1])
    
    elif i == 1:
        
        if j == 0:
            
            if triplet_1[2] > triplet_2[1]:
                return(triplet_2[1])
            else:
                return(triplet_1[2])
        
        elif j == 1:
            return(triplet_1[1])
        
        elif j == 2:
            
            if triplet_1[0] > triplet_2[1]:
                return(triplet_1[0])
            else:
                return(triplet_2[1])
    
    elif i == 0:
        
        if j == 0:
            
            if triplet_1[1] > triplet_2[1]:
                
                if triplet_1[2] > triplet_2[2]:
                    
                    if triplet_1[1] > triplet_2[2]:
                        return(triplet_2[2])
                    else:
                        return(triplet_1[1])
                
                else:
                    return(triplet_1[1])
            
            else:
                
                if triplet_1[2] > triplet_2[1]:
                    return(triplet_2[1])
                else:
                    return(triplet_1[2])
                  
        elif j == 1:
            
            if triplet_1[1] > triplet_2[2]:
                return(triplet_2[2])
            else:
                return(triplet_1[1])
        
        elif j == 2:
            return(triplet_1[0])
        
    
    
            
        

from itertools import permutations
for _ in permutations([1, 2, 3, 4, 5], 5):
    print(_)
    print(median_of_five(* _))






    
        
     
    