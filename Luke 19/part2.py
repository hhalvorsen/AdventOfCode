import os, sys, re, copy


def find_unaffected_sub_rule(r, r_dict):
    sub_rules = list()  # Liste over reglene i denne posisjonen

    if r == '11':
        return ['affected11']
    if r == '8':
        return ['affected8']

    if re.search('[a-z]', r_dict[r]):
        return re.search('[a-z]', r_dict[r]).group()

    options = r_dict[r].split('|')
    for option in options:
        temp_sub_rules = list()
        order = re.findall('[0-9]+', option)
        for o in order:
            temp_sub_rules.append(find_unaffected_sub_rule(o, r_dict))

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


with open(os.path.join(sys.path[0], 'input_extra.txt'), mode='r', encoding='utf-8') as _file:
    input_rules, input_data = _file.read().split('\n\n')

input_rules = input_rules.split('\n')
rules = {}
for rule in input_rules:
    number, info = rule.split(':')
    rules[number] = info

impact_rules = {}
for key in rules:
    impact_rules[key] = find_unaffected_sub_rule(key, rules)

possibilities_42 = impact_rules['42']
possibilities_31 = impact_rules['31']
e_length_42 = len(possibilities_42[0])
e_length_31 = len(possibilities_31[0])

# Ingen av elementene i possibilities_42 matcher elementene i possibilities_31

data = input_data.split('\n')

match_sum = 0
for element in data:
    print(element)
    ele_length = len(element)
    if ele_length >= e_length_42 + e_length_42 + e_length_31:
        if element[:e_length_42] in possibilities_42:
            pos_42 = e_length_42
            matches_42 = 0
            while pos_42 + e_length_42 < ele_length and element[pos_42:pos_42 + e_length_42] in possibilities_42:
                pos_42 += e_length_42
                matches_42 += 1
            print('42', matches_42)
            pos_31 = pos_42
            matches_31 = 0
            while (pos_31 + e_length_31 < ele_length and element[pos_31:pos_31 + e_length_31] in possibilities_31)\
                    or (element[pos_31:] in possibilities_31):
                pos_31 += e_length_31
                matches_31 += 1
            print('31', matches_31)

            if matches_42 >= matches_31 > 0 and pos_31 == ele_length:
                print('Match')
                match_sum += 1

print(match_sum)
