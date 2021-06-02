import os, sys, re, copy


def find_sub_rule(r, r_dict):
    if re.search('[a-z]', r_dict[r]):
        return re.search('[a-z]', r_dict[r]).group()

    sub_rules = list()  # Liste over reglene i denne posisjonen

    options = r_dict[r].split('|')
    for option in options:
        temp_sub_rules = list()
        order = re.findall('[0-9]+', option)
        for o in order:
            temp_sub_rules.append(find_sub_rule(o, r_dict))

        temp_subs = temp_sub_rules[-1]
        for i in range(len(temp_sub_rules)-2, -1, -1):
            temp_joined_subs = list()
            if type(temp_sub_rules[i]) == str:
                for k in range(0, len(temp_subs)):
                    temp_joined_subs.append(temp_sub_rules[i] + temp_subs[k])
            else:
                for j in range(0, len(temp_sub_rules[i])):
                    for k in range(0, len(temp_subs)):
                        temp_joined_subs.append(temp_sub_rules[i][j] + temp_subs[k])
            temp_subs = copy.deepcopy(temp_joined_subs)

        for sub in temp_subs:
            sub_rules.append(sub)

    return sub_rules


with open(os.path.join(sys.path[0], 'input.txt'), mode='r', encoding='utf-8') as _file:
    input_rules, input_data = _file.read().split('\n\n')

input_rules = input_rules.split('\n')
rules = {}
for rule in input_rules:
    number, info = rule.split(':')
    rules[number] = info

data = input_data.split('\n')

possibilities = find_sub_rule('0', rules)

match_sum = 0
for element in data:
    if element in possibilities:
        match_sum += 1

print(match_sum)


