import random

changed = 0
not_changed = 0

for x in range(100):
    winner = random.randint(1, 3)
    losers = [x for x in (1, 2, 3) if x != winner]
    choice = random.randint(1, 3)
    
    print(f'Game {x}')
    if choice not in losers:
        dropout = random.choice(losers)
    else:
        dropout = 6 - winner - choice
    
    print(f'Dropped: {dropout}')
    
    result = (winner == choice)
    
    if result:
        print(f'Not changed: win;\nchanged: lose')
        not_changed += 1
    else:
        print(f'Not changed: lose;\nchanged: win')
        changed += 1

print(f'Total wins:\nChanged - {changed}\nNot changed - {not_changed}')
    