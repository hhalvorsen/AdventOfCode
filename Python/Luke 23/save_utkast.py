import copy


def shuffle_cups(tail_dic, front_dic, runs):
    keys_list = list(tail_dic.keys())
    current_cup = keys_list[0]
    last_three = keys_list[-3:]
    # end_and_front = keys_list[-3:] + keys_list[:6]
    for run in range(0, runs):
        print('-------------------------')

        destination_cup = current_cup - 1
        next_cup = tail_dic[tail_dic[current_cup][0]][-1]
        while destination_cup in tail_dic[current_cup]:
            destination_cup -= 1
            if destination_cup < 1:
                destination_cup = 9

        print_list = list()
        print_list.append(current_cup)
        while len(print_list) < 9:
            print_list.append(tail_dic[print_list[-1]][0])
        print(tail_dic)
        print(print_list)
        print('Current cup', current_cup, tail_dic[current_cup])
        print('Destination', destination_cup)
        print('Next Cup', next_cup)
        print('Last three', last_three)

        # Oppdatere tail
        destination_cup_tail = copy.deepcopy(tail_dic[destination_cup])
        tail_dic[destination_cup] = copy.deepcopy(tail_dic[current_cup])

        print(destination_cup_tail)
        print(tail_dic[current_cup])

        if destination_cup not in last_three:
            start = 2
            for i in tail_dic[current_cup]:
                j = start
                index = 0
                while j < len(tail_dic[i]):
                    tail_dic[i][j] = destination_cup_tail[index]
                    j += 1
                    index += 1
                start -= 1
        else:
            start = last_three.index(destination_cup) + 1
            j = start
            while j < len():
                index = 0


        tail_dic[current_cup] = [next_cup] + tail_dic[next_cup][:2]
        tail_dic[last_three[1]][-1] = tail_dic[current_cup][0]
        tail_dic[last_three[-1]][1] = tail_dic[current_cup][0]
        tail_dic[last_three[-1]][-1] = tail_dic[current_cup][1]

        last_three.pop(0)
        last_three.append(current_cup)
        if destination_cup in last_three:
            index = last_three.index(destination_cup)
            for i in tail_dic[destination_cup]:
                index += 1
                last_three.insert(index, i)

            while len(last_three) > 3:
                last_three.pop(0)


        # tail_dic[tail_dic[current_cup]['present'][1]][-1] = tail_dic[current_cup][0]
        # tail_dic[tail_dic[current_cup]['present'][0]][1] = tail_dic[current_cup][0]
        # tail_dic[tail_dic[current_cup]['present'][0]][-1] = tail_dic[current_cup][1]

        # Oppdatere present

        front_dic[current_cup] = last_three[:1] + [front_dic[last_three[1]][2]]

        # print(tail_dic)

        current_cup = next_cup


# cups = [x for x in range(10, 1000001)]  # Del 2
test_cups = [3, 8, 9, 1, 2, 5, 4, 6, 7]
actual_cups = [5, 8, 3, 9, 7, 6, 2, 4, 1]

# for x in reversed(actual_cups):  # Del 2
#    cups.insert(0, x)  # Del 2
# Husk å endre grenser for destination cup
cups = test_cups
tail_dictionary = {}
front_dictionary = {}

cups_length = len(cups)
surroundings = [1, 2, 3, cups_length - 1, cups_length - 2, cups_length - 3]
w = 0
while w < cups_length:
    tail_dictionary[cups[w]] = [cups[surroundings[0]], cups[surroundings[1]], cups[surroundings[2]]]
    front_dictionary[cups[w]] = [cups[surroundings[5]], cups[surroundings[4]], cups[surroundings[3]]]
    w += 1
    for x in range(0, len(surroundings)):
        surroundings[x] += 1
        if surroundings[x] >= cups_length:
            surroundings[x] = 0

print(tail_dictionary)
print(front_dictionary)
r = 100
shuffle_cups(tail_dictionary, front_dictionary, r)
"""
runs = 10000000
for x in range(0, runs):
    print(x)
    cups = shuffle_cups(cups, dictionary_cups)

one_index = cups.index(1)  # Del 2
print(cups[one_index+1] * cups[one_index+2])  # Del 2
"""

# NYTT FORSØK

import copy


