import re


test = '123'
print('Test', test[:-2])
re_test = re.search('[a-z]', test)
if re_test:
    print('Har bokstav')
else:
    print('Ingen bokstav')

if type(test) == str:
    print('is string')

a = 0
b = 0
if a == b > 0:
    print('ab')
