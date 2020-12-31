example = [
    '35',
    '20',
    '15',
    '25',
    '47',
    '40',
    '62',
    '55',
    '65',
    '95',
    '102',
    '117',
    '150',
    '182',
    '127',
    '219',
    '299',
    '277',
    '309',
    '576'
]

with open("day9-input.txt") as file:
    data = [int(d.strip()) for d in file.readlines()]

example = [int(d) for d in example]

preamble = 25

def check(num, prev):
    for i in prev:
        for j in prev:
            if i != j and i + j == num:
                return True
    return False

invalid_num = 0

# Part 1
for n in range(preamble, len(data)):
    num = data[n]
    prev = []

    for i in range(preamble):
        prev.append(data[(n - i) - 1])

    # print(f'At {num}, previous {preamble} = {prev}')

    if not check(num, prev):
        invalid_num = num
        print(f'Invalid number: {invalid_num}')

index = 0
found = False

# Part 2
for n in range(len(data)):
    total = 0
    contiguous = []

    # start at {index}, add each num and check if > or = to invalid_num. 
    # if >, then scrap the list and increment index. 
    # if =, then return the list and find the max/min. 

    if not found:
        for i in range(index, len(data)):
            val = data[i]

            contiguous.append(val)
            total += val
            
            if total == invalid_num:
                print(contiguous)
                print(f'{min(contiguous)} + {max(contiguous)} = {min(contiguous) + max(contiguous)}')
                found = True
            elif total > invalid_num:
                index += 1
                break

