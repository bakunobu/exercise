a = [[1, 2, 3, 4],
     [5, 6, 7, 8],
     [9, 10, 11, 12],
     [13, 14, 15, 16]]

a = [[a[j][i] for j in range(len(a))] for i in range(len(a))]

print(a)
