starting_numbers = '18,8,0,5,4,1,20'

turn = 1
previous = 20

# game = {}
seen = {}

# game = { turn_number: number }
# seen = { number: last_turn_seen }

for num in map(int, starting_numbers.split(',')):
    # game[turn] = num
    seen[num] = [turn]
    turn += 1

while turn <= 30000000:
    # previous = game[turn - 1]
    if len(seen[previous]) == 1:
        # game[turn] = 0
        num = 0
        seen[0].append(turn)
    else:
        num = (turn - 1) - seen[previous][-2]
        # game[turn] = num
        if num in seen:
            seen[num].append(turn)
        else:
            seen[num] = [turn]
    turn += 1
    previous = num
    
print(num)
# print(game[2020])