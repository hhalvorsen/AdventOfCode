import os, sys, re, copy


def get_tile_sides(t):
    t_row = t[0]
    b_row = t[-1]
    l_side = list()
    r_side = list()
    for i in t:
        l_side.append(i[0])
        r_side.append(i[-1])
    l_side = "".join(l_side)
    r_side = "".join(r_side)
    return [t_row, r_side, b_row, l_side]


def rotate_tile(t):
    # Rotates clockwise
    width = len(t[0])
    height = len(t)
    grid = [[char for char in line] for line in t]
    rotated_grid = list()
    for col in range(0, width):
        rotated_line = list()
        for row in range(height-1, -1, -1):
            rotated_line.append(grid[row][col])
        rotated_grid.append(rotated_line)
    return ["".join(line) for line in rotated_grid]


def flip_tile(t):
    return [i[::-1] for i in t]


def get_tile_active_pixels(t):
    active_p = list()
    for i in range(1, len(t)-1):
        active_p.append(t[i][1:-1])
    return active_p


def append_row(row, append_r):
    for i in range(0, len(append_r)):
        row[i] = row[i] + append_r[i]
    return row


def check_if_next(id_dict, direction, all_ids, copy_all_ids):
    next_exists = False
    next_id = 'Fail'
    # Directions: north - 0, east - 1, south - 2, west - 3
    for code in all_ids:
        rotated = 0
        while rotated < 4:
            if id_dict['sides'][direction] == all_ids[code]['sides'][(direction+2) % 4]:
                copy_all_ids[code] = all_ids[code]
                return [True, code]
            else:
                all_ids[code]['pixels'] = rotate_tile(all_ids[code]['pixels'])
                all_ids[code]['active_pixels'] = get_tile_active_pixels(all_ids[code]['pixels'])
                all_ids[code]['sides'] = get_tile_sides(all_ids[code]['pixels'])
                rotated += 1

        # Flip
        all_ids[code]['pixels'] = flip_tile(all_ids[code]['pixels'])
        all_ids[code]['active_pixels'] = get_tile_active_pixels(all_ids[code]['pixels'])
        all_ids[code]['sides'] = get_tile_sides(all_ids[code]['pixels'])

        rotated = 0
        while rotated < 4:
            if id_dict['sides'][direction] == all_ids[code]['sides'][(direction+2) % 4]:
                copy_all_ids[code] = all_ids[code]
                return [True, code]
            else:
                all_ids[code]['pixels'] = rotate_tile(all_ids[code]['pixels'])
                all_ids[code]['active_pixels'] = get_tile_active_pixels(all_ids[code]['pixels'])
                all_ids[code]['sides'] = get_tile_sides(all_ids[code]['pixels'])
                rotated += 1

    return [next_exists, next_id]


def build_north(id_dict, all_ids, copy_all_ids):
    northern_rows = list()
    western_row = list()
    eastern_row = list()

    # Check if next exists
    # save next id_dict
    # pop next
    # build north for next
    # build west
    # build east
    # return top rows

    next_north_exists, next_north_id = check_if_next(id_dict, 0, all_ids, copy_all_ids)
    if next_north_exists:
        next_id_dict = all_ids[next_north_id]
        all_ids.pop(next_north_id)
        northern_rows = build_north(next_id_dict, all_ids, copy_all_ids)

    next_west_exists, next_west_id = check_if_next(id_dict, 3, all_ids, copy_all_ids)
    if next_west_exists:
        next_id_dict = all_ids[next_west_id]
        all_ids.pop(next_west_id)
        western_row = build_west(next_id_dict, all_ids, copy_all_ids)

    next_east_exists, next_east_id = check_if_next(id_dict, 1, all_ids, copy_all_ids)
    if next_east_exists:
        next_id_dict = all_ids[next_east_id]
        all_ids.pop(next_east_id)
        eastern_row = build_west(next_id_dict, all_ids, copy_all_ids)

    this_row = list()
    if next_west_exists and next_east_exists:
        this_row = western_row
        this_row.append(id_dict['id'])
        for i in eastern_row:
            this_row.append(i)
    elif next_west_exists:
        this_row = western_row
        this_row.append(id_dict['id'])
    elif next_east_exists:
        this_row = [id_dict['id']]
        for i in eastern_row:
            this_row.append(i)

    if next_north_exists:
        northern_rows.append(this_row)
        return northern_rows
    else:
        return [this_row]


def build_west(id_dict, all_ids, copy_all_ids):
    next_west_exists, next_west_id = check_if_next(id_dict, 3, all_ids, copy_all_ids)
    if next_west_exists:
        next_id_dict = all_ids[next_west_id]
        all_ids.pop(next_west_id)
        western_row = build_west(next_id_dict, all_ids, copy_all_ids)
        western_row.append(id_dict['id'])
        return western_row
    else:
        return [id_dict['id']]


def build_east(id_dict, all_ids, copy_all_ids):
    next_east_exists, next_east_id = check_if_next(id_dict, 1, all_ids, copy_all_ids)
    if next_east_exists:
        next_id_dict = all_ids[next_east_id]
        all_ids.pop(next_east_id)
        eastern_row = build_west(next_id_dict, all_ids, copy_all_ids)
        eastern_row.insert(0, id_dict['id'])
        return eastern_row
    else:
        return [id_dict['id']]


