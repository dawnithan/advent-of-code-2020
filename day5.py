import math

example = [
    'FBFBBFFRLR',
    'BFFFBBFRRR',
    'FFFBBBFRRR',
    'BBFFBBFRLL'
]

with open("day5-input.txt") as file:
    data = [d.strip() for d in file.readlines()]

highest = 0
ids = []

for line in data:
    lower = 0
    upper = 127
    lower_column = 0
    upper_column = 7
    # print(f'Rows {lower} through {upper}')
    for char in line:
        if char == 'F':
            upper = math.floor((lower + upper) / 2)
        if char == 'B':
            lower = math.ceil((lower + upper) / 2)
        
        # if char == 'F' or char == 'B':
        #     print(f'{char}: Rows {lower} through {upper}')

        if char == 'L':
            upper_column = math.floor((lower_column + upper_column) / 2)
        if char == 'R':
            lower_column = math.ceil((lower_column + upper_column) / 2)

        # if char == 'R' or char == 'L':
        #     print(f'{char}: Columns {lower_column} through {upper_column}')

    seat_id = lower * 8 + lower_column
    print(f'Seat ID = {lower} * 8 + {lower_column} = {seat_id}')

    if seat_id > highest:
        highest = seat_id

    ids.append(seat_id)

print(f'Highest seat ID: {highest}')

ids.sort()
# print(ids)

def find_missing(lst): 
    return [x for x in range(lst[0], lst[-1]+1) if x not in lst] 

print(find_missing(ids))