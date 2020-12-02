from 4_20 import find_rectangle

def find_up_right(dot_a:tuple, a:float, b:float) -> tuple:
    return(tuple(dot_a[0]+b, dot_a[1]+a))


u_r_a = find_up_right(l_l_a, a_1, b_1)
u_r_b = find_up_right(l_l_b, a_2, b_2)


print(find_rectangle(l_l_a, l_l_b,
                     u_r_a, u_r_b))