def shuffle_cups(tail_dic, front_dic, runs):
    keys_list = list(tail_dic.keys())
    current_cup = keys_list[0]
    last_three = keys_list[-3:]
    end_and_front = keys_list[-3:] + keys_list[:6]
    for run in range(0, runs):
        print('-------------------------')

        destination_cup = current_cup - 1
        next_cup = tail_dic[tail_dic[current_cup][0]][-1]
        while destination_cup in tail_dic[current_cup]:
            destination_cup -= 1
            if destination_cup < 1:
                destination_cup = 9

        print_list = list()
        print_list.append(current_cup)
        while len(print_list) < 9:
            print_list.append(tail_dic[print_list[-1]][0])
        print(tail_dic)
        print(print_list)
        print('Current cup', current_cup, tail_dic[current_cup])
        print('Destination', destination_cup)
        print('Next Cup', next_cup)
        print('Last three', last_three)

        # Oppdatere tail
        destination_cup_tail = copy.deepcopy(tail_dic[destination_cup])
        tail_dic[destination_cup] = copy.deepcopy(tail_dic[current_cup])

        print(destination_cup_tail)
        print(tail_dic[current_cup])

        # Remove current tail from end_and_start, current can stay as it will keep its position
        stop_pop = end_and_front.index(current_cup)
        start_pop = stop_pop + 3
        while start_pop > stop_pop:
            end_and_front.pop(start_pop)
            start_pop -= 1

        if destination_cup not in end_and_front[:3]:
            start = 2
            for i in tail_dic[current_cup]:
                j = start
                index = 0
                while j < len(tail_dic[i]):
                    tail_dic[i][j] = destination_cup_tail[index]
                    j += 1
                    index += 1
                start -= 1
        else:
            for i in reversed(destination_cup_tail):
                end_and_front.insert(3, i)
            for i in range(0, len(end_and_front)-3):
                tail_dic[i] = end_and_front[i:i+4]

        tail_dic[current_cup] = [next_cup] + tail_dic[next_cup][:2]
        tail_dic[last_three[1]][-1] = tail_dic[current_cup][0]
        tail_dic[last_three[-1]][1] = tail_dic[current_cup][0]
        tail_dic[last_three[-1]][-1] = tail_dic[current_cup][1]

        last_three.pop(0)
        last_three.append(current_cup)
        if destination_cup in last_three:
            index = last_three.index(destination_cup)
            for i in tail_dic[destination_cup]:
                index += 1
                last_three.insert(index, i)

            while len(last_three) > 3:
                last_three.pop(0)


        # tail_dic[tail_dic[current_cup]['present'][1]][-1] = tail_dic[current_cup][0]
        # tail_dic[tail_dic[current_cup]['present'][0]][1] = tail_dic[current_cup][0]
        # tail_dic[tail_dic[current_cup]['present'][0]][-1] = tail_dic[current_cup][1]

        # Oppdatere present

        front_dic[current_cup] = last_three[:1] + [front_dic[last_three[1]][2]]

        # print(tail_dic)

        current_cup = next_cup


# cups = [x for x in range(10, 1000001)]  # Del 2
test_cups = [3, 8, 9, 1, 2, 5, 4, 6, 7]
actual_cups = [5, 8, 3, 9, 7, 6, 2, 4, 1]

# for x in reversed(actual_cups):  # Del 2
#    cups.insert(0, x)  # Del 2
# Husk å endre grenser for destination cup
cups = test_cups
tail_dictionary = {}
front_dictionary = {}

cups_length = len(cups)
surroundings = [1, 2, 3, cups_length - 1, cups_length - 2, cups_length - 3]
w = 0
while w < cups_length:
    tail_dictionary[cups[w]] = [cups[surroundings[0]], cups[surroundings[1]], cups[surroundings[2]]]
    front_dictionary[cups[w]] = [cups[surroundings[5]], cups[surroundings[4]], cups[surroundings[3]]]
    w += 1
    for x in range(0, len(surroundings)):
        surroundings[x] += 1
        if surroundings[x] >= cups_length:
            surroundings[x] = 0

print(tail_dictionary)
print(front_dictionary)
r = 100
shuffle_cups(tail_dictionary, front_dictionary, r)
"""
runs = 10000000
for x in range(0, runs):
    print(x)
    cups = shuffle_cups(cups, dictionary_cups)

one_index = cups.index(1)  # Del 2
print(cups[one_index+1] * cups[one_index+2])  # Del 2
"""

# ---------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------

import copy


