# print function
print(20 * 24 * 60)

# String concatenation
print('20 days are ' + str(28800) + ' minutes')

# String concatenation formatting
print(f'20 days are {20 * 24 * 60} minutes')

seconds_in_day = 24 * 60 * 60
name_of_unit = 'seconds'

print(f'5 days are {5 * seconds_in_day} seconds long')
print(f'10 days are {10 * seconds_in_day} {name_of_unit} long')


# Functions
def days_to_units():
    print(f'5 days are {5 * seconds_in_day} seconds long')
    print('this is weird that you have to indent')


def days_to_units(user_input):
    print(f'{user_input} days have {user_input * seconds_in_day} {name_of_unit}')


days_to_units(5)


def add_two_nums(x, y):
    print(f'{x} + {y} = {x + y}')


add_two_nums(5, 3)
