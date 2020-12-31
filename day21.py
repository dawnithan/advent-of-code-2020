import re
import collections

example = [
    'mxmxvkd kfcds sqjhc nhms (contains dairy, fish)',
    'trh fvjkl sbzzf mxmxvkd (contains dairy)',
    'sqjhc fvjkl (contains soy)',
    'sqjhc mxmxvkd sbzzf (contains fish)'
]

with open("day21-input.txt") as file:
    data = [d.strip() for d in file.readlines()]

foods = {}

ingredients = {}
ing_id = 0

allergens = {}
a_id = 0

for line in data:
    allergen = re.search(r'\(.*\)', line)
    ingredient_lst = [x.split(' ') for x in line.split(' (contains ')][0]
    allergen_str = allergen.group(0)[10:-1] 
    
    allergens[a_id] = allergen_str.split(', ')
    ingredients[ing_id] = ingredient_lst
    ing_id += 1
    a_id +=1 

for i in range(len(data)):
    curr_all = allergens[i]
    curr_ing = ingredients[i]

    for k in curr_all:
        if k not in foods.keys():
            foods[k] = set(curr_ing)

        foods[k] = set.intersection(foods[k], set(curr_ing))
        # print(foods)

# foods -> allergen : {potential_ingredients}
# print(foods)

def list_diff(list1, list2):
    out = [item for item in list1 if not item in list2]
    return out

allergen_check_lst = []
for i in foods.values():
    for j in i:
        allergen_check_lst.append(j)

ingredients_check_lst = []
for i in ingredients.values():
    for j in i:
        ingredients_check_lst.append(j)

difference = list_diff(ingredients_check_lst, allergen_check_lst)
print(len(difference))

sorted_rules = sorted(foods.items(), key=lambda x: len(x[1]))
print(sorted_rules)

# peanuts = txdmlzd
# wheat = mptbpz
# dairy = cxsvdm
# sesame = vlblq
# egg = glf
# nuts = xbnmzr
# soy = mtnh
# fish = rsbxb

dangerous = {
    'peanuts' : 'txdmlzd', 
    'wheat' : 'mptbpz', 
    'dairy' : 'cxsvdm', 
    'sesame' : 'vlblq', 
    'egg' : 'glf', 
    'nuts' : 'xbnmzr', 
    'soy' : 'mtnh', 
    'fish' : 'rsbxb'
}

answer = ''.join([dangerous[i] + ',' for i in sorted(dangerous)])
print(answer)