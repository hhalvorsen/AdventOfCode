import os, sys, re, math, copy


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
    # Orienter alle sidene med klokka og flipped
    return [t_row, r_side, b_row[::-1], l_side[::-1], t_row[::-1], r_side[::-1], b_row, l_side]


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


with open(os.path.join(sys.path[0], 'input.txt'), mode='r', encoding='utf-8') as _file:
    info = _file.read().split('\n\n')

tiles_info = {}
corners = list()
sides = list()
center = list()

for tile in info:
    t_id, pixels = tile.split('\n', 1)
    pixels = pixels.split('\n')
    top, right_side, bottom, left_side, f_top, f_right_side, f_bottom, f_left_side = get_tile_sides(pixels)
    tiles_info[t_id] = {'id': t_id, 'pixels': pixels, 'active_pixels': get_tile_active_pixels(pixels),
                        'sides': [top, right_side, bottom, left_side],
                        'flipped_sides': [f_top, f_right_side, f_bottom, f_left_side]}

for key in tiles_info:
    matching_sides = list()
    flipped_matching_sides = list()
    for sub_key in tiles_info:
        if sub_key != key:
            for x in range(0, len(tiles_info[key]['sides'])):
                if tiles_info[key]['sides'][x] in tiles_info[sub_key]['sides'] or \
                        tiles_info[key]['sides'][x] in tiles_info[sub_key]['flipped_sides']:
                    matching_sides.append(x)
            for x in range(0, len(tiles_info[key]['flipped_sides'])):
                if tiles_info[key]['flipped_sides'][x] in tiles_info[sub_key]['sides'] or \
                        tiles_info[key]['flipped_sides'][x] in tiles_info[sub_key]['flipped_sides']:
                    flipped_matching_sides.append(x)
    tiles_info[key]['matching_sides'] = matching_sides
    tiles_info[key]['flipped_matching_sides'] = flipped_matching_sides
    if key == 'Tile 1889:':
        print(key)
        print('Matches', max(len(matching_sides), len(flipped_matching_sides)))
    if max(len(matching_sides), len(flipped_matching_sides)) == 2:
        corners.append(key)
    if max(len(matching_sides), len(flipped_matching_sides)) == 3:
        sides.append(key)
    if max(len(matching_sides), len(flipped_matching_sides)) == 4:
        center.append(key)

# ['Tile 3407:', 'Tile 1889:']
print('Corners: ', len(corners))
print('Sides: ', len(sides))
print('Center: ', len(center))

corners_product = 1
for corner in corners:
    print(corner)
    corners_product *= int(re.search('[0-9]+', corner).group())

print('Part 1')
print(corners_product)

first_corner = corners[0]
if len(tiles_info[first_corner]['flipped_matching_sides']) == 2:
    tiles_info[first_corner]['pixels'] = flip_tile(tiles_info[first_corner]['pixels'])
    # Rotate while matching sides aren't bottom and right
    tiles_info[first_corner]['flipped_matching_sides'].sort()
    while tiles_info[first_corner]['flipped_matching_sides'] != [1, 2]:
        tiles_info[first_corner]['pixels'] = rotate_tile(tiles_info[first_corner]['pixels'])
        x, y = tiles_info[first_corner]['flipped_matching_sides']
        top, right_side, bottom, left_side, f_top, f_right_side, f_bottom, f_left_side = \
            get_tile_sides(tiles_info[first_corner]['pixels'])
        tiles_info[first_corner]['sides'] = [top, right_side, bottom, left_side]
        x = (x+1) % 4
        y = (y+1) % 4
        tiles_info[first_corner]['flipped_matching_sides'] = [x, y]
elif len(tiles_info[first_corner]['matching_sides']) == 2:
    # Rotate while matching sides aren't bottom and right
    tiles_info[first_corner]['matching_sides'].sort()
    while tiles_info[first_corner]['matching_sides'] != [1, 3]:
        tiles_info[first_corner]['pixels'] = rotate_tile(tiles_info[first_corner]['pixels'])
        top, right_side, bottom, left_side, f_top, f_right_side, f_bottom, f_left_side = \
            get_tile_sides(tiles_info[first_corner]['pixels'])
        tiles_info[first_corner]['sides'] = [top, right_side, bottom, left_side]
        x, y = tiles_info[first_corner]['matching_sides']
        x = (x + 1) % 4
        y = (y + 1) % 4
        tiles_info[first_corner]['matching_sides'] = [x, y]