def build_south(id_dict, all_ids, copy_all_ids):
    southern_rows = list()
    western_row = list()
    eastern_row = list()

    # Check if next exists
    # save next id_dict
    # pop next
    # build north for next
    # build west
    # build east
    # return top rows

    next_south_exists, next_south_id = check_if_next(id_dict, 2, all_ids, copy_all_ids)
    if next_south_exists:
        next_id_dict = all_ids[next_south_id]
        all_ids.pop(next_south_id)
        southern_rows = build_south(next_id_dict, all_ids, copy_all_ids)

    next_west_exists, next_west_id = check_if_next(id_dict, 3, all_ids, copy_all_ids)
    if next_west_exists:
        next_id_dict = all_ids[next_west_id]
        all_ids.pop(next_west_id)
        western_row = build_west(next_id_dict, all_ids, copy_all_ids)

    next_east_exists, next_east_id = check_if_next(id_dict, 1, all_ids, copy_all_ids)
    if next_east_exists:
        next_id_dict = all_ids[next_east_id]
        all_ids.pop(next_east_id)
        eastern_row = build_west(next_id_dict, all_ids, copy_all_ids)

    this_row = list()
    if next_west_exists and next_east_exists:
        this_row = western_row
        this_row.append(id_dict['id'])
        for i in eastern_row:
            this_row.append(i)
    elif next_west_exists:
        this_row = western_row
        this_row.append(id_dict['id'])
    elif next_east_exists:
        this_row = [id_dict['id']]
        for i in eastern_row:
            this_row.append(i)

    if next_south_exists:
        southern_rows.append(this_row)
        return southern_rows
    else:
        return [this_row]


def build_ids(start_id, all_ids, copy_all_ids):
    start_id_dict = all_ids[start_id]
    all_ids.pop(start_id)

    # northern_rows inkluderer raden til start_id
    northern_rows = build_north(start_id_dict, all_ids, copy_all_ids)

    southern_rows = list()
    next_south_exists, next_south_id = check_if_next(start_id_dict, 2, all_ids, copy_all_ids)
    if next_south_exists:
        next_id_dict = all_ids[next_south_id]
        all_ids.pop(next_south_id)
        southern_rows = build_south(next_id_dict, all_ids, copy_all_ids)

    if next_south_exists:
        for i in southern_rows:
            northern_rows.append(i)

    return northern_rows


def draw_picture(id_picture, copy_all_ids):
    picture = list()
    for picture_row in id_picture:
        picture_part = copy.deepcopy(copy_all_ids[picture_row[0]]['active_pixels'])
        for i in range(1, len(picture_row)):
            picture_part = append_row(picture_part, copy_all_ids[picture_row[i]]['active_pixels'])
        for i in picture_part:
            picture.append(i)

    return picture


def find_sea_monsters(picture, pattern):
    len_pattern1 = len(pattern[1])
    len_pattern2 = len(pattern[2])
    sm = 0
    for i in range(0, len(picture) - len(pattern)):
        search_start = 0
        while search_start < len(picture[0]) - len_pattern1 and re.search(pattern[0], picture[i][search_start:]):
            search_start += re.search(pattern[0], picture[i][search_start:]).start()

            if (re.search(pattern[1], picture[i+1][search_start:search_start+len_pattern1]) and
                    re.search(pattern[2], picture[i+2][search_start:search_start + len_pattern2])):
                sm += 1
            search_start += 1
    return sm


with open(os.path.join(sys.path[0], 'input.txt'), mode='r', encoding='utf-8') as _file:
    info = _file.read().split('\n\n')

with open(os.path.join(sys.path[0], 'sea_monster.txt'), mode='r', encoding='utf-8') as _file:
    sea_monster = _file.read().split('\n')

with open(os.path.join(sys.path[0], 'test_find_sea_monsters.txt'), mode='r', encoding='utf-8') as _file:
    test_sea_monster = _file.read().split('\n')

tiles_info = {}
corners = list()
sides = list()
center = list()

for tile in info:
    t_id, pixels = tile.split('\n', 1)
    pixels = pixels.split('\n')
    tiles_info[t_id] = {'id': t_id, 'pixels': pixels, 'active_pixels': get_tile_active_pixels(pixels),
                        'sides': get_tile_sides(pixels)}

copy_tiles_info = copy.deepcopy(tiles_info)
# list(tiles_info.keys())[5]
corner_aim = ['Tile 2351:', 'Tile 1433:', 'Tile 3229:', 'Tile 1699:']
for start_tile in copy_tiles_info:
    tiles_info = copy.deepcopy(copy_tiles_info)
    match = False
    print(start_tile)
    image_ids = build_ids(start_tile, tiles_info, copy_tiles_info)
    if len(image_ids) == len(image_ids[0]) == 12:
        corners = [image_ids[0][0], image_ids[-1][0], image_ids[0][-1], image_ids[-1][-1]]
        for c in corners:
            if c not in corner_aim:
                match = False
                break
            else:
                match = True
    if match:
        print('Match')
        break
    else:
        print('No Match')

for x in image_ids:
    print(x)

image = draw_picture(image_ids, copy_tiles_info)

for x in range(0, len(sea_monster)):
    sea_monster[x] = re.sub('\s', '.', sea_monster[x])
    print(sea_monster[x])

n_sea_monsters = find_sea_monsters(image, sea_monster)
rot = 0

while rot < 4 and n_sea_monsters == 0:
    print(n_sea_monsters)
    image = rotate_tile(image)
    n_sea_monsters = find_sea_monsters(image, sea_monster)
    rot += 1

if n_sea_monsters == 0:
    image = flip_tile(image)
    rot = 0
    n_sea_monsters = find_sea_monsters(image, sea_monster)

    while rot < 4 and n_sea_monsters == 0:
        print(n_sea_monsters)
        image = rotate_tile(image)
        n_sea_monsters = find_sea_monsters(image, sea_monster)
        rot += 1
    
total_hashtags = 0
for bla in image:
    total_hashtags += len(re.findall('#', bla))

print(total_hashtags - n_sea_monsters*15)

print(n_sea_monsters)
