from datetime import datetime
start = datetime.now()

pos_e = [e ** 5 for e in range(150, 5, -1)]

pos_d = [d ** 5 for d in range(149, 4, -1)]

pos_c = [c ** 5 for c in range(148, 3, -1)]

pos_b = [b ** 5 for b in range(147, 2, -1)]

pos_a = [a ** 5 for a in range(146, 1, -1)]


results = []
while True:
    for d in pos_d:
        if len(results) != 0:
            break
        for c in pos_c:
            if len(results) != 0:
                break
            for b in pos_b:
                if len(results) != 0:
                    break
                for a in pos_a:
                    if a + b + c + d in pos_e:
                        results.append(int(((a + b + c + d) ** 0.2)))
                        break
                        
                    


delta = start - datetime.now()
print(results[0])
print(f'Duration {delta}')
