import os, sys, copy, re


def in_intervals(value, intervals):
    for interval in intervals:
        if interval[0] <= value <= interval[1]:
            return True
    return False


with open(os.path.join(sys.path[0], 'input.txt'), mode='r', encoding='utf-8') as _file:
    info = _file.read().split('\n\n')

rules_info = info[0].split('\n')
ticket_intervals = list()
rules = list()
for rule in rules_info:
    text, ranges = rule.split(': ')
    low_interval, separator, high_interval = ranges.split(' ')
    l_lim_l_int, h_lim_l_int = low_interval.split('-')
    ticket_intervals.append([int(l_lim_l_int), int(h_lim_l_int)])
    l_lim_h_int, h_lim_h_int = high_interval.split('-')
    ticket_intervals.append([int(l_lim_h_int), int(h_lim_h_int)])
    rules.append({"field": text, "l_int": [int(l_lim_l_int), int(h_lim_l_int)],
                  "h_int": [int(l_lim_h_int), int(h_lim_h_int)]})

for r in rules:
    print(r)

info_my_ticket = info[1].split('\n')
my_ticket = info_my_ticket[1].split(',')
info_nearby_tickets = info[2].split('\n')
nearby_tickets = list()
result = 0
for ticket in info_nearby_tickets[1:]:
    ticket_split = ticket.split(',')
    valid_ticket = True
    ticket_ints = list()
    for n in ticket_split:
        ticket_ints.append(int(n))
        if not in_intervals(int(n), ticket_intervals):
            # result += int(n)  # Del 1
            valid_ticket = False
            break
    if valid_ticket:
        nearby_tickets.append(ticket_ints)

# print(result)  # Del 1

fields = [r["field"] for r in rules]
possible_fields = list()
for i in range(0, len(nearby_tickets[0])):
    possible_fields.append(copy.deepcopy(fields))

for i in possible_fields:
    print(i)

for ticket in nearby_tickets:
    for n in range(0, len(ticket)):
        for r in rules:
            if not in_intervals(ticket[n], [r["l_int"], r["h_int"]]):
                if r["field"] in possible_fields[n]:
                    possible_fields[n].pop(possible_fields[n].index(r["field"]))

for i in possible_fields:
    print(i)

correct_fields = [""] * len(possible_fields)
all_empty = False

while not all_empty:
    for i in range(0, len(correct_fields)):
        print('--------------------')
        if len(possible_fields[i]) == 1:
            correct_fields[i] = possible_fields[i][0]
            for n in range(0, len(possible_fields)):
                print(correct_fields[i])
                print(possible_fields[n])
                if correct_fields[i] in possible_fields[n]:
                    possible_fields[n].pop(possible_fields[n].index(correct_fields[i]))

    for n in possible_fields:
        if len(n) > 0:
            all_empty = False
            break
        else:
            all_empty = True

print('--------------------')
print(correct_fields)

product = 1
for i in range(0, len(correct_fields)):
    if re.search('departure', correct_fields[i]):
        product *= int(my_ticket[i])

print(product)
