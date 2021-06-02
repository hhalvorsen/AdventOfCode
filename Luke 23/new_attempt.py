def shuffle_cups(dic, runs):
    keys_list = list(dic.keys())
    destination_cup_max_value = max(keys_list)
    current_cup = keys_list[0]
    for run in range(0, runs):
        print(run)
        # Find the 2nd to 4th element
        tail_elements = list()
        element = current_cup
        for i in range(0, 3):
            tail_elements.append(dic[element]['tail'])
            element = dic[element]['tail']

        # Find the first cup in the next round
        next_cup = dic[element]['tail']

        # Find destination cup
        destination_cup = current_cup - 1
        while destination_cup in tail_elements or destination_cup < 1:
            destination_cup -= 1
            if destination_cup < 1:
                destination_cup = destination_cup_max_value
        """
        print('-------------------------')
        print(dic)
        print_list = list()
        print_list.append(current_cup)
        while len(print_list) < 9:
            print_list.append(dic[print_list[-1]]['tail'])
        print(print_list)
        print('Current cup', current_cup, tail_elements)
        print('Destination', destination_cup)
        print('Next Cup', next_cup)
        """

        # Remove tail_elements
        dic[current_cup]['tail'] = next_cup
        dic[next_cup]['front'] = current_cup

        # Insert tail_elements
        dic[dic[destination_cup]['tail']]['front'] = tail_elements[-1]
        dic[tail_elements[-1]]['tail'] = dic[destination_cup]['tail']
        dic[destination_cup]['tail'] = tail_elements[0]
        dic[tail_elements[0]]['front'] = destination_cup

        # Update last cup and current cup
        current_cup = next_cup


cups = [x for x in range(10, 1000001)]  # Del 2
test_cups = [3, 8, 9, 1, 2, 5, 4, 6, 7]
actual_cups = [5, 8, 3, 9, 7, 6, 2, 4, 1]

for x in reversed(actual_cups):  # Del 2
    cups.insert(0, x)  # Del 2

# cups = test_cups  # Del 1

cups_dictionary = {cups[0]: {'front': cups[-1], 'tail': cups[1]}}
for x in range(1, len(cups)-1):
    cups_dictionary[cups[x]] = {'front': cups[x-1], 'tail': cups[x+1]}
cups_dictionary[cups[-1]] = {'front': cups[-2], 'tail': cups[0]}

r = 10000000
shuffle_cups(cups_dictionary, r)

print(cups_dictionary[1]['tail'] * cups_dictionary[cups_dictionary[1]['tail']]['tail'])
