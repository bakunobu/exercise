# a
for x in range(20, 36):
    print(x)
    

# b
def print_squares(a:int, b:int=51) -> None:
    for i in range(a, b):
        print(i ** 2)


if __name__ == '__main__':
    a = int(input('Введите число: '))
    print_squares(a)
    

# c
def print_cubes(b:int, a:int=10) -> None:
    for x in range(a, b+1):
        print(x ** 3)


if __name__ == "__main__":
    a = int(input('Введите число: '))
    print_cubes(b)
        
        