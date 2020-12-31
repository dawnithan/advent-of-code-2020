import timeit
start = timeit.default_timer()

example = [
    'L.LL.LL.LL',
    'LLLLLLL.LL',
    'L.L.L..L..',
    'LLLL.LL.LL',
    'L.LL.LL.LL',
    'L.LLLLL.LL',
    '..L.L.....',
    'LLLLLLLLLL',
    'L.LLLLLL.L',
    'L.LLLLL.LL'
]

with open("day11-input.txt") as file:
    data = [d.strip() for d in file.readlines()]

rows, cols = (len(data), len(data[0]))
grid = []

def print_grid(g):
    for i in range(rows):
        print(g[i])

def get_neighbours_adj(x, y, r, c):
    neighbours = []
    # [x-1y-1, x-1y, x-1y+1]
    # [xy-1,    xy,  xy+1]
    # [x+1y-1, x+1y, x+1y+1]

    if x - 1 >= 0 and y - 1 >= 0:
        neighbours.append((x-1, y-1))
    if x - 1 >= 0:
        neighbours.append((x-1, y))
    if x - 1 >= 0 and y + 1 < c:
        neighbours.append((x-1, y+1))
    if y - 1 >= 0:
        neighbours.append((x, y-1))
    if y + 1 < c:
        neighbours.append((x, y+1))
    if x + 1 < r and y - 1 >= 0:
        neighbours.append((x+1, y-1))
    if x + 1 < r:
        neighbours.append((x+1, y))
    if x + 1 < r and y + 1 < c:
        neighbours.append((x+1, y+1))

    return neighbours

def get_neighbours_los(x, y, r, c, g):
    results = []
    # beam out lines clockwise, stop once you hit '#' or 'L', return that coord
    i = x - 1
    j = y - 1
    while i >= 0 and j >= 0:
        if g[i][j] == ".":
            i -= 1
            j -= 1
        elif g[i][j] == '#' or g[i][j] == 'L':
            results.append((i, j))
            break
    i = x - 1
    j = y
    while i >= 0:
        if g[i][j] == ".":
            i -= 1
        elif g[i][j] == '#' or g[i][j] == 'L':
            results.append((i, j))
            break
    i = x - 1
    j = y + 1
    while i >= 0 and j < c:
        if g[i][j] == ".":
            i -= 1
            j += 1
        elif g[i][j] == '#' or g[i][j] == 'L':
            results.append((i, j))
            break
    i = x
    j = y - 1
    while j >= 0:
        if g[i][j] == ".":
            j -= 1
        elif g[i][j] == '#' or g[i][j] == 'L':
            results.append((i, j))
            break
    i = x
    j = y + 1
    while j < c:
        if g[i][j] == ".":
            j += 1
        elif g[i][j] == '#' or g[i][j] == 'L':
            results.append((i, j))
            break
    i = x + 1
    j = y - 1
    while i < r and j >= 0:
        if g[i][j] == ".":
            i += 1
            j -= 1
        elif g[i][j] == '#' or g[i][j] == 'L':
            results.append((i, j))
            break
    i = x + 1
    j = y
    while i < r:
        if g[i][j] == ".":
            i += 1
        elif g[i][j] == '#' or g[i][j] == 'L':
            results.append((i, j))
            break
    i = x + 1
    j = y + 1
    while i < r and j < c:
        if g[i][j] == ".":
            i += 1
            j += 1
        elif g[i][j] == '#' or g[i][j] == 'L':
            results.append((i, j))
            break
    return results

# initial grid
for i in range(rows):
    col = []
    for j in range(cols):
        col.append(data[i][j])
    grid.append(col)

def make_new_grid(g):
    for _ in range(rows):
        row = ['' for j in range(cols)]
        g.append(row)

def compare_grids(a, b):
    for i in range(rows):
        for j in range(cols):
            if a[i][j] != b[i][j]:
                return False
    return True

def count_occupied(g):
    count = 0
    for i in range(rows):
        for j in range(cols):
            if g[i][j] == '#':
                count += 1
    return count

# print_grid(grid)
# print('------------')

def generate(grid_data):
    flag = False
    updated_grid = []
    # makes a new blank grid
    make_new_grid(updated_grid)

    for x in range(rows):
        for y in range(cols):
            curr_pos_state = grid_data[x][y]
            if curr_pos_state == 'L' or curr_pos_state == '#':
                adjacents_occupied = 0
                neighbours = get_neighbours_los(x, y, rows, cols, grid_data)
                for n in neighbours:
                    seat = grid_data[n[0]][n[1]]
                    if seat == '#':
                        adjacents_occupied += 1
                if curr_pos_state == 'L' and adjacents_occupied == 0:
                    updated_grid[x][y] = '#'
                    flag = True
                elif curr_pos_state == '#' and adjacents_occupied >= 5:
                    updated_grid[x][y] = 'L'
                    flag = True
                else:
                    updated_grid[x][y] = grid_data[x][y]
            else:
                updated_grid[x][y] = '.'
    # print_grid(updated_grid)
    # print('------------')
    return updated_grid, flag

ug, f = generate(data)

while f:
    ug, f = generate(ug)
    
print(count_occupied(ug))

stop = timeit.default_timer()
print('Time: ', stop - start)  