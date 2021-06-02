import os, sys, re


def calculate(left, operator, right):
    if operator == '+':
        return left + right
    elif operator == '*':
        return left * right
    else:
        print("Wrong operator")
        return 0


def parenthesis_value(pos, exp, direction):
    result = 0
    p_o = '+'
    if direction == 1:
        par_end = parenthesis_end(pos, exp, direction)
        if par_end + 1 == len(exp):
            exp = eliminate_pluses(exp[pos:])
        else:
            exp = eliminate_pluses(exp[pos:par_end])
        pos += 1
        while exp[pos] != ')':
            if exp[pos] == '(':
                r, pos = parenthesis_value(pos, exp, direction)
                result = calculate(result, p_o, r)
            elif re.search('[0-9]', exp[pos]):
                numb = re.search('[0-9]+', line[pos:]).group()
                result = calculate(result, p_o, int(numb))
                pos = pos + len(numb) - 1
            elif re.search('[+*]', exp[pos]):
                p_o = exp[pos]
            pos += 1
    elif direction == -1:
        par_end = parenthesis_end(pos, exp, direction)
        if pos + 1 == len(exp):
            exp = eliminate_pluses(exp[par_end:])
        else:
            exp = eliminate_pluses(exp[par_end:pos+1])

        pos -= 1
        while exp[pos] != '(':
            if exp[pos] == ')':
                r, pos = parenthesis_value(pos, exp, direction)
                result = calculate(result, p_o, r)
            elif re.search('[0-9]', exp[pos]):
                i = 1
                while pos - i > -1 and re.search('[0-9]', exp[pos - i]):
                    i += 1
                numb = int(exp[pos - i + 1:pos + 1])
                result = calculate(result, p_o, numb)
                pos = pos - i + 1
            elif re.search('[+*]', exp[pos]):
                p_o = exp[pos]
            pos -= 1

    print("result", result, "pos", pos)
    return [result, pos]


def calculate_plus(pos, exp):
    left_pos = pos - 1
    right_pos = pos + 1
    left = 0
    right = 0
    if exp[left_pos] == ')':
        left, left_pos = parenthesis_value(left_pos, exp, -1)
    elif re.search('[0-9]', exp[left_pos]):
        i = 1
        while left_pos - i > -1 and re.search('[0-9]', exp[left_pos - i]):
            i += 1
        left = int(exp[left_pos-i+1:left_pos+1])
        left_pos = left_pos-i+1

    if exp[right_pos] == '(':
        right, right_pos = parenthesis_value(right_pos, exp, 1)
    elif re.search('[0-9]', exp[right_pos]):
        right = int(re.search('[0-9]+', exp[right_pos:]).group())
    return [left + right, left_pos, right_pos]


def eliminate_pluses(exp):
    while re.search('[+]', exp):
        print(exp)
        plus_position = re.search('[+]', exp).start()
        plus_sum, left_position, right_position = calculate_plus(plus_position, exp)
        print(exp[:left_position] + str(plus_sum) + exp[right_position+1:])
        exp = exp[:left_position] + str(plus_sum) + exp[right_position+1:]
    return exp


def parenthesis_end(pos, exp, direction):
    p = 1
    while p > 0:
        pos += direction
        if direction == 1:
            if exp[pos] == '(':
                p += 1
            elif exp[pos] == ')':
                p -= 1
        if direction == -1:
            if exp[pos] == ')':
                p += 1
            elif exp[pos] == '(':
                p -= 1

    return pos


with open(os.path.join(sys.path[0], 'input.txt'), mode='r', encoding='utf-8') as _file:
    info = _file.read().split('\n')

total_sum = 0

for line in info:
    line = line.replace(' ', '')
    print(line)

    line = eliminate_pluses(line)

    value = 0
    position = 0
    previous_operator = "+"
    while position < len(line):
        if line[position] == '(':
            v, position = parenthesis_value(position, line, 1)
            value = calculate(value, previous_operator, v)
        elif re.search('[0-9]', line[position]):
            number = re.search('[0-9]+', line[position:]).group()
            value = calculate(value, previous_operator, int(number))
            position = position + len(number) - 1
        elif re.search('[+*]', line[position]):
            previous_operator = line[position]
        position += 1
    total_sum += value

print(total_sum)
