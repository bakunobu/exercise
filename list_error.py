'''
Составьте программу, которая создает одномерный массив a, содержащий ровно 1000 целых чисел, а затем пытается получить доступ к элементу a[1000]
'''


a = [x for x in range(1, 1001)]
print(len(a))

try:
    print(a[1000])
except IndexError:
    print('Yop, it\'s an IndexError!')