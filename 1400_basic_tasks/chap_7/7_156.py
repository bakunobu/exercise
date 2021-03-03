from main_funcs import get_input


# a 
def max_asc_seq(n:int) -> int:
    max_seq = 1
    cur_seq = 1
    prev_a = get_input('Введите число: ')
    for _ in range(1, n):
        a = get_input('Введите число: ')
        if a > prev_a:
            cur_seq += 1
            prev_a = a
        else:
            prev_a = a
            max_seq = max(max_seq, cur_seq)
            cur_seq = 1
    return(max_seq)


def max_des_seq(n:int) -> int:
    max_seq = 1
    cur_seq = 1
    prev_a = get_input('Введите число: ')
    for _ in range(1, n):
        a = get_input('Введите число: ')
        if a < prev_a:
            cur_seq += 1
            prev_a = a
        else:
            prev_a = a
            max_seq = max(max_seq, cur_seq)
            cur_seq = 1
    return(max_seq)


def max_seq(n):
    seq_1 = max_asc_seq(n)
    seq_2 = max_des_seq(n)
    return(max(seq_1, seq_2))


# b
def adj_max_seq(n:int) -> int:
    status = False
    max_seq = 1
    cur_seq = 1
    prev_a = get_input('Введите число: ')
    for _ in range(1, n):
        a = get_input('Введите число: ')
        if not status:
            if a > prev_a:
                status = 'u'

            else:
                status = 'd'

            cur_seq += 1
            print('Status initialized! Counter on {}.'.format(cur_seq))
                
        else:
            
            if status == 'u':
                if a > prev_a:
                    cur_seq += 1
                    prev_a = a
                    print('Status {}, counter on {}'.format(status,
                                                            cur_seq))
                    
                else:
                    prev_a = a
                    max_seq = max(max_seq, cur_seq)
                    cur_seq = 1
                    status = 'd'
                
            elif status == 'd':
                if a < prev_a:
                    cur_seq += 1
                    prev_a = a
                    print('Status {}, counter on {}'.format(status,
                                                            cur_seq))
                    
                else:
                    prev_a = a
                    max_seq = max(max_seq, cur_seq)
                    cur_seq = 1
                    status = 'u'
                     
    max_seq = max(max_seq, cur_seq)
  
    return(max_seq)


print(adj_max_seq(10))
