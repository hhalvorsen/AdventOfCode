import sys, os, re, copy


def check_all_seats(seats):
    occupied_adjacent_matrix = list()
    for line in seats:
        occupied_adjacent_matrix.append(list(line))

    for rad in range(0, len(seats)):
        for col in range(0, len(seats[0])):
            occupied_adjacent_matrix[rad][col] = occupied_visible_seats(rad, col, seats)

    return occupied_adjacent_matrix


def occupied_adjacent_seats(r, c, seat_matrix):
    if r == 0 and c == 0:  # Top left corner
        adjacent_seats = seat_matrix[r][c+1] + seat_matrix[r+1][c:c+2]
    elif r == 0 and c == len(seat_matrix[0]) - 1:  # Top right corner
        adjacent_seats = seat_matrix[r][c-1] + seat_matrix[r+1][c-1:]
    elif r == len(seat_matrix) - 1 and c == 0:  # Bottom left corner
        adjacent_seats = seat_matrix[r-1][c:c+2] + seat_matrix[r][c+1]
    elif r == len(seat_matrix) - 1 and c == len(seat_matrix[0]) - 1:  # Bottom right corner
        adjacent_seats = seat_matrix[r-1][c-1:] + seat_matrix[r][c-1]
    elif r == 0 and 0 < c < len(seat_matrix[0]) - 1:  # Top row
        adjacent_seats = seat_matrix[r][c-1] + seat_matrix[r][c+1] + seat_matrix[r+1][c-1:c+2]
    elif r == len(seat_matrix) - 1 and 0 < c < len(seat_matrix[0]) - 1:  # Bottom row
        adjacent_seats = seat_matrix[r-1][c-1:c+2] + seat_matrix[r][c-1] + seat_matrix[r][c+1]
    elif 0 < r < len(seat_matrix) - 1 and c == 0:  # Left col
        adjacent_seats = seat_matrix[r-1][c:c+2] + seat_matrix[r][c+1] + seat_matrix[r+1][c:c+2]
    elif 0 < r < len(seat_matrix) - 1 and c == len(seat_matrix[0]) - 1:  # Right col
        adjacent_seats = seat_matrix[r-1][c-1:] + seat_matrix[r][c-1] + seat_matrix[r+1][c-1:]
    else:
        adjacent_seats = seat_matrix[r-1][c-1:c+2] + seat_matrix[r][c-1] + seat_matrix[r][c+1] \
                         + seat_matrix[r+1][c-1:c+2]

    return len(re.findall("#", adjacent_seats))


def occupied_visible_seats(r, c, seat_matrix):
    directions = [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1]]
    directions_step = [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1]]
    found_seats = 0
    occupied_seats = 0
    while found_seats < 8:
        pop_directions = list()  # Liste over de elementene som skal slettes fra directions
        for d in range(0, len(directions)):
            element_r = r + directions[d][0]
            element_c = c + directions[d][1]
            if element_r not in range(0, len(seat_matrix)) or element_c not in range(0, len(seat_matrix[0])):
                pop_directions.append(d)
                found_seats += 1
            elif seat_matrix[element_r][element_c] == ".":
                directions[d][0] += directions_step[d][0]
                directions[d][1] += directions_step[d][1]
            elif seat_matrix[element_r][element_c] == "#":
                pop_directions.append(d)
                found_seats += 1
                occupied_seats += 1
            elif seat_matrix[element_r][element_c] == "L":
                pop_directions.append(d)
                found_seats += 1

        # Slett elementer fra directions
        pop_directions.sort(reverse=True)  # Starter med de bakerste elementene
        for pd in pop_directions:
            directions.pop(pd)
            directions_step.pop(pd)

    return occupied_seats


with open(os.path.join(sys.path[0], 'input.txt'), mode='r', encoding='utf-8') as _file:
    new_seats = _file.read().split('\n')


old_seats = list()
counter = 0
while old_seats != new_seats:
    counter += 1
    if counter == 1000:
        print("Counter max!")
        break

    old_seats = copy.deepcopy(new_seats)
    occupied_adjacent = check_all_seats(old_seats)

    # Split to change status of seats
    split_matrix = list()
    for x in old_seats:
        split_matrix.append(list(x))

    # Replace crammed seats
    for i in range(0, len(new_seats)):
        for j in range(0, len(new_seats[0])):
            if occupied_adjacent[i][j] == 0 and split_matrix[i][j] == 'L':
                split_matrix[i][j] = '#'
            elif occupied_adjacent[i][j] > 4 and split_matrix[i][j] == '#':
                split_matrix[i][j] = 'L'

    # Join again
    for i in range(0, len(split_matrix)):
        new_seats[i] = ''.join(split_matrix[i])

all_seats = ""
for row in new_seats:
    all_seats += row

print(len(re.findall("#", all_seats)))
