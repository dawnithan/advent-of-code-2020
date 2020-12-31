with open("example.txt") as file:
    example = [e.strip() for e in file.readlines()]

with open("day16-input.txt") as file:
    data = [d.strip() for d in file.readlines()]

end_of_rules = data.index('your ticket:') - 1
start_of_nearby = data.index('nearby tickets:') + 1

rule_id = 0
rules = {}
rules_mapped = {}
possible_positions_for_rules = {}
errors = []

def verify_valid(values, rules):
    valid = True
    for v in values:
        invalid_count = 0
        for r in range(len(rules)):
            low_lowest = int(rules[r][0].split('-')[0])
            low_upper = int(rules[r][0].split('-')[1])
            up_lowest = int(rules[r][1].split('-')[0])
            up_upper = int(rules[r][1].split('-')[1])

            if not (low_lowest <= v <= low_upper or up_lowest <= v <= up_upper):
                invalid_count += 1
        # the value was invalid for every field
        if invalid_count == len(rules) and valid:
            errors.append(v)
            valid = False
    return valid

def find_rule_positions(values, rules):
    for v in values:
        for r in rules:
            low_lowest = int(rules[r][0].split('-')[0])
            low_upper = int(rules[r][0].split('-')[1])
            up_lowest = int(rules[r][1].split('-')[0])
            up_upper = int(rules[r][1].split('-')[1])
            
            if not (low_lowest <= v <= low_upper or up_lowest <= v <= up_upper):
                possible_positions_for_rules[r].remove(values.index(v))

# build the rules dictionary
for rule in range(0, end_of_rules):
    ranges = data[rule].split(' or ')
    lower_range = ranges[0].split(': ')[1]
    upper_range = ranges[1]
    
    name = ranges[0].split(': ')[0]
    rules[rule_id] = [lower_range, upper_range]
    rules_mapped[rule_id] = 0
    possible_positions_for_rules[rule_id] = set([i for i in range(end_of_rules)])
    rule_id += 1

# check each ticket
for ticket in range(start_of_nearby, len(data)):
    values = [int(x) for x in data[ticket].split(',')]
    
    # if a value doesn't satisfy *any* field, the ticket is invalid
    if verify_valid(values, rules):
        find_rule_positions(values, rules)

sorted_rules = sorted(possible_positions_for_rules.items(), key=lambda x: len(x[1]))

for s in range(len(sorted_rules)):
    num = [int(i) for i in sorted_rules[s][1]]
    rules_mapped[sorted_rules[s][0]] = num
    for rest in range(s + 1, len(sorted_rules)):
        if num[0] in sorted_rules[rest][1]:
            sorted_rules[rest][1].remove(num[0]) 

# print(rules_mapped)

my_ticket = [int(i) for i in data[data.index("your ticket:") + 1].split(',')]
ans = 1
for i in range(6):
    ans *= my_ticket[rules_mapped[i][0]]

print(f'Part 1: {sum(errors)}')
print(f'Part 2: {ans}')

# rules -> contains ranges
# rules_mapped -> contains references to columns