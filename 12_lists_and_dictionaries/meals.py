breakfast = ['Egg Sandwich', 'Bagel', 'Coffee']
lunch = ['BLT', 'PB&J', 'Turkey Sandwich']
dinner = ['Soup', 'Salad', 'Spaghetti', 'Taco']

menus = [
    ['Egg Sandwich', 'Bagel', 'Coffee'],
    ['BLT', 'PB&J', 'Turkey Sandwich'],
    ['Soup', 'Salad', 'Spaghetti', 'Taco']
]

print('Breakfast Menu:\t', menus[0])
print('Lunch Menu:\t', menus[1])
print('Dinner Menu:\t', menus[2])

print(menus[0][1])

menus = {
    'Breakfast': ['Egg Sandwich', 'Bagel', 'Coffee'],
    'Lunch': ['BLT', 'PB&J', 'Turkey Sandwich'],
    'Dinner': ['Soup', 'Salad', 'Spaghetti', 'Taco']
}

# This will print only the keys
for item in menus:
    print(item)

# This will print the keys and values
for name, menu in menus.items():
    print(name, ':', menu)

person = {
    'name': 'Sarah Smith',
    'city': 'Orlando',
    'age': '45'
}

print(person.get('name'), 'is', person.get('age'), 'years old.')
