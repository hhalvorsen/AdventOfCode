import os, sys, re


def move_del1(ship_info, instruction):
    # ship_info [x_pos, y_pos, direction]
    ins_dir = instruction[0]
    ins_dist = int(instruction[1:])

    if ins_dir == "F":
        if ship_info[2] % 360 == 0:
            ins_dir = "N"
        elif ship_info[2] % 360 == 180:
            ins_dir = "S"
        elif ship_info[2] % 360 == 90:
            ins_dir = "E"
        elif ship_info[2] % 360 == 270:
            ins_dir = "W"

    if ins_dir == "N":
        ship_info[1] += ins_dist
    elif ins_dir == "S":
        ship_info[1] -= ins_dist
    elif ins_dir == "E":
        ship_info[0] += ins_dist
    elif ins_dir == "W":
        ship_info[0] -= ins_dist
    elif ins_dir == "R":
        ship_info[2] += ins_dist
    elif ins_dir == "L":
        ship_info[2] -= ins_dist

    return ship_info


def turn_waypoint(wp_x, wp_y, turn_dir, turn_dist):
    if turn_dist == 180:
        n_wp_x = -wp_x
        n_wp_y = -wp_y
    elif (turn_dir == "L" and turn_dist == 90) or (turn_dir == "R" and turn_dist == 270):
        n_wp_x = -wp_y
        n_wp_y = wp_x
    elif (turn_dir == "L" and turn_dist == 270) or (turn_dir == "R" and turn_dist == 90):
        n_wp_x = wp_y
        n_wp_y = -wp_x
    else:
        n_wp_x = wp_x
        n_wp_y = wp_y

    return [n_wp_x, n_wp_y]


def move_del2(ship_info, instruction):
    # ship_info [x_pos, y_pos, waypoint_x, waypoint_y]
    x = re.search("[A-Z]", instruction)
    ins_dir = instruction[x.start()]
    ins_dist = int(instruction[x.start()+1:])

    if ins_dir == "F":
        ship_info[0] += ship_info[2] * ins_dist
        ship_info[1] += ship_info[3] * ins_dist

    if ins_dir == "N":
        ship_info[3] += ins_dist
    elif ins_dir == "S":
        ship_info[3] -= ins_dist
    elif ins_dir == "E":
        ship_info[2] += ins_dist
    elif ins_dir == "W":
        ship_info[2] -= ins_dist
    elif ins_dir == "R" or ins_dir == "L":
        new_waypoint = turn_waypoint(ship_info[2], ship_info[3], ins_dir, ins_dist)
        ship_info[2] = new_waypoint[0]
        ship_info[3] = new_waypoint[1]

    return ship_info


with open(os.path.join(sys.path[0], 'input.txt'), mode='r', encoding='utf-8') as _file:
    directions = _file.read().split('\n')

"""
Del 1:
ship = [0, 0, 90]  # x_pos, y_pos, direction

for i in directions:
    ship = move_del1(ship, i)

print(abs(ship[0]) + abs(ship[1])) """

ship = [0, 0, 10, 1]  # x_pos, y_pos, waypoint_x, waypoint_y
for i in directions:
    ship = move_del2(ship, i)

print(abs(ship[0]) + abs(ship[1]))