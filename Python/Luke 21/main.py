import os, sys, re


with open(os.path.join(sys.path[0], 'input.txt'), mode='r', encoding='utf-8') as _file:
    info = _file.read().split('\n')


possible_ingredients = {}
all_ingredients = {}
for line in info:
    listed_line = re.findall('[a-z]+', line)
    ingredients = listed_line[:listed_line.index('contains')]
    allergens = listed_line[listed_line.index('contains')+1:]
    for allergen in allergens:
        if allergen in possible_ingredients:
            possible_ingredients[allergen].append(ingredients)
        else:
            possible_ingredients[allergen] = [ingredients]

    for ingredient in ingredients:
        if ingredient in all_ingredients:
            all_ingredients[ingredient] += 1
        else:
            all_ingredients[ingredient] = 1

appearances = 0
safe_ingredients = list()
allergen_possible_ingredients = {}
for ingredient_key in all_ingredients:
    safe = True
    for allergen_key in possible_ingredients:
        number_of_lists = len(possible_ingredients[allergen_key])
        ingredient_in_list = 0
        for ingredient_list in possible_ingredients[allergen_key]:
            if ingredient_key in ingredient_list:
                ingredient_in_list += 1
        if ingredient_in_list == number_of_lists:
            safe = False
            if allergen_key in allergen_possible_ingredients:
                allergen_possible_ingredients[allergen_key].append(ingredient_key)
            else:
                allergen_possible_ingredients[allergen_key] = [ingredient_key]

    if safe:
        appearances += all_ingredients[ingredient_key]
        safe_ingredients.append(ingredient_key)

print(allergen_possible_ingredients)

allergen_ingredient_dict = {}
while len(allergen_possible_ingredients) > 0:
    pop_keys = list()
    for allergen_key in allergen_possible_ingredients:
        if len(allergen_possible_ingredients[allergen_key]) == 1:
            taken_ingredient = allergen_possible_ingredients[allergen_key][0]
            allergen_ingredient_dict[allergen_key] = taken_ingredient
            pop_keys.append(allergen_key)
            for sub_a_k in allergen_possible_ingredients:
                if taken_ingredient in allergen_possible_ingredients[sub_a_k]:
                    allergen_possible_ingredients[sub_a_k].\
                        pop(allergen_possible_ingredients[sub_a_k].index(taken_ingredient))

    for p in pop_keys:
        allergen_possible_ingredients.pop(p)

print(allergen_ingredient_dict)

allergens_list = list(allergen_ingredient_dict.keys())
allergens_list.sort()
canonical_dangerous_ingredient_list = ""
for a in allergens_list:
    canonical_dangerous_ingredient_list = canonical_dangerous_ingredient_list + allergen_ingredient_dict[a] + ','

print('Part 1:', appearances)
print(canonical_dangerous_ingredient_list)



