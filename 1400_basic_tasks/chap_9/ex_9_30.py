def div_to_list(n:int) -> list:
    div_list = [x for x in range(1, n) if not n % x]
    return(div_list)

i = 0
while i < 999:
    if sum(div_to_list(i)) == i:
        print(i, sum(div_to_list(i)), sep=' --> ')
    
    i += 1