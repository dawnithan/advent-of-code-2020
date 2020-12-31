import math

example = [
    'F10',
    'N3',
    'F7',
    'R90',
    'F11'
]

with open("day12-input.txt") as file:
    data = [d.strip() for d in file.readlines()]

# heading = {'east': 0, 'west': 0, 'north': 0, 'south': 0}
x = 0
y = 0

waypoint_x = 10
waypoint_y = 1

directions = ['E', 'S', 'W', 'N']
curr_direction = 0

# def move(towards, units, heading):
#     away = ''
#     if towards == 'south': away = 'north'
#     if towards == 'north': away = 'south'
#     if towards == 'west': away = 'east'
#     if towards == 'east': away = 'west'
#     if heading[away] - units >= 0:
#         heading[away] -= units
#     elif heading[away] - units < 0:
#         units -= heading[away]
#         heading[away] = 0
#         heading[towards] += abs(units)

def move(dir, units):
    global x, y
    if dir == 'N':
        y += units
    if dir == 'S':
        y -= units
    if dir == 'E':
        x += units
    if dir == 'W':
        x -= units

def move_waypoint(dir, units):
    global waypoint_x, waypoint_y
    if dir == 'N':
        waypoint_y += units
    if dir == 'S':
        waypoint_y -= units
    if dir == 'E':
        waypoint_x += units
    if dir == 'W':
        waypoint_x -= units
    
def rotate_waypoint(dir, units):
    global waypoint_x, waypoint_y
    new_x = 0 
    new_y = 0

    if dir == 'R':
        if units == 90:
            new_x = waypoint_y
            new_y = -waypoint_x 
        if units == 180:
            new_x = -waypoint_x
            new_y = -waypoint_y
        if units == 270:
            new_x = -waypoint_y
            new_y = waypoint_x
    
    if dir == 'L':
        if units == 90:
            new_x = -waypoint_y
            new_y = waypoint_x
        if units == 180:
            new_x = -waypoint_x
            new_y = -waypoint_y
        if units == 270:
            new_x = waypoint_y
            new_y = -waypoint_x
        
    waypoint_x = new_x
    waypoint_y = new_y

def move_to_waypoint(units):
    global waypoint_x, waypoint_y, x, y
    x = x + (units * waypoint_x)
    y = y + (units * waypoint_y)

for instruction in data:
    char = instruction[0]
    units = int(instruction[1:])
    print(char, units)

    if char == 'F':
        move_to_waypoint(units)
    if char == 'R' or char == 'L':
        rotate_waypoint(char, units)
        # curr_direction = (curr_direction + int(units / 90)) % len(directions)
        # curr_direction = (curr_direction - int(units / 90)) % len(directions)
    else:
        move_waypoint(char, units)

    print(x, y)

# distance = abs(heading['east'] - heading['west']) + abs(heading['north'] - heading['south'])
distance = abs(x) + abs(y)
print(f'Distance: {distance}')