def shuffle_cups(tail_dic, front_dic, runs):
    keys_list = list(tail_dic.keys())
    current_cup = keys_list[0]
    last_cup = keys_list[-1]
    for run in range(0, runs):
        print('-------------------------')
        print('Tail', tail_dic)
        print('Front', front_dic)

        # Find destination cup
        destination_cup = current_cup - 1
        next_cup = tail_dic[tail_dic[current_cup][0]][-1]
        while destination_cup in tail_dic[current_cup] or destination_cup < 1:
            destination_cup -= 1
            if destination_cup < 1:
                destination_cup = 9
            print(destination_cup)

        print_list = list()
        print_list.append(current_cup)
        while len(print_list) < 9:
            print_list.append(tail_dic[print_list[-1]][0])
        print(print_list)
        print('Current cup', current_cup, tail_dic[current_cup])
        print('Destination', destination_cup)
        print('Next Cup', next_cup)

        # Save tail and front of current cup
        current_cup_tail = copy.deepcopy(tail_dic[current_cup])
        current_cup_front = copy.deepcopy(front_dic[current_cup])

        """
        # Delete current cup and current cup tail elements from circle and update affected elements
        # Both tail_dic and front_dic
        tail_dic.pop(current_cup)
        front_dic.pop(current_cup)
        for i in current_cup_tail:
            tail_dic.pop(i)
            front_dic.pop(i)
        """

        # Update affected elements
        # Tail_dic
        tail_dic[current_cup_front[0]][2] = next_cup
        tail_dic[current_cup_front[1]][1] = next_cup
        tail_dic[current_cup_front[1]][2] = tail_dic[next_cup][0]
        tail_dic[current_cup_front[2]][0] = next_cup
        tail_dic[current_cup_front[2]][1] = tail_dic[next_cup][0]
        tail_dic[current_cup_front[2]][2] = tail_dic[next_cup][1]
        # Front_dic
        front_dic[next_cup] = copy.deepcopy(current_cup_front)
        front_dic[tail_dic[next_cup][0]][0] = current_cup_front[1]
        front_dic[tail_dic[next_cup][0]][1] = current_cup_front[2]
        front_dic[tail_dic[next_cup][1]][0] = current_cup_front[2]

        # end_and_front = front_dic[next_cup] + [next_cup] + tail_dic[next_cup]

        # Save tail and front of destination cup and last cup
        destination_cup_tail = copy.deepcopy(tail_dic[destination_cup])
        destination_cup_front = copy.deepcopy(front_dic[destination_cup])
        last_cup_tail = copy.deepcopy(tail_dic[last_cup])
        last_cup_front = copy.deepcopy(front_dic[last_cup])
        next_cup_tail = copy.deepcopy(tail_dic[next_cup])
        next_cup_front = copy.deepcopy(front_dic[next_cup])

        # Insert current_cup into circle and update affected elements
        # Both tail and front_dic

        tail_dic[last_cup_front[2]][1] = current_cup
        tail_dic[last_cup_front[2]][2] = last_cup_tail[0]
        tail_dic[last_cup_front[1]][2] = current_cup
        # front_dic[current_cup] and the elements in front are untouched by the insertion of current_cup at the end
        front_dic[next_cup] = next_cup_front[1:] + [current_cup]
        front_dic[next_cup_tail[0]] = [last_cup, current_cup, next_cup]
        front_dic[next_cup_tail[1]][0] = current_cup
        tail_dic[last_cup] = [current_cup, next_cup, current_cup_tail[0]]

        # Insert current cup tail elements into circle and update affected elements
        # Both tail and front_dic
        tail_dic[destination_cup] = copy.deepcopy(current_cup_tail)
        tail_dic[current_cup_tail[0]] = current_cup_tail[1:] + [destination_cup_tail[0]]
        tail_dic[current_cup_tail[1]] = [current_cup_tail[2]] + destination_cup_tail[:2]
        tail_dic[current_cup_tail[2]] = copy.deepcopy(destination_cup_tail)
        tail_dic[current_cup] = [next_cup] + current_cup_tail[:2]
        front_dic[destination_cup_tail[0]] = copy.deepcopy(current_cup_tail)
        front_dic[destination_cup_tail[1]] = current_cup_tail[1:] + [destination_cup_tail[0]]
        front_dic[destination_cup_tail[2]][0] = current_cup_tail[2]
        front_dic[current_cup_tail[2]] = [destination_cup] + current_cup_tail[:2]
        if next_cup == destination_cup:
            front_dic[current_cup_tail[1]] = [current_cup, destination_cup, current_cup_tail[0]]
            front_dic[current_cup_tail[0]] = [last_cup, current_cup, destination_cup]
        else:
            front_dic[current_cup_tail[1]] = [destination_cup_front[2], destination_cup, current_cup_tail[0]]
            front_dic[current_cup_tail[0]] = destination_cup_front[1:] + [destination_cup]
            tail_dic[destination_cup_front[2]] = [destination_cup] + current_cup_tail[:2]
            tail_dic[destination_cup_front[1]][2] = current_cup_tail[0]

        # Update last cup and current cup
        last_cup = current_cup
        current_cup = next_cup


