import re

example = [
    'ecl:gry pid:860033327 eyr:2020 hcl:#fffffd\n',
    'byr:1937 iyr:2017 cid:147 hgt:183cm\n',
    '\n',
    'iyr:2013 ecl:amb cid:350 eyr:2023 pid:028048884\n',
    'hcl:#cfa07d byr:1929\n',
    '\n',
    'hcl:#ae17e1 iyr:2013\n',
    'eyr:2024\n',
    'ecl:brn pid:760753108 byr:1931\n',
    'hgt:179cm\n',
    '\n',
    'hcl:#cfa07d eyr:2025 pid:166559648\n',
    'iyr:2011 ecl:brn hgt:59in\n',
    '\n'
]

# byr, iyr, eyr, hgt, hcl, ecl, pid, cid <- (optional if all previous exist)

example = [e.strip() for e in example]

with open("day4-input.txt") as file:
    data = file.readlines()
    data = [d.strip() for d in data]

passports = {}
pp_id = 0
created = False

valid_col = ['amb','blu','brn','gry','grn','hzl','oth']
valid_char = ['a','b','c','d','e','f']
valid_num = ['0','1','2','3','4','5','6','7','8','9']

def set_dict(d):
    f = ['byr','iyr','eyr','hgt','hcl','ecl','pid','cid']
    for i in f:
        d[i] = 0

def check_height(v):
    which = v[-2:]
    num = v[:-2]
    print(f'Which: {which}, Num: {num}')
    if which == 'cm' and int(num) >= 150 and int(num) <= 193:
        return True
    elif which == 'in' and int(num) >= 59 and int(num) <= 76:
        return True
    else:
        return False

def check_hex(v):
    if v[0] != '#' or len(v) != 7:
        return False
    for i in range(1, len(v)):
        if v[i] not in valid_char and v[i] not in valid_num:
            return False
    return True

# test = '#12667a'
# print(check_hex(test))

# store each passport into a dictionary as a one-line string
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
        passports[pp_id] = info
        pp_id += 1

num_valid_pp = 0

for p in passports.values():
    # each passport is a single string containing info, delimited by spaces
    lst = p.split(" ")
    fields = {}
    set_dict(fields)
    
    valid = True

    for i in lst:
        x = i.split(":")
        if x[0] != '':
            field = x[0]
            val = x[1]

            # validate the passport
            if field == 'byr' and (int(val) < 1920 or int(val) > 2002):
                valid = False
            if field == 'iyr' and (int(val) < 2010 or int(val) > 2020):
                valid = False
            if field == 'eyr' and (int(val) < 2020 or int(val) > 2030):
                valid = False
            if field == 'hgt' and not check_height(val):
                valid = False
            if field == 'hcl' and not bool(re.match(r"#[0-9a-f]{6}", val)):
                valid = False
            if field == 'ecl' and val not in valid_col:
                valid = False
            if field == 'pid' and not bool(re.match(r"^[0-9]{9}$", val)):
                valid = False
            
            # add field to dict
            fields[field] += 1
    
    if valid and fields['byr'] == 1 and fields['iyr'] == 1 and fields['eyr'] == 1 and fields['hgt'] == 1 and fields['hcl'] == 1 and fields['ecl'] == 1 and fields['pid'] == 1:
        num_valid_pp += 1

print(f'No. of valid passports: {num_valid_pp}')
