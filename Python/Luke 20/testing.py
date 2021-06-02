import re


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


def get_tile_active_pixels(t):
    active_p = list()
    for i in range(1, len(t) - 1):
        active_p.append(t[i][1:-1])
    return active_p


def flip_tile(t):
    return [i[::-1] for i in t]


test_grid = ['abc', 'efg', 'ijk', 'mno']
for li in test_grid:
    print(li)

r_grid = rotate_tile(test_grid)
print('Rotated:')
for li in r_grid:
    print(li)

flipped_grid = flip_tile(test_grid)
print('Flipped:')
for li in flipped_grid:
    print(li)

print(flip_tile(test_grid))
print(get_tile_active_pixels(test_grid))
print(rotate_tile(test_grid))

w = {'a': 0, 'b': 0, 'c': 0, 'd': 0}
u = 'a'
if u in w:
    print('Match')
else:
    print('No Match')


re_test = 'asdf1a1'
print(re.search('.....1', re_test).start())

if 'e' in w:
    w['e'] = 2
else:
    w['e'] = 1
print(w)
