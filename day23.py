from collections import deque

puzzle = '398254716'

ex = [int(i) for i in puzzle]

# d = deque(ex + list(range(10, 1000001)))
d = deque(ex)

current = 0
for move in range(100):
    # print(f'{move + 1})')
    # print(f'Current: {d[current]}')

    curr_label = d[current]
    next_three = []
    
    for _ in range(3):
        offset = current + 1
        if offset >= len(d): offset = 0
        next_three.append(d[offset])
        d.remove(d[offset])

    # print(f'Next three: {next_three}. Remaining: {list(d)}')

    destination_cup = curr_label - 1

    while True:
        if destination_cup in d:
            break
        else:
            if (destination_cup - 1) < 1:
                destination_cup = 9
            else:
                destination_cup -= 1
            
    # print(f'Destination: {destination_cup}')

    ind = d.index(destination_cup)

    for i in range(3):
        offset = i + 1
        if offset > 9: offset = 0
        d.insert(ind + offset, next_three[i])
    
    check_diff = current - d.index(curr_label) 
    if check_diff < 0:
        d.rotate(check_diff)

    # print(f'Result: {list(d)}\n')

    current += 1
    if current >= len(d):
        current = 0

print(d)
# 45798623

# index_of_one = d.index(1)
# cup_one = d[index_of_one + 1]
# cup_two = d[index_of_one + 2]

# print(cup_one * cup_two)