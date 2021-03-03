from main_funcs import get_input

# a 
def find_nearest_n(seq:list, n:float) -> float:
    diff = False
    nn = False
    for x in seq():
        n_diff = abs(x - n)
        if not diff:
            diff = n_diff
            nn = x
        if n_diff < diff:
            diff = n_diff
            nn = x
    return(nn)

# b
def adj_nn(seq:list, n:float) -> float:
    prev_diff = abs(seq[0] - n)
    diff = abs(seq[1] - n)
    i = 1
    
    while prev_diff > diff and i < len(seq) - 1:
        i += 1
        print(f'Loop {i}, prev_diff: {prev_diff}, cur_diff: {diff}')
        prev_diff = diff
        diff = abs(seq[i] - n)
    
    if prev_diff < diff:
        i -= 1
        
    return(seq[i])
    

def main(seq:list) -> float:
    n = get_input('Введите число: ')
    print(adj_nn(seq, n)) 