# cups = [x for x in range(10, 1000001)]  # Del 2
test_cups = [3, 8, 9, 1, 2, 5, 4, 6, 7]
actual_cups = [5, 8, 3, 9, 7, 6, 2, 4, 1]

# for x in reversed(actual_cups):  # Del 2
#    cups.insert(0, x)  # Del 2
# Husk å endre grenser for destination cup
cups = test_cups
tail_dictionary = {}
front_dictionary = {}

cups_length = len(cups)
surroundings = [1, 2, 3, cups_length - 1, cups_length - 2, cups_length - 3]
w = 0
while w < cups_length:
    tail_dictionary[cups[w]] = [cups[surroundings[0]], cups[surroundings[1]], cups[surroundings[2]]]
    front_dictionary[cups[w]] = [cups[surroundings[5]], cups[surroundings[4]], cups[surroundings[3]]]
    w += 1
    for x in range(0, len(surroundings)):
        surroundings[x] += 1
        if surroundings[x] >= cups_length:
            surroundings[x] = 0

print(tail_dictionary)
print(front_dictionary)
r = 100
shuffle_cups(tail_dictionary, front_dictionary, r)
"""
runs = 10000000
for x in range(0, runs):
    print(x)
    cups = shuffle_cups(cups, dictionary_cups)

one_index = cups.index(1)  # Del 2
print(cups[one_index+1] * cups[one_index+2])  # Del 2
"""

# -----------------------------------------------------------------
# -----------------------------------------------------------------

import copy


