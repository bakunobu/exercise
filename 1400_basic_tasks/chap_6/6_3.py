def print_odd(a:int=10, b:int=100, is_odd=True):
    i = 1
    if is_odd:
        a += 1
        i += 1
    
    while a <= b:
        print(a)
        a += i
        
        
print_odd()