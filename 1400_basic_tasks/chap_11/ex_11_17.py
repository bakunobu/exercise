fib_seq = [1, 1,]

for i in range(8):
    fib_seq.append(fib_seq[-2]+fib_seq[-1])

print(fib_seq)