def fiab_seq(n:int) -> bool:
    seq = [1, 1,]
    a, b = 1, 1
    while len(seq) <= n-1:
        a, b = b, a + b
        seq.append(b)
    
    return(sum(seq) % 2 == 0)


for x in range(20):
    print(fiab_seq(x))

