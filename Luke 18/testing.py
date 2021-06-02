import re


test = "123"
print(test[:0])
while re.search('2', test):
    print(test)
    test = "13"