else:
    print("Error")

remaining_tiles = copy.deepcopy(tiles_info)
image_ids = [[first_corner]]
image = list()
image_row = get_tile_active_pixels(tiles_info[first_corner]['pixels'])
remaining_tiles.pop(first_corner)

row_length = math.sqrt(len(info))
index = 1
while index < row_length:
    matching_tile = False
    matching_tile_id = ''
    for key in remaining_tiles:
        print(image_ids[0], 'index - 1', index - 1)
        if tiles_info[image_ids[0][index - 1]]['sides'][1] in remaining_tiles[key]['sides']:
            rotate_times = 3 - remaining_tiles[key]['sides'].index(tiles_info[image_ids[0][index - 1]]['sides'][1])
            while rotate_times > 0:
                remaining_tiles[key]['pixels'] = rotate_tile(remaining_tiles[key]['pixels'])
                remaining_tiles[key]['active_pixels'] = get_tile_active_pixels(remaining_tiles[key]['pixels'])
                rotate_times -= 1
            matching_tile_id = key
            matching_tile = True
            break
        elif tiles_info[image_ids[0][index - 1]]['sides'][1] in remaining_tiles[key]['flipped_sides']:
            remaining_tiles[key]['pixels'] = flip_tile(remaining_tiles[key]['pixels'])
            rotate_times = 3 - remaining_tiles[key]['flipped_sides'].\
                index(tiles_info[image_ids[0][index - 1]]['sides'][1])
            while rotate_times > 0:
                remaining_tiles[key]['pixels'] = rotate_tile(remaining_tiles[key]['pixels'])
                remaining_tiles[key]['active_pixels'] = get_tile_active_pixels(remaining_tiles[key]['pixels'])
                rotate_times -= 1
            matching_tile_id = key
            matching_tile = True
            break

    if matching_tile:
        image_ids[0].append(matching_tile_id)
        image_row = append_row(image_row, remaining_tiles[matching_tile_id]['active_pixels'])
        remaining_tiles.pop(matching_tile_id)
        index += 1
    else:
        print('No Match')
        break

"""
index = 0
rad = 1
while rad < row_length:
    while index < row_length:
        matching_tile = False
        matching_tile_id = ''
        for key in remaining_tiles:
            if tiles_info[image_ids[rad-1][index - 1]]['sides'][1] in remaining_tiles[key]['sides']:
                rotate_times = 3 - remaining_tiles[key]['sides'].index(tiles_info[image_ids[rad-1][index - 1]]['sides'][1])
                while rotate_times > 0:
                    remaining_tiles[key]['pixels'] = rotate_tile(remaining_tiles[key]['pixels'])
                    remaining_tiles[key]['active_pixels'] = get_tile_active_pixels(remaining_tiles[key]['pixels'])
                    rotate_times -= 1
                matching_tile_id = key
                matching_tile = True
                break
            elif tiles_info[image_ids[0][index - 1]]['sides'][1] in remaining_tiles[key]['flipped_sides']:
                remaining_tiles[key]['pixels'] = flip_tile(remaining_tiles[key]['pixels'])
                rotate_times = 3 - remaining_tiles[key]['flipped_sides'].\
                    index(tiles_info[image_ids[0][index - 1]]['sides'][1])
                while rotate_times > 0:
                    remaining_tiles[key]['pixels'] = rotate_tile(remaining_tiles[key]['pixels'])
                    remaining_tiles[key]['active_pixels'] = get_tile_active_pixels(remaining_tiles[key]['pixels'])
                    rotate_times -= 1
                matching_tile_id = key
                matching_tile = True
                break

        if matching_tile:
            image_row = append_row(image_row, remaining_tiles[matching_tile_id]['active_pixels'])
            remaining_tiles.pop(matching_tile_id)
            index += 1
        else:
            print('No Match')
            break
    rad += 1

"""