def shuffle_cups(tail_dic, front_dic, runs):
    keys_list = list(tail_dic.keys())
    current_cup = keys_list[0]
    last_cup = keys_list[-1]
    end_and_front = keys_list[-3:] + keys_list[:6]
    for run in range(0, runs):
        print('-------------------------')
        print('Tail', tail_dic)
        print('Front', front_dic)

        # Find destination cup
        destination_cup = current_cup - 1
        next_cup = tail_dic[tail_dic[current_cup][0]][-1]
        while destination_cup in tail_dic[current_cup] or destination_cup < 1:
            destination_cup -= 1
            if destination_cup < 1:
                destination_cup = 9
            print(destination_cup)

        print_list = list()
        print_list.append(current_cup)
        while len(print_list) < 9:
            print_list.append(tail_dic[print_list[-1]][0])
        print(print_list)
        print('Current cup', current_cup, tail_dic[current_cup])
        print('Destination', destination_cup)
        print('Next Cup', next_cup)
        print('End and front', end_and_front)

        # Save tail and front of current cup
        current_cup_tail = copy.deepcopy(tail_dic[current_cup])
        current_cup_front = copy.deepcopy(front_dic[current_cup])

        """
        # Delete current cup and current cup tail elements from circle and update affected elements
        # Both tail_dic and front_dic
        tail_dic.pop(current_cup)
        front_dic.pop(current_cup)
        for i in current_cup_tail:
            tail_dic.pop(i)
            front_dic.pop(i)
        """
        # Delete elements from end_and_front
        stop_pop_index = end_and_front.index(current_cup)
        start_pop_index = stop_pop_index + 3
        while start_pop_index > stop_pop_index:
            end_and_front.pop(start_pop_index)
            start_pop_index -= 1

        if destination_cup in end_and_front:
            insert_index = end_and_front.index(destination_cup) + 1
            for i in reversed(current_cup_tail):
                end_and_front.insert(insert_index, i)

            for i in range(0, len(end_and_front)-3):
                tail_dic[end_and_front[i]] = end_and_front[i+1:i+4]
                front_dic[end_and_front[i+3]] = end_and_front[i:i+3]


        # Update affected elements
        # Tail_dic
        tail_dic[current_cup_front[0]][2] = next_cup
        tail_dic[current_cup_front[1]][1] = next_cup
        tail_dic[current_cup_front[1]][2] = tail_dic[next_cup][0]
        tail_dic[current_cup_front[2]][0] = next_cup
        tail_dic[current_cup_front[2]][1] = tail_dic[next_cup][0]
        tail_dic[current_cup_front[2]][2] = tail_dic[next_cup][1]
        # Front_dic
        front_dic[next_cup] = copy.deepcopy(current_cup_front)
        front_dic[tail_dic[next_cup][0]][0] = current_cup_front[1]
        front_dic[tail_dic[next_cup][0]][1] = current_cup_front[2]
        front_dic[tail_dic[next_cup][1]][0] = current_cup_front[2]

        # end_and_front = front_dic[next_cup] + [next_cup] + tail_dic[next_cup]

        # Save tail and front of destination cup and last cup
        destination_cup_tail = copy.deepcopy(tail_dic[destination_cup])
        destination_cup_front = copy.deepcopy(front_dic[destination_cup])
        last_cup_tail = copy.deepcopy(tail_dic[last_cup])
        last_cup_front = copy.deepcopy(front_dic[last_cup])
        next_cup_tail = copy.deepcopy(tail_dic[next_cup])
        next_cup_front = copy.deepcopy(front_dic[next_cup])

        # Insert current_cup into circle and update affected elements
        # Both tail and front_dic

        tail_dic[last_cup_front[2]][1] = current_cup
        tail_dic[last_cup_front[2]][2] = last_cup_tail[0]
        tail_dic[last_cup_front[1]][2] = current_cup
        # front_dic[current_cup] and the elements in front are untouched by the insertion of current_cup at the end
        front_dic[next_cup] = next_cup_front[1:] + [current_cup]
        front_dic[next_cup_tail[0]] = [last_cup, current_cup, next_cup]
        front_dic[next_cup_tail[1]][0] = current_cup
        tail_dic[last_cup] = [current_cup, next_cup, current_cup_tail[0]]

        # Insert current cup tail elements into circle and update affected elements
        # Both tail and front_dic
        tail_dic[destination_cup] = copy.deepcopy(current_cup_tail)
        tail_dic[current_cup_tail[0]] = current_cup_tail[1:] + [destination_cup_tail[0]]
        tail_dic[current_cup_tail[1]] = [current_cup_tail[2]] + destination_cup_tail[:2]
        tail_dic[current_cup_tail[2]] = copy.deepcopy(destination_cup_tail)
        tail_dic[current_cup] = [next_cup] + current_cup_tail[:2]
        front_dic[destination_cup_tail[0]] = copy.deepcopy(current_cup_tail)
        front_dic[destination_cup_tail[1]] = current_cup_tail[1:] + [destination_cup_tail[0]]
        front_dic[destination_cup_tail[2]][0] = current_cup_tail[2]
        front_dic[current_cup_tail[2]] = [destination_cup] + current_cup_tail[:2]
        if next_cup == destination_cup:
            front_dic[current_cup_tail[1]] = [current_cup, destination_cup, current_cup_tail[0]]
            front_dic[current_cup_tail[0]] = [last_cup, current_cup, destination_cup]
        else:
            front_dic[current_cup_tail[1]] = [destination_cup_front[2], destination_cup, current_cup_tail[0]]
            front_dic[current_cup_tail[0]] = destination_cup_front[1:] + [destination_cup]
            tail_dic[destination_cup_front[2]] = [destination_cup] + current_cup_tail[:2]
            tail_dic[destination_cup_front[1]][2] = current_cup_tail[0]

        # Update last cup and current cup
        last_cup = current_cup
        current_cup = next_cup


# cups = [x for x in range(10, 1000001)]  # Del 2
test_cups = [3, 8, 9, 1, 2, 5, 4, 6, 7]
actual_cups = [5, 8, 3, 9, 7, 6, 2, 4, 1]

# for x in reversed(actual_cups):  # Del 2
#    cups.insert(0, x)  # Del 2
# Husk å endre grenser for destination cup
cups = test_cups
tail_dictionary = {}
front_dictionary = {}

cups_length = len(cups)
surroundings = [1, 2, 3, cups_length - 1, cups_length - 2, cups_length - 3]
w = 0
while w < cups_length:
    tail_dictionary[cups[w]] = [cups[surroundings[0]], cups[surroundings[1]], cups[surroundings[2]]]
    front_dictionary[cups[w]] = [cups[surroundings[5]], cups[surroundings[4]], cups[surroundings[3]]]
    w += 1
    for x in range(0, len(surroundings)):
        surroundings[x] += 1
        if surroundings[x] >= cups_length:
            surroundings[x] = 0

print(tail_dictionary)
print(front_dictionary)
r = 100
shuffle_cups(tail_dictionary, front_dictionary, r)
"""
runs = 10000000
for x in range(0, runs):
    print(x)
    cups = shuffle_cups(cups, dictionary_cups)

one_index = cups.index(1)  # Del 2
print(cups[one_index+1] * cups[one_index+2])  # Del 2
"""