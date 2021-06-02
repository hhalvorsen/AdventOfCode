number_list = {2: 0, 20: 1, 0: 2, 4: 3, 1: 4}
counter = len(number_list)
temp_numb = 17
while counter < 30000000 - 1:
    if temp_numb in number_list:
        insert_numb = temp_numb
        temp_numb = counter - number_list[temp_numb]
        number_list[insert_numb] = counter
    else:
        number_list[temp_numb] = counter
        temp_numb = 0
    counter += 1
print(temp_numb)


