def comp_int(t:int, p:float=1000.0, i:float=0.02) -> float:
    return(p * (1 + i) ** t)

# a
for i in range(1, 11):
    print(i, comp_int(i) - comp_int(i-1), sep=': ')
    

# b
for i in range(3, 13):
    print(i, comp_int(i), sep=': ')