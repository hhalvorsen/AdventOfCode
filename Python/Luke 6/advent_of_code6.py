import sys, os, re


def count_group_yes(group_answers):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    return sum(1 for i in range(0, len(alphabet)) if alphabet[i] in group_answers)


def group_similar_answers(group_a):
    individual = group_a.split('\n')
    answered = individual[0]
    for i in individual:
        temp = ""
        for j in range(0, len(answered)):
            if answered[j] in i:
                temp += answered[j]

        answered = temp

    return len(answered)


with open(os.path.join(sys.path[0], 'input.txt'), mode='r', encoding='utf-8') as _file:
    records = _file.read().split('\n\n')

print(sum(count_group_yes(group) for group in records))
print(sum(group_similar_answers(group) for group in records))

