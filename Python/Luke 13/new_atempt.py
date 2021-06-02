import os, sys, re


def mod_inverse(a, m):
    m0 = m
    y = 0
    x = 1

    if m == 1:
        return 0

    while a > 1:

        # q is quotient
        q = a // m

        t = m

        # m is remainder now, process
        # same as Euclid's algo
        m = a % m
        a = t
        t = y

        # Update x and y
        y = x - q * y
        x = t

        # Make x positive
    if x < 0:
        x = x + m0

    return x


with open(os.path.join(sys.path[0], 'input.txt'), mode='r', encoding='utf-8') as _file:
    info = _file.read().split('\n')

info_split = info[1].split(",")
position = list()
bus_schedules = re.findall("[0-9]+", info[1])

for i in range(0, len(info_split)):
    if info_split[i] in bus_schedules:
        position.append(i)

bus_schedules = [int(i) for i in bus_schedules]
gap = [bus_schedules[i] - position[i] for i in range(0, len(bus_schedules))]

bus_schedules_product = 1
for i in bus_schedules:
    bus_schedules_product *= i

n_list = [bus_schedules_product / n for n in bus_schedules]
modular_inverse_n = [mod_inverse(n_list[i], bus_schedules[i]) for i in range(0, len(bus_schedules))]

result = 0
for i in range(0, len(gap)):
    result += gap[i] * n_list[i] * modular_inverse_n[i]

while result > 0:
    result -= bus_schedules_product

result += bus_schedules_product
print(result)
