def fib_seq(n:int) -> list:
    a = 1
    b = 1
    fibbies = [a, b]
    for k in range(n-2):
        a, b = b, a+b
        fibbies.append(b)
    return(fibbies)


# a
print(fib_seq(5)[-1])

# b
print(* fib_seq(10))
