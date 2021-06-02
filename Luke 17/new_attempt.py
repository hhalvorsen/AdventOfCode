import os, sys


def find_start_positions(grid):
    start_positions = list()
    for y in range(0, len(grid)):
        for x in range(0, len(grid[y])):
            if grid[y][x] == "#":
                start_positions.append([0, 0, y, x])
    return start_positions


def find_nearby_positions(a_positions):
    nb_positions = list()
    for position in a_positions:
        for w in range(-1, 2):
            for z in range(-1, 2):
                for y in range(-1, 2):
                    for x in range(-1, 2):
                        if [w, z, y, x] != [0, 0, 0, 0]:
                            nb_pos = [position[0]+w, position[1]+z, position[2]+y, position[3]+x]
                            if nb_pos not in nb_positions and nb_pos not in a_positions:
                                nb_positions.append(nb_pos)
    return nb_positions


def check_nearby_positions(position, a_positions):
    counter = 0
    for w in range(-1, 2):
        for z in range(-1, 2):
            for y in range(-1, 2):
                for x in range(-1, 2):
                    if [w, z, y, x] != [0, 0, 0, 0]:
                        nb_position = [position[0]+w, position[1]+z, position[2]+y, position[3]+x]
                        if nb_position in a_positions:
                            counter += 1
    return counter


with open(os.path.join(sys.path[0], 'input.txt'), mode='r', encoding='utf-8') as _file:
    data = _file.read().split('\n')

active_positions = find_start_positions(data)

for cycles in range(0, 6):
    pop_active_positions = list()
    for i in range(0, len(active_positions)):
        if check_nearby_positions(active_positions[i], active_positions) not in [2, 3]:
            pop_active_positions.append(i)
    pop_active_positions.sort(reverse=True)

    nearby_positions = find_nearby_positions(active_positions)
    add_active_positions = list()
    for nb_p in nearby_positions:
        if nb_p not in active_positions:
            if check_nearby_positions(nb_p, active_positions) == 3:
                add_active_positions.append(nb_p)

    for pop_index in pop_active_positions:
        active_positions.pop(pop_index)

    for add_p in add_active_positions:
        active_positions.append(add_p)

    print(len(active_positions))

