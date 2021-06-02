import os, sys, re


def calculate(left, operator, right):
    if operator == '+':
        return left + right
    elif operator == '*':
        return left * right
    else:
        print("Wrong operator")
        return 0


def parenthesis_value(pos, exp):
    result = 0
    pos += 1
    p_o = '+'
    while exp[pos] != ')':
        if exp[pos] == '(':
            r, pos = parenthesis_value(pos, exp)
            result = calculate(result, p_o, r)
        elif re.search('[0-9]', exp[pos]):
            result = calculate(result, p_o, int(exp[pos]))
        elif re.search('[+*]', exp[pos]):
            p_o = exp[pos]
        pos += 1

    return [result, pos]


with open(os.path.join(sys.path[0], 'input.txt'), mode='r', encoding='utf-8') as _file:
    info = _file.read().split('\n')

total_sum = 0

for line in info:
    line = line.replace(' ', '')
    value = 0
    position = 0
    previous_operator = "+"
    while position < len(line):
        if line[position] == '(':
            v, position = parenthesis_value(position, line)
            value = calculate(value, previous_operator, v)
        elif re.search('[0-9]', line[position]):
            value = calculate(value, previous_operator, int(line[position]))
        elif re.search('[+*]', line[position]):
            previous_operator = line[position]

        position += 1
    total_sum += value

print(total_sum)
