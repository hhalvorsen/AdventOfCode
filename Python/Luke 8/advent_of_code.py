import sys, os, re
fields = ('byr','iyr','eyr','hgt','hcl','ecl','pid')
eye_colors = ('amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth')
hcl_pattern = re.compile("^#[a-f0-9]{6}$")
pid_pattern = re.compile("^[0-9]{9}$")


def check(record):
    for field in fields:
        if (field not in record):
            return False
    return check_valid_values(record)


def check_valid_values(record):
    record_pairs = record.split() # ['byr:123', 'iyr:24']
    for pair in record_pairs:
        att, value = pair.split(':') 
        if(att == 'byr'):
            if(int(value) not in range(1920, 2003)):
                return False
        elif(att == 'iyr'):
            if(int(value) not in range(2010, 2021)):
                return False
        elif(att == 'eyr'):
            if(int(value) not in range(2020, 2031)):
                return False
        elif(att == 'hgt'):
            height, unit = value[:-2], value[-2:]
            if (unit not in ('cm','in')):
                return False
            if(unit == 'cm' and int(height) not in range(150, 194)):
                return False
            elif(unit == 'in' and int(height) not in range(59, 77)):
                return False
        elif(att == 'hcl'):
            if(not hcl_pattern.match(value)):
                return False 
        elif(att == 'ecl'):
            num = sum(map(value.count, eye_colors))
            if(num != 1):
                return False
            print(pair)
        elif(att == 'pid'):
            if(not pid_pattern.match(value)):
                return False
        elif(att == 'cid'):
            pass   
        else:
            return False
    return True


with open(os.path.join(sys.path[0],'input.txt'), mode='r', encoding='utf-8') as _file:
    records = _file.read().split('\n\n')
answer = sum([1 for record in records if check(record)])
print(answer)