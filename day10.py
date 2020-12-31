example = [
    '16',
    '10',
    '15',
    '5',
    '1',
    '11',
    '7',
    '19',
    '6',
    '12',
    '4',
]

example2 = [
    '28',
    '33',
    '18',
    '42',
    '31',
    '14',
    '46',
    '20',
    '48',
    '47',
    '24',
    '23',
    '49',
    '45',
    '19',
    '38',
    '39',
    '11',
    '1',
    '32',
    '25',
    '35',
    '8',
    '17',
    '7',
    '9',
    '4',
    '2',
    '34',
    '10',
    '3'
]

with open("day10-input.txt") as file:
    data = [int(d.strip()) for d in file.readlines()]

data.append(0)
data.sort()

example = [int(e) for e in example]
example.append(0)
example.append(max(example) + 3)
example.sort()

example2 = [int(e) for e in example2]
example2.append(0)
example2.append(max(example2) + 3)
example2.sort()

curr_jolts = 0
distribution = {1: 0, 3: 0}

for n in range(1, len(data)):
    diff = data[n] - curr_jolts
    # print(f'At adapter {example[n]}, current jolts = {curr_jolts} with a diff of {diff}')
    if diff <= 3:
        curr_jolts += diff
        distribution[diff] += 1

# add the last 3 jolts
curr_jolts += 3
distribution[3] += 1

# print(distribution)
print(f'Differences: {distribution[1] * distribution[3]}')

i = 0
last_jump = 0
chains = []
while i < len(data):
    if i + 1 >= len(data):
        chain = [data[x] for x in range(last_jump - 1, i + 1)]
        chains.append(chain)
        break

    if data[i + 1] - data[i] >= 3:
        chain = [data[x] for x in range(last_jump, i + 1)]
        if len(chain) > 1:
            chains.append(chain)
        last_jump = i + 1
    i += 1

print(chains)

ans = 1
for c in chains:
    if len(c) == 3:
        ans *= 2
    if len(c) == 4:
        ans *= 4
    if len(c) == 5:
        ans *= 7

print(ans)