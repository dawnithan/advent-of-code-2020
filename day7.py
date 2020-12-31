import timeit
start = timeit.default_timer()

example = [
    'light red bags contain 1 bright white bag, 2 muted yellow bags.',
    'dark orange bags contain 3 bright white bags, 4 muted yellow bags.',
    'bright white bags contain 1 shiny gold bag.',
    'muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.',
    'shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.',
    'dark olive bags contain 3 faded blue bags, 4 dotted black bags.',
    'vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.',
    'faded blue bags contain no other bags.',
    'dotted black bags contain no other bags.'
]

example2 = [
    'shiny gold bags contain 2 dark red bags.',
    'dark red bags contain 2 dark orange bags.',
    'dark orange bags contain 2 dark yellow bags.',
    'dark yellow bags contain 2 dark green bags.',
    'dark green bags contain 2 dark blue bags.',
    'dark blue bags contain 2 dark violet bags.',
    'dark violet bags contain no other bags.'
]

with open("day7-input.txt") as file:
    data = [d.strip() for d in file.readlines()]

bag_types = {}
bag_types_invert = {}

for line in data:
    l = line.split(' contain ')
    bag = l[0].split(' bags')[0]
    contains = l[1].split(', ')
    contains_formatted = []
    
    for i in contains:
        b = i.split(' bag')[0]
        if b == 'no other':
            amount = 0
            color = ''
        else:
            amount = b[0]
            color = b[2:]
        contains_formatted.append((color, amount))
    bag_types[bag] = contains_formatted

bags = set()
count = 0

def check_part1(bag):
    x = bag_types_invert[bag]
    for i in x:
        bags.add(i[0])
        if i[0] != '':
            check_part1(i[0])

# at this point the data is stored as so: bag -> contains
# need to reverse the order such that: bag -> is contained in
for i in bag_types.keys():
    bag_types_invert[i] = []

for key in bag_types:
    for val in bag_types[key]:
        # val[0] = color, val[1] = qty
        if val[0] != '':
            bag_types_invert[val[0]].append((key, val[1]))

check_part1('shiny gold')
print(f'Part 1: {len(bags)}')

def check_part2(bag):
    global count
    x = bag_types[bag]
    for i in x:
        # print(f'Color: {i[0]}, Quantity: {i[1]}')
        count += int(i[1])
        if i[0] != '':
            for _ in range(int(i[1])):
                check_part2(i[0])

check_part2('shiny gold')
print(f'Part 2: {count}')

stop = timeit.default_timer()
print('Time: ', stop - start)  