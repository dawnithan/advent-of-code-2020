with open("rough work\\example19.txt") as file:
    example = [d.strip() for d in file.readlines()]

rules = {}
messages = []

start_of_messages = 0

for line in example:
    if len(line) <= 0:
        start_of_messages = example.index(line)
        break
    
    rule_id = line[0:line.index(':')]
    rule_content = line.split(': ')[1]
    
    if rule_content.startswith('"'):
        content = "".join([char for char in rule_content if char != '"'])
    else:
        content = rule_content

    rules[rule_id] = content

for m in range(start_of_messages + 1, len(example)):
    messages.append(example[m])

print(rules)
print(messages)

def check(r):
    r_content = rules[r]

    if r_content.isalpha():
        print(r_content)
        return r_content
    else:
        if '|' in r_content:
            options = r_content.split(' | ')
            option_one = options[0].split(' ')
            option_two = options[1].split(' ')
            check(option_one[0])
            check(option_one[1])
            check(option_two[0])
            check(option_two[1])
        else:
            options = r_content.split(' ')
            for o in options:
                check(o)

check('0')