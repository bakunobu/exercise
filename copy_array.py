a = [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]]


"""
Составьте фрагмент кода, создающий двумерный массив b[][], являющийся копией существующего двумерного массива a[][],
при условии что,
a. массив квадратный
"""
a = [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]]

b = []

for n in range(len(a)):
    b.append([])
    for m in range(len(a)):
        b[n].append(a[n][m])


print(b)

'''
b. массив прямоугольный
'''

a = [[1, 2, 3, 4],
     [5, 6, 7, 8],
     [9, 10, 11, 12]]

n = len(a)
m = len(a[0])

b = []
for i in range(n):
    b.append([])
    for j in range(m):
        b[i].append(a[i][j])

print(b)

'''
c. ряды произвольной длины
'''

a = [[1, 2, 3, 4],
     [5, 6, 7],
     [8, 9, 10, 11]]

b = []


n = len(a)

b = []
for i in range(n):
    b.append([])
    m = len(a[i])
    for j in range(m):
        b[i].append(a[i][j])

print(b)
