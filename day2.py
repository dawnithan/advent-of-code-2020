example = [
    '1-3 a: abcde',
    '1-3 b: cdefg',
    '2-9 c: ccccccccc'
]

with open('day2-input.txt') as file:
    data = file.readlines()
    data = [d.strip() for d in data]

def set_dict(d):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    for i in alphabet:
        d[i] = 0

p1_valid_pwds = 0
p2_valid_pwds = 0

for entry in data:
    parts = entry.split(' ')
    
    lower = int(parts[0].split('-')[0])
    upper = int(parts[0].split('-')[1])
    letter = parts[1][0]
    password = parts[2]
    
    check = {}
    set_dict(check)

    for char in password:
        check[char] += 1
    
    if check[letter] >= lower and check[letter] <= upper:
        p1_valid_pwds += 1

    if password[lower-1] == letter and password[upper-1] != letter:
        p2_valid_pwds += 1
    elif password[lower-1] != letter and password[upper-1] == letter:
        p2_valid_pwds += 1
    
    # or just this:
    # if (password[lower-1] == letter) != (password[upper-1] == letter)

print(f'Part 1 valid passwords: {p1_valid_pwds}\nPart 2 valid passwords: {p2_valid_pwds}')