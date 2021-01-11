def find_seq(n:int) -> list:
    my_seq = [1,]
    for k in range(1, n+1):
        el = k * my_seq[k-1] + 1 / k
        my_seq.append(el)
    return(my_seq)