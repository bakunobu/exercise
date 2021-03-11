def generate_fib_seq(n:int) -> list:
    feb_seq = [1,]
    a, b = 1, 1
    while b < n:
        a, b = b, a + b
        feb_seq.append(b)
    return(feb_seq)


# a
print(sum(generate_fib_seq(1001)))

# b
while True:
    try:
        n = int(input('Введите число: '))
        if n > 0:
            break
        else:
            print('Используйте положительные числа!')
    except ValueError:
        print('Используйте только целые числа')
        
print(generate_fib_seq(n)[-1])