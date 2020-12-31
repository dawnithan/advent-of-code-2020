import itertools
import collections

example = [
    'mask = XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X',
    'mem[8] = 11',
    'mem[7] = 101',
    'mem[8] = 0'
]

example2 = [
    'mask = 000000000000000000000000000000X1001X',
    'mem[42] = 100',
    'mask = 00000000000000000000000000000000X0XX',
    'mem[26] = 1'
]

with open("day14-input.txt") as file:
    data = [d.strip() for d in file.readlines()]

memory = collections.defaultdict(int)
curr_mask = ''

def pass_value_through_mask_part1(value, mask):
    bin_val = ('{:036b}'.format(int(value)))
    index = 0
    result = ['0' for i in range(36)]

    while index < 36:
        if mask[index] == 'X':                                result[index] = bin_val[index]
        elif bin_val[index] == '0' and mask[index] == '0':    result[index] = '0'
        elif bin_val[index] == '0' and mask[index] == '1':    result[index] = '1'
        elif bin_val[index] == '1' and mask[index] == '0':    result[index] = '0'
        elif bin_val[index] == '1' and mask[index] == '1':    result[index] = '1'
        index += 1

    result = ''.join(result)
    dec_val = int(result, 2)

    return dec_val

def pass_value_through_mask_part2(value, mask):
    bin_val = ('{:036b}'.format(int(value)))
    index = 0
    result = ['0' for i in range(36)]

    while index < 36:
        if mask[index] == 'X':      result[index] = 'X'
        elif mask[index] == '0':    result[index] = bin_val[index]
        elif mask[index] == '1':    result[index] = '1'
        index += 1

    result = ''.join(result)
    return result

def pass_address_through_mask(address, mask):
    result = pass_value_through_mask_part2(address, mask)
    addresses = []

    num_floating = len([x for x in result if x == 'X'])
    bin_combos = list(itertools.product([0, 1], repeat=num_floating))

    curr_combo = 0
    for _ in range(pow(2, num_floating)):
        result_lst = [r for r in result]
        x_index = 0
        for j in range(len(result)):
            if result_lst[j] == 'X':
                result_lst[j] = str(bin_combos[curr_combo][x_index])
                x_index += 1
        curr_combo += 1
        result_lst = ''.join(result_lst)
        addresses.append(int(result_lst, 2))
    return addresses

for line in data:
    if line.startswith('mask'):
        curr_mask = line.split(' = ')[1]
    if line.startswith('mem'):
        address = int(line[line.index('[')+1:line.index(']')])
        value = line.split(' = ')[1]

        addresses = pass_address_through_mask(address, curr_mask)
        # v = pass_value_through_mask_part1(value, curr_mask)
        for addr in addresses:
            memory[addr] = int(value)

print(sum(memory.values()))