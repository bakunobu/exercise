def fib_seq(n:int) -> list:
    a = 1
    b = 1
    fibbies = [a, b]
    for k in range(n-2):
        a, b = b, a+b
        fibbies.append(b)
    return(fibbies)


my_list = fib_seq(10)
for el in my_list[2:]:
    print(el, end=', ')