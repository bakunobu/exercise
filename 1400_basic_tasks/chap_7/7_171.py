from main_funcs import get_input


# a
def two_big_nums(n:int) -> tuple:
    f_g_n = False
    s_g_n = False
    
    for i in range(n):
        x = get_input('Введите число: ', False)
        if not f_g_n:
            f_g_n = x
        if not s_g_n:
            s_g_n = x
        
        if x >= f_g_n:
            s_g_n = f_g_n
            f_g_n = x
        elif x > s_g_n:
            s_g_n = x
    
    return(f_g_n, s_g_n)


# b
def two_small_nums(n:int) -> tuple:
    f_l_n = False
    s_l_n = False
    
    for i in range(n):
        x = get_input('Введите число: ', False)
        if not f_l_n:
            f_l_n = x
        elif not s_l_n:
            s_l_n = x
        
        else:
            if x <= f_l_n:
                s_l_n = f_l_n
                f_l_n = x
            elif x < s_l_n:
                s_l_n = x
    
    return(f_l_n, s_l_n)