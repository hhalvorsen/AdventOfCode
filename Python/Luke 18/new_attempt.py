import os, sys, re


def is_inner_parenthesis(pos, exp):
    pos += 1
    while pos < len(exp):
        if exp[pos] == "(":
            return False
        elif exp[pos] == ")":
            return True
        pos += 1
    return True


def calculate_pluses(exp):
    while re.search('[+]', exp):
        plus_pos = re.search('[+]', exp).start()
        left = ""
        left_pos = plus_pos - 1
        while left_pos > -1 and re.search('[0-9]', exp[left_pos]):
            left = exp[left_pos] + left
            left_pos -= 1

        right_pos = plus_pos + 1
        right = re.search('[0-9]+', exp[right_pos:]).group()
        right_pos = right_pos + len(right)
        plus_sum = str(int(left) + int(right))
        if right_pos == len(exp):
            exp = exp[:left_pos+1] + plus_sum
        else:
            exp = exp[:left_pos+1] + plus_sum + exp[right_pos:]

    return exp


def calculate_multiplications(exp):
    while re.search('[*]', exp):
        multi_pos = re.search('[*]', exp).start()
        left = re.search('[0-9]+', exp).group()
        right = re.search('[0-9]+', exp[multi_pos:]).group()
        product = str(int(left)*int(right))
        if multi_pos + len(right) == len(exp):
            exp = product
        else:
            exp = product + exp[multi_pos+len(right)+1:]

    return exp


def calculate_parenthesis(exp):
    while re.search('[()]', exp):
        parenthesis_start = re.search('[(]', exp).start()
        while not is_inner_parenthesis(parenthesis_start, exp):
            parenthesis_start = parenthesis_start + 1 + re.search('[(]', exp[parenthesis_start+1:]).start()

        parenthesis_end = re.search('[)]', exp[parenthesis_start:]).start() + parenthesis_start
        parenthesis_expression = exp[parenthesis_start+1:parenthesis_end]
        parenthesis_expression = calculate_pluses(parenthesis_expression)
        parenthesis_expression = calculate_multiplications(parenthesis_expression)
        if parenthesis_end == len(exp)-1:
            exp = exp[:parenthesis_start] + parenthesis_expression
        else:
            exp = exp[:parenthesis_start] + parenthesis_expression + exp[parenthesis_end+1:]

    return exp


with open(os.path.join(sys.path[0], 'input.txt'), mode='r', encoding='utf-8') as _file:
    info = _file.read().split('\n')

total_sum = 0
for line in info:
    line = line.replace(' ', '')
    line = calculate_parenthesis(line)
    line = calculate_pluses(line)
    line = calculate_multiplications(line)
    total_sum += int(line)


print(total_sum)
