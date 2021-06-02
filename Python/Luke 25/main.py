def find_loop_size(p_key):
    value = 1
    s_number = 7
    l_size = 0
    while value != p_key:
        value = transform(value, s_number)
        l_size += 1
        if l_size > 1000000000000:
            print('1000000000000 iterations')
            break
    print(value, l_size)
    return l_size


def transform(value, s_number):
    value *= s_number
    return value % 20201227


def calculate_encryption_key(p_key, l_size):
    value = 1
    for i in range(0, l_size):
        value = transform(value, p_key)
    return value


test_key1 = 5764801
test_key2 = 17807724

public_key1 = 12578151
public_key2 = 5051300

loop_size = find_loop_size(public_key1)
encryption_key = calculate_encryption_key(public_key2, loop_size)
print(encryption_key)
