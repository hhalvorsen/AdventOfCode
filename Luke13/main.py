import os, sys, re


def find_next_possibility(my_arrival, bus_time):
    bus_departure = bus_time
    while bus_departure < my_arrival:
        bus_departure += bus_time

    return bus_departure


def find_next_possibility2(my_arrival, bus_interval, previous_departure):
    bus_departure = previous_departure
    while bus_departure < my_arrival:
        bus_departure += bus_interval

    return bus_departure


with open(os.path.join(sys.path[0], 'input.txt'), mode='r', encoding='utf-8') as _file:
    info = _file.read().split('\n')
"""
# Del 1
bus_schedules = re.findall("[0-9]+", info[1])
my_arrival_time = int(info[0])
bus_schedules = [int(i) for i in bus_schedules]
shortest_wait = 1000000
result = 0
for i in range(0, len(bus_schedules)):
    wait = find_next_possibility(my_arrival_time, bus_schedules[i]) - my_arrival_time
    if wait < shortest_wait:
        shortest_wait = wait
        result = bus_schedules[i] * wait

print(result)

"""

# Del 2



"""
info_split = info[1].split(",")
position = list()
bus_schedules = re.findall("[0-9]+", info[1])

for i in range(0, len(info_split)):
    if info_split[i] in bus_schedules:
        position.append(i)

bus_schedules = [int(i) for i in bus_schedules]
max_interval = max(bus_schedules)
max_int_pos = bus_schedules.index(max_interval)
position_difference = [x - position[max_int_pos] for x in position]
n = 534035653563227 - 10000
start_time = n - n % max_interval
check_times = [start_time + x for x in position_difference]
match = False
while not match:
    match = True
    for i in range(0, len(bus_schedules)):
        if check_times[i] % bus_schedules[i] != 0:
            start_time += max_interval
            check_times = [start_time + x for x in position_difference]
            match = False
            break

print(start_time+position_difference[0])
"""


"""
match = False
correct_gap = True
start_time = 100000000000000 - 100000000000000 % bus_schedules[0]
previous_bus_times = [start_time - start_time % x for x in bus_schedules]
while not match:
    start_time += bus_schedules[0]
   single_match = True
    iterator = 1
    while iterator < len(bus_schedules) and single_match:
        next_departure = find_next_possibility2(start_time, bus_schedules[iterator], previous_bus_times[iterator])
        if next_departure - start_time != position[iterator]:
            single_match = False
            previous_bus_times[iterator] = next_departure - bus_schedules[iterator]

        iterator += 1

    if single_match:
        match = True

print(start_time)

"""
