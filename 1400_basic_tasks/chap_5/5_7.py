def print_table(x:float, i:int=20) -> None:
    for j in range(1, i+1):
        print(f'{j}\t{round(x * j, 1)}')
        
        
print_table(20.4)