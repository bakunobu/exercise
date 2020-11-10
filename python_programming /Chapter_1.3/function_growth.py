""" Составьте программу functiongrowth.ру,
выводящую таблицу значений log2 n, n, n log_e n, n^2, n^3 и 2^n
для n = 2, 4, 8, 16, 32, 64, ... , 2048.
Для выравни­вания столбцов таблицы используйте табуляцию (символы \t).  """

import math

for x in range(1, 12):
    n = 2 ** x
    print(math.log2(n), end='\t')
    print(n, end='\t')
    print(n * math.log(n), end='\t')
    print(n ** 2, end='\t')
    print(n ** 3, end='\t')
    print(2 ** n, end='\n')