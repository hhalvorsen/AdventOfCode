import sys, os


def find_differences(numbers):
    differences = [0, 0, 0, 1]
    for i in range(1, len(numbers)-1):
        diff = numbers[i] - numbers[i-1]
        differences[diff] += 1

    return differences[1] * differences[3]


def find_possibilities(numbers):
    possible_steps = [0]*len(numbers)
    possible_steps[-3:-1] = [1, 1, 1]

    for i in range(len(numbers)-4, -1, -1):
        next_three = [x - numbers[i] for x in numbers[i+1:i+4]]
        for j in range(0, len(next_three)):
            if next_three[j] < 4:
                possible_steps[i] += possible_steps[i+j+1]

    return possible_steps[0]


with open(os.path.join(sys.path[0], 'input.txt'), mode='r', encoding='utf-8') as _file:
    records = _file.read().split('\n')
numberlist = [int(record) for record in records]
numberlist.sort()
numberlist.insert(0, 0)
numberlist.append(numberlist[-1] + 3)
print(find_differences(numberlist))
print(find_possibilities(numberlist))
