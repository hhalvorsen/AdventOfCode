import os, sys, re, copy


def overwrite(number, mask):
    overwritten_number = [x if x == "1" else "0" for x in mask]
    b_number = bin(number)
    b_string = str(b_number)
    for j in range(-1, -(len(b_string)-1), -1):

        if mask[j] == "X":
            overwritten_number[j] = b_string[j]
        else:
            overwritten_number[j] = mask[j]

    result = ""
    return int(result.join(overwritten_number), 2)


def overwrite_memory_addresses(original_address, mask):
    masked_address = list(mask)
    b_number = bin(original_address)
    b_string = str(b_number)
    # Sett elementer med 0 i mask til sin verdi i original adresse
    for j in range(-1, -(len(b_string) - 1), -1):
        if mask[j] == "0":
            masked_address[j] = b_string[j]

    #
    binary_addresses = list()
    binary_addresses.append(["0" if x == "X" else x for x in masked_address])
    for k in range(-1, -len(masked_address)-1, -1):
        if masked_address[k] == "X":
            extra_addresses = copy.deepcopy(binary_addresses)
            for m in extra_addresses:
                m[k] = "1"
                binary_addresses.append(m)

    addresses = list()
    for k in binary_addresses:
        temp_address = ""
        addresses.append(int(temp_address.join(k), 2))

    return addresses


with open(os.path.join(sys.path[0], 'input.txt'), mode='r', encoding='utf-8') as _file:
    info = _file.read().split('\n')

# Del 2
test = "1234"
for q in range(-1, -(len(test) - 1), -1):
    print(test[q])

info_split = [x.split(" ") for x in info]
current_mask = info_split[0][2]
for i in range(0, len(info_split)):
    if info_split[i][0][:3] == "mem":
        info_split[i][0] = int(re.findall("[0-9]+", info_split[i][0])[0])

memory = {}
for i in range(1, len(info_split)):
    if type(info_split[i][0]) != int:
        current_mask = info_split[i][2]
    else:
        write_to_addresses = overwrite_memory_addresses(info_split[i][0], current_mask)
        for y in write_to_addresses:
            memory[y] = int(info_split[i][2])
print(memory)
memory_sum = sum(memory.values())
print(memory_sum)

"""
# Del 1 ikke komplett, slettet linjer ved feil
for i in range(1, len(info_split)):
    if info_split[i][0][:3] == "mem":
        memory[int(re.findall("[0-9]+", info_split[i][0])[0])] = overwrite(int(info_split[i][2]), current_mask)
    else:
        current_mask = info_split[i][2]

print(memory)
memory_sum = sum([memory[x] for x in memory])
print(memory_sum)

"""
