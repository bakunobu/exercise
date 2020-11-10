a = [[99, 98, 92, 94, 99, 90, 76, 92, 97, 89],
     [85, 57, 77, 32, 34, 46, 59, 66, 71, 29],
     [98, 78, 76, 11, 22, 54, 88, 89, 24, 38]]


trans_a = []

for i in range(len(a[0])):
    row = []
    for j in range(len(a)):
        row.append(a[j][i])
    trans_a.append(row) 

print(trans_a)
