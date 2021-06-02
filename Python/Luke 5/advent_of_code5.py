import sys, os, re


def find_seat_id(seat):
    row_values = [64, 32, 16, 8, 4, 2, 1]
    row = sum(row_values[i] for i in range(0, 7) if (seat[i] == 'B'))
    col_values = [4, 2, 1]
    col = sum(col_values[m-7] for m in range(7, 10) if (seat[m] == 'R'))
    return row*8 + col


with open(os.path.join(sys.path[0], 'input.txt'), mode='r', encoding='utf-8') as _file:
    records = _file.read().split('\n')
max_id = 0
seat_ids = list()
for seat_code in records:
    current_id = find_seat_id(seat_code)
    if max_id < current_id:
        max_id = current_id

    seat_ids.append(current_id)

possible_ids = sorted(k for k in seat_ids if (k > 7 & k < 127*8))
my_seat_id = 0
for j in range(0, len(possible_ids) - 2):
    if possible_ids[j+1] - possible_ids[j] > 1:
        my_seat_id = possible_ids[j] + 1

print(max_id)
print(my_seat_id)

