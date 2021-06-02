import os, sys, re


def check_all_cubes(grid):
    active_adjacent_grid = list()
    for j in range(0, len(grid)):
        active_adjacent_grid.append(list())
        for line in grid[j]:
            active_adjacent_grid[j].append(list(line))

    for level in range(1, len(grid)-1):
        for row in range(1, len(grid[level])-1):
            for col in range(1, len(grid[level][row])-1):
                active_adjacent_grid[level][row][col] = active_adjacent_cubes(col, row, level, grid)

    return active_adjacent_grid


def active_adjacent_cubes(x, y, z, grid):
    level_below = grid[z-1][y-1][x-1:x+2] + grid[z-1][y][x-1:x+2] + grid[z-1][y+1][x-1:x+2]
    same_level = grid[z][y-1][x-1:x+2] + grid[z][y][x-1] + grid[z][y][x+1] + grid[z][y+1][x-1:x+2]
    level_above = grid[z+1][y-1][x-1:x+2] + grid[z+1][y][x-1:x+2] + grid[z+1][y+1][x-1:x+2]
    adjacent_cubes = level_below + same_level + level_above
    return len(re.findall("#", adjacent_cubes))


with open(os.path.join(sys.path[0], 'input.txt'), mode='r', encoding='utf-8') as _file:
    new_grid = [_file.read().split('\n')]

new_grid.insert(0, ["".join(["."] * len(new_grid[0][0]))] * len(new_grid[0][0]))
new_grid.append(["".join(["."] * len(new_grid[0][0]))] * len(new_grid[0][0]))

for i in range(0, 6):
    # Add inactive surroundings
    for lev in range(0, len(new_grid)):
        for lin in range(0, len(new_grid[lev])):
            new_grid[lev][lin] = ".." + new_grid[lev][lin] + ".."
        new_grid[lev].insert(0, "".join(["."] * len(new_grid[0][0])))
        new_grid[lev].append("".join(["."] * len(new_grid[0][0])))
        new_grid[lev].insert(0, "".join(["."] * len(new_grid[0][0])))
        new_grid[lev].append("".join(["."] * len(new_grid[0][0])))

    new_grid.insert(0, ["".join(["."] * len(new_grid[0][0]))] * len(new_grid[0][0]))
    new_grid.append(["".join(["."] * len(new_grid[0][0]))] * len(new_grid[0][0]))

    active_adjacent = check_all_cubes(new_grid)

    # Split to change status of cubes
    split_grid = list()
    for k in range(0, len(new_grid)):
        split_grid.append(list())
        for li in new_grid[k]:
            split_grid[k].append(list(li))

    # Change status of cubes
    for a in range(1, len(new_grid)-1):
        for b in range(1, len(new_grid[a])-1):
            for c in range(1, len(new_grid[a][b])-1):
                # print(a, b, c)
                # print(new_grid[a][b][c])
                # print(active_adjacent[a][b][c])
                if new_grid[a][b][c] == "#" and 1 < active_adjacent[a][b][c] < 4:
                    split_grid[a][b][c] = "#"
                    # print('#')
                elif new_grid[a][b][c] == "." and active_adjacent[a][b][c] == 3:
                    split_grid[a][b][c] = "#"
                    # print('#')
                else:
                    split_grid[a][b][c] = "."
                    # print('.')

    # Join again
    for k in range(0, len(new_grid)):
        for li in range(0, len(new_grid[k])):
            new_grid[k][li] = ''.join(split_grid[k][li])

    print('---------------------------------')
    for k in new_grid:
        print('---------------------------------')
        for li in k:
            print(li)

all_cubes = ""
for niva in range(0, len(new_grid)):
    for rad in range(0, len(new_grid[niva])):
        all_cubes += new_grid[niva][rad]

print(len(re.findall("#", all_cubes)))
