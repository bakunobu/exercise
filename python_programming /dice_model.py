import random

probabilities = [0 for _ in range(13)]

for i in range(1, 7):
    for j in range(1, 7):
        probabilities[i+j] += 1
        
for k in range(2, 13):
    probabilities[k] /= 36
    
print(probabilities)

def experiment(n):
    results = [random.randint(1, 6) + random.randint(1, 6) for _ in range(n)]
    prob_results = {result: results.count(result) /n for result in list(set(results))}
    return(prob_results)

a = experiment(1000000)

print(* a.items())