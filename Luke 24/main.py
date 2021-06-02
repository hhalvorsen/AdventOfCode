import os, sys


def flip_tile(t, dic):
    if t in dic:
        if dic[t]['status'] == 'black':
            dic[t]['status'] = 'white'
        else:
            dic[t]['status'] = 'black'
    else:
        dic[t] = {'status': 'black', 'adjacent black': 0, 'adjacent tiles': find_adjacent_tiles(t)}

    return dic


def find_adjacent_tiles(t):
    e, n = t.split(',')
    e = float(e)
    n = float(n)
    t_ne = str(e + 0.5) + ',' + str(n + 1)
    t_e = str(e + 1) + ',' + str(n)
    t_se = str(e + 0.5) + ',' + str(n - 1)
    t_sw = str(e - 0.5) + ',' + str(n - 1)
    t_w = str(e - 1) + ',' + str(n)
    t_nw = str(e - 0.5) + ',' + str(n + 1)
    return [t_ne, t_e, t_se, t_sw, t_w, t_nw]


def insert_adjacent_tiles(a_tiles, temp_dic, a_dic):
    for pos in a_tiles:
        if pos not in temp_dic and pos not in a_dic:
            temp_dic[pos] = {'status': 'white', 'adjacent black': 0, 'adjacent tiles': find_adjacent_tiles(pos)}
    return temp_dic


def check_for_adjacent_black(dic):
    for k in dic:
        dic[k]['adjacent black'] = 0
        # print(k)
        # print(dic[k]['adjacent tiles'])
        for x in dic[k]['adjacent tiles']:
            if x in dic:
                # print(x, dic[x]['status'])
                if dic[x]['status'] == 'black':
                    dic[k]['adjacent black'] += 1
        # print(dic[k]['adjacent black'])

    return dic


def apply_rules(dic):
    pop_list = list()
    all_list = list()
    for k in dic:
        all_list.append(k)
        if dic[k]['adjacent black'] == 0 or (dic[k]['adjacent black'] > 2 and dic[k]['status'] == 'black'):
            pop_list.append(k)
        elif dic[k]['status'] == 'white' and dic[k]['adjacent black'] == 2:
            dic[k]['status'] = 'black'
    # print(len(all_list), all_list)
    # print(len(pop_list), pop_list)
    for x in pop_list:
        dic.pop(x)
    return dic


with open(os.path.join(sys.path[0], 'input'), mode='r', encoding='utf-8') as _file:
    info = _file.read().split('\n')

all_tiles = {'0,0': {'status': 'white', 'adjacent black': 0, 'adjacent tiles': find_adjacent_tiles('0,0')}}
for tile in info:
    north = float(0)
    east = float(0)

    i = 0
    while i < len(tile):
        if tile[i] == 'e':
            east += 1
        elif tile[i] == 'w':
            east -= 1
        elif tile[i] == 'n':
            i += 1
            north += 1
            if tile[i] == 'e':
                east += 0.5
            elif tile[i] == 'w':
                east -= 0.5
        elif tile[i] == 's':
            i += 1
            north -= 1
            if tile[i] == 'e':
                east += 0.5
            elif tile[i] == 'w':
                east -= 0.5
        i += 1

    position = [east, north]
    p = str(east) + ',' + str(north)

    all_tiles = flip_tile(p, all_tiles)

"""

b_t = 0
black_tiles = list()
for key in all_tiles:
    if all_tiles[key]['status'] == 'black':
        black_tiles.append(key)
        b_t += 1
print(b_t)
print(black_tiles)

status_string = ""
for i in black_tiles:
    if i in all_tiles:
        status_string = status_string + ' ' + i + ' ' + all_tiles[i]['status']
    else:
        status_string = status_string + ' ' + 'Gone'
print(status_string)
"""
# For a days:
for a in range(0, 100):
    # Find all adjacent tiles and add them to all_tiles with their respective adjacent tiles
    temp_tiles = {}
    for key in all_tiles:
        temp_tiles = insert_adjacent_tiles(all_tiles[key]['adjacent tiles'], temp_tiles, all_tiles)

    for key in temp_tiles:
        if key not in all_tiles:
            all_tiles[key] = temp_tiles[key]

    # Check all tiles in all_tiles, change number of adjacent black
    all_tiles = check_for_adjacent_black(all_tiles)

    # Apply rules to flip tiles, if zero adjacent black delete tile
    all_tiles = apply_rules(all_tiles)

    b_t = 0
    for key in all_tiles:
        if all_tiles[key]['status'] == 'black':
            b_t += 1
    print(b_t)


"""
# Del 1:
with open(os.path.join(sys.path[0], 'input'), mode='r', encoding='utf-8') as _file:
    info = _file.read().split('\n')

flipped_tiles = list()
for tile in info:
    north = 0
    east = 0

    i = 0
    while i < len(tile):
        if tile[i] == 'e':
            east += 1
        elif tile[i] == 'w':
            east -= 1
        elif tile[i] == 'n':
            i += 1
            north += 1
            if tile[i] == 'e':
                east += 0.5
            elif tile[i] == 'w':
                east -= 0.5
        elif tile[i] == 's':
            i += 1
            north -= 1
            if tile[i] == 'e':
                east += 0.5
            elif tile[i] == 'w':
                east -= 0.5
        i += 1

    position = [east, north]

    if position in flipped_tiles:
        flipped_tiles.pop(flipped_tiles.index(position))
    else:
        flipped_tiles.append(position)

print(len(flipped_tiles))
"""
