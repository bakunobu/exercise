import random


seq = [random.randint(1,10) for x in range(13)]
seq.append(0)

i = 0
while True:
    print('Вы ввели число:', end=' ')
    num = seq[i]
    i += 1
    print(num)
    if num == 0:
        break
    
    
