def shuffle_cups(c):
    front_cup = c[0]
    next_three = c[1:4]
    c = c[4:]
    insert_number = front_cup - 1
    while insert_number not in c:
        insert_number -= 1
        if insert_number < min(c):
            insert_number = 9
    insert_index = c.index(insert_number) + 1
    for i in next_three:
        c.insert(insert_index, i)
        insert_index += 1
    c.append(front_cup)
    return c


test_cups = [3, 8, 9, 1, 2, 5, 4, 6, 7]
actual_cups = [5, 8, 3, 9, 7, 6, 2, 4, 1]

cups = actual_cups
runs = 100
for x in range(0, runs):
    cups = shuffle_cups(cups)

one_index = cups.index(1)
result = ''
for x in cups[one_index:]:
    result = result + str(x)
for x in cups[:one_index]:
    result = result + str(x)

print(result)

