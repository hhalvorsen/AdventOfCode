import os, sys, re, copy


def check_all_cubes(grid):
    active_adjacent_grid = list()
    for hyper in range(0, len(grid)):
        active_adjacent_grid.append(list())
        for j in range(0, len(grid[hyper])):
            active_adjacent_grid[hyper].append(list())
            for line in grid[hyper][j]:
                active_adjacent_grid[hyper][j].append(list(line))
    for hyper in range(1, len(grid)-1):
        for level in range(1, len(grid[hyper])-1):
            for row in range(1, len(grid[hyper][level])-1):
                for col in range(1, len(grid[hyper][level][row])-1):
                    active_adjacent_grid[hyper][level][row][col] = active_adjacent_cubes(col, row, level, hyper, grid)

    return active_adjacent_grid


def active_adjacent_cubes(x, y, z, w, grid):
    """print(w, z, y, x)
    print(len(grid[w]))
    print(len(grid[w][z]))
    print(len(grid[w][z][y]))
    print(grid[w+1][z+1])"""
    wu_level_below = grid[w-1][z - 1][y - 1][x - 1:x + 2] + grid[w-1][z - 1][y][x - 1:x + 2] + grid[w-1][z - 1][y + 1][
                                                                                        x - 1:x + 2]
    wu_same_level = grid[w-1][z][y - 1][x - 1:x + 2] + grid[w-1][z][y][x - 1:x + 2] + grid[w-1][z][y + 1][
                                                                                                x - 1:x + 2]
    wu_level_above = grid[w-1][z + 1][y - 1][x - 1:x + 2] + grid[w-1][z + 1][y][x - 1:x + 2] + grid[w-1][z + 1][y + 1][
                                                                                        x - 1:x + 2]
    # same w
    level_below = grid[w][z-1][y-1][x-1:x+2] + grid[w][z-1][y][x-1:x+2] + grid[w][z-1][y+1][x-1:x+2]
    same_level = grid[w][z][y-1][x-1:x+2] + grid[w][z][y][x-1] + grid[w][z][y][x+1] + grid[w][z][y+1][x-1:x+2]
    level_above = grid[w][z+1][y-1][x-1:x+2] + grid[w][z+1][y][x-1:x+2] + grid[w][z+1][y+1][x-1:x+2]

    wo_level_below = grid[w + 1][z - 1][y - 1][x - 1:x + 2] + grid[w + 1][z - 1][y][x - 1:x + 2] + grid[w + 1][z - 1][
                                                                                    y + 1][x - 1:x + 2]
    wo_same_level = grid[w + 1][z][y - 1][x - 1:x + 2] + grid[w + 1][z][y][x - 1:x + 2] + grid[w + 1][z][y + 1][
                                                                                       x - 1:x + 2]
    wo_level_above = grid[w + 1][z + 1][y - 1][x - 1:x + 2] + grid[w + 1][z + 1][y][x - 1:x + 2] + grid[w + 1][z + 1][
                                                                                        y + 1][x - 1:x + 2]

    adjacent_cubes = (wu_level_below + wu_same_level + wu_level_above + level_below + same_level + level_above +
                      wo_level_below + wo_same_level + wo_level_above)
    return len(re.findall("#", adjacent_cubes))


with open(os.path.join(sys.path[0], 'input.txt'), mode='r', encoding='utf-8') as _file:
    start_grid = [_file.read().split('\n')]

start_grid.insert(0, ["".join(["."] * len(start_grid[0][0]))] * len(start_grid[0][0]))
start_grid.append(["".join(["."] * len(start_grid[0][0]))] * len(start_grid[0][0]))
print(start_grid)
empty_grid = [copy.deepcopy(start_grid[0])] * len(start_grid[0][0])
new_grid = [empty_grid, start_grid, copy.deepcopy(empty_grid)]

print(new_grid)
for i in range(0, 6):
    # Add inactive surroundings
    for hyp in range(0, len(new_grid)):
        for lev in range(0, len(new_grid[hyp])):
            for lin in range(0, len(new_grid[hyp][lev])):
                new_grid[hyp][lev][lin] = ".." + copy.deepcopy(new_grid[hyp][lev][lin]) + ".."
            new_grid[hyp][lev].insert(0, "".join(["."] * len(new_grid[0][0][0])))
            new_grid[hyp][lev].append("".join(["."] * len(new_grid[0][0][0])))
            new_grid[hyp][lev].insert(0, "".join(["."] * len(new_grid[0][0][0])))
            new_grid[hyp][lev].append("".join(["."] * len(new_grid[0][0][0])))

        new_grid[hyp].insert(0, ["".join(["."] * len(new_grid[hyp][0][0]))] * len(new_grid[hyp][0]))
        new_grid[hyp].append(["".join(["."] * len(new_grid[hyp][0][0]))] * len(new_grid[hyp][0]))

    empty_grid = [copy.deepcopy(new_grid[0][0])] * len(new_grid[0][0][0])
    new_grid.insert(0, empty_grid)
    new_grid.append(copy.deepcopy(empty_grid))

    active_adjacent = check_all_cubes(new_grid)

    # Split to change status of cubes
    split_grid = list()
    for h in range(0, len(new_grid)):
        split_grid.append(list())
        for k in range(0, len(new_grid[h])):
            split_grid[h].append(list())
            for li in new_grid[h][k]:
                split_grid[h][k].append(list(li))

    # Change status of cubes
    for d in range(1, len(new_grid)-1):
        for a in range(1, len(new_grid[d])-1):
            for b in range(1, len(new_grid[d][a])-1):
                for c in range(1, len(new_grid[d][a][b])-1):
                    # print(a, b, c)
                    # print(new_grid[a][b][c])
                    # print(active_adjacent[a][b][c])
                    if new_grid[d][a][b][c] == "#" and 1 < active_adjacent[d][a][b][c] < 4:
                        split_grid[d][a][b][c] = "#"
                        # print('#')
                    elif new_grid[d][a][b][c] == "." and active_adjacent[d][a][b][c] == 3:
                        split_grid[d][a][b][c] = "#"
                        # print('#')
                    else:
                        split_grid[d][a][b][c] = "."
                        # print('.')

    # Join again
    for h in range(0, len(new_grid)):
        for k in range(0, len(new_grid[h])):
            for li in range(0, len(new_grid[h][k])):
                new_grid[h][k][li] = ''.join(split_grid[h][k][li])

all_cubes = ""
for h in range(0, len(new_grid)):
    for niva in range(0, len(new_grid[h])):
        for rad in range(0, len(new_grid[h][niva])):
            all_cubes += new_grid[h][niva][rad]

print(len(re.findall("#", all_cubes)))
