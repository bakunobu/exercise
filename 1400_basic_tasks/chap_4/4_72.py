def find_all_points(x_1:float,y_1:float, len_x:float, len_y:float) -> tuple:
    """
    (x_4, y_4)-------(x_3, y_3)
        |                 |
        |                 |
    (x_1, y_1)-------(x_2, y_2)
    """
    
    x_2 = x_1 + len_x
    y_2 = y_1
    x_3 = x_2
    y_3 = y_2 + len_y
    x_4 = x_1
    y_4 = y_3
    return(x_1, x_2, x_3, x_4,
           y_1, y_2, y_3, y_4)


# a
def is_in_rectangle(x_1_a, y_1_a, len_x_a, len_y_a,
                    x_1_b, y_1_b, len_x_b, len_y_b) -> bool:
    fig_a = find_all_points(x_1_a, y_1_a, len_x_a, len_y_a)
    fig_b = find_all_points(x_1_b, y_1_b, len_x_b, len_y_b)
    cond = fig_a[0] < fig_b[0] and fig_a[4] < fig_b[4]
    cond = cond and (fig_a[1] > fig_b[1] and fig_a[5] < fig_b[5])
    cond = cond and (fig_a[2] > fig_b[2] and fig_a[6] > fig_b[6])
    cond = cond and (fig_a[3] < fig_b[3] and fig_a[7] > fig_b[7])
    return(cond)

# b
def is_in_one_of_rect(x_1_a, y_1_a, len_x_a, len_y_a,
                      x_1_b, y_1_b, len_x_b, len_y_b) -> bool:
    cond1 = is_in_rectangle(x_1_a, y_1_a, len_x_a, len_y_a,
                            x_1_b, y_1_b, len_x_b, len_y_b)
    cond2 = is_in_rectangle(x_1_b, y_1_b, len_x_b, len_y_b,
                            x_1_a, y_1_a, len_x_a, len_y_a)
    return(cond1 or cond2)

# c

def cross_lines(x_1_a:float, y_1_a:float,
                x_2_a:float, y_2_a:float,
                x_1_b:float, y_1_b:float,
                x_2_b:float, y_2_b:float) -> bool:
    if x_1_a == x_2_a:
        cond1 = min(y_1_a, y_2_a) < y_1_b < max(y_1_a, y_2_a)
        cond2 = min(x_1_b, x_2_b) < x_1_a < max(x_1_b, x_2_b)
    else:
        cond1 = min(y_1_b, y_2_b) < y_1_a < max(y_1_b, y_2_b)
        cond2 = min(x_1_a, x_2_a) < x_1_b < max(x_1_a, x_2_a)
    return(cond1 and cond2)
    
    
def is_crossing(x_1_a, y_1_a, len_x_a, len_y_a,
                x_1_b, y_1_b, len_x_b, len_y_b) -> bool:
    fig_a = find_all_points(x_1_a, y_1_a, len_x_a, len_y_a)
    fig_b = find_all_points(x_1_b, y_1_b, len_x_b, len_y_b)
    points_a = [(x, y) for x, y in zip(fig_a[:4], fig_a[4:])]
    points_b = [(x, y) for x, y in zip(fig_b[:4], fig_b[4:])]
    points_b = points_b[1:] + points_b[0]
    for i in range(3):
        if cross_lines(points_a[i][0], points_a[i][1],
                       points_a[i+1][0], points_a[i+i][1],
                       points_b[i][0], points_b[i][1],
                       points_b[i+1][0], points_b[i+1][1]):
            return(True)
    return(False)

    
        