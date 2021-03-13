# a
def eight_printer() -> None:
    line = [8 for i in range(3)]
    for j in range(5):
        print(* line, sep=' ')
        
        
# eight_printer()

# b
def print_series() -> None:
    for i in range(1, 8):
        line = [i for j in range(5)]
        print(* line, sep=' ')
        
        
# print_series()

# c
def print_ten_series() -> None:
    for i in range(1, 9):
        line = [i * 10 for j in range(4)]
        print(* line, sep=' ')
        
# d
def print_ten_series() -> None:
    for i in range(1, 9):
        line = [(i * 10) + 2 for j in range(4)]
        print(* line, sep=' ')
        

# e
def print_to_twenty() -> None:
    line = [i for i in range(2, 21)]
    for j in range(5):
        print(* line, sep=' ')
        
        
# f
def print_reverse() -> None:
    line =[i for i in range(15, 2, -1)]
    for j in range(5):
        print(* line, sep=' ')
        
# print_reverse()


# g
def print_zeros() -> None:
    for i in range(5):
        line = [0 for j in range(6-i)]
        print(* line, sep=' ')
        
        
# h
def print_rev_seq() -> None:
    for i in range(8):
        line = [j for j in range(8, i, -1)]
        print(* line, sep=' ')
        
        
# print_rev_seq()

# i
def print_seq() -> None:
    for i in range(8):
        line = [j for j in range(i+2, 11)]
        print(* line, sep=' ')
        
# print_seq()


# k
def print_stairs() -> None:
    for i in range(1, 10):
        line = [j for j in range(2, i+2)]
        print(* line, sep=' ')
        
# print_stairs()


# l
def print_three_six() -> None:
    for i in range(3, 7):
        line = [i for j in range(i)]
        print(* line, sep=' ')
        
# print_three_six()


# m
def print_twenties() -> None:
    for i in range(1, 6):
        line = [i + 20 for j in range(i)]
        print(* line, sep=' ')
        
        
# n
def print_eights() -> None:
    for i in range(5):
        line = [i + 1 for j in range(8-i)]
        print(* line, sep=' ')
        
# print_eights()


# o
def print_decs() -> None:
    for i in range(1, 6):
        line = [i * 10 for j in range(i)]
        print(* line, sep=' ')
        
# print_decs()


# p
def print_five_to_nine() -> None:
    for i in range(5):
        line = [5 + i for j in range(5-i)]
        print(* line, sep=' ')
        
        
# print_five_to_nine()


# q
def print_x_five() -> None:
    for i in range(1, 6):
        line = [5 * i for j in range(6-i)]
        print(* line, sep=' ')
        
# print_x_five()


# r
def print_hund() -> None:
    for i in range(7):
        line = [100 + i * 10 + j for j in range(1, 6)]
        print(* line, sep=' ')
        
# print_hund()


# s
def print_rev_dec() -> None:
    for i in range(50, 10, -10):
        line = [i + j for j in range(1, 9)]
        print(* line, sep=' ')
        
print_rev_dec()