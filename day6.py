example = [
    'abc\n',
    '\n',
    'a\n',
    'b\n',
    'c\n',
    '\n',
    'ab\n',
    'ac\n',
    '\n',
    'a\n',
    'a\n',
    'a\n',
    'a\n',
    '\n',
    'b\n',
    '\n'
]

def set_dict(d):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    for i in alphabet:
        d[i] = 0

example = [e.strip() for e in example]

with open("day6-input.txt") as file:
    data = [d.strip() for d in file.readlines()]

groups = {}
group_id = 0
created = False

count_sum = 0

# collect each group into a dict
for line in data:
    if len(line) > 0:
        if created:
            info += line + ' '
        else:
            info = ''
            info += line + ' '
            created = True
    else:
        created = False
        groups[group_id] = info
        group_id += 1

# Part 1 (remove ' ' from line 40/43 to see)
# for group in groups.values():
#     questions = {}
#     count = 0
#     set_dict(questions)
#     for i in group:
#         if questions[i] < 1:
#             questions[i] += 1
#     for j in questions.values():
#         if j > 0:
#             count += 1
#     count_sum += count
#     # print(f'Count: {count}')

# Part 2
for group in groups.values():
    responses = group.split(' ')
    
    questions = {}
    set_dict(questions)

    num_people_in_group = len(responses) - 1
    num_questions_all = 0
    # print(f'{responses}, {num_people_in_group}')
    for response in responses:
        for char in response:
            if char != '':
                questions[char] += 1

    for i in questions.values():
        if i == num_people_in_group:
            num_questions_all += 1

    count_sum += num_questions_all
    print(f'Num people: {num_people_in_group}, questions all answered: {num_questions_all}')

print(count_sum)