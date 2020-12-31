example = [
    '..##.......',
    '#...#...#..',
    '.#....#..#.',
    '..#.#...#.#',
    '.#...##..#.',
    '..#.##.....',
    '.#.#.#....#',
    '.#........#',
    '#.##...#...',
    '#...##....#',
    '.#..#...#.#'
]

with open('day3-input.txt') as file:
    data = file.readlines()
    data = [d.strip() for d in data]

rows, cols = (len(data), len(data[0]))
grid = []

def print_grid():
    for i in range(rows):
        print(grid[i])

for i in range(rows):
    col = []
    for j in range(cols):
        col.append('')
    grid.append(col)

r = 0
for line in data:
    c = 0
    for char in line:
        grid[r][c] = char
        c += 1
    r += 1

print_grid()

amount_down = 2
amount_right = 1

tree_count = 0

while amount_down < rows:
    if amount_right >= cols:
        amount_right = amount_right - cols
    print(f'({amount_down}, {amount_right}): {grid[amount_down][amount_right]}')
    
    if grid[amount_down][amount_right] == '#':
        tree_count += 1
    
    amount_down += 2
    amount_right += 1

print(f'Trees encountered: {tree_count}')

# right 1, down 1: 66
# right 3, down 1: 153
# right 5, down 1: 79
# right 7, down 1: 92
# right 1, down 2: 33

print(f'Total: {66 * 153 * 79 * 92 * 33}')