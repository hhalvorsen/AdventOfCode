def shuffle_cups(c, d):
    front_cup = c[0]
    next_three = c[1:4]
    c = c[4:]
    insert_number = front_cup - 1
    while insert_number in next_three:
        insert_number -= 1
        if insert_number < min(c):
            insert_number = 1000000
    insert_index = d[insert_number] + 1
    for i in next_three:
        c.insert(insert_index, i)
        insert_index += 1
    c.append(front_cup)
    return c


cups = [x for x in range(10, 1000001)]  # Del 2
test_cups = [3, 8, 9, 1, 2, 5, 4, 6, 7]
actual_cups = [5, 8, 3, 9, 7, 6, 2, 4, 1]

for x in reversed(actual_cups):  # Del 2
    cups.insert(0, x)  # Del 2

dictionary_cups = {x: y for x, y in enumerate(cups)}
print(dictionary_cups)

runs = 10000000
for x in range(0, runs):
    print(x)
    cups = shuffle_cups(cups, dictionary_cups)

one_index = cups.index(1)  # Del 2
print(cups[one_index+1] * cups[one_index+2])  # Del 2